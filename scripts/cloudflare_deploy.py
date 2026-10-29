import os
import sys
import json
import urllib.request
import urllib.error

ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "a17978d12dc9d62ca76f7712fe8f758c")
ZONE_ID = os.environ.get("CLOUDFLARE_ZONE_ID", "eed02d9917c1a0c6144972136e836eba")
TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN", "")
EMAIL = os.environ.get("CLOUDFLARE_EMAIL", "quan.luunguyen@gmail.com")
DOMAIN = "renewablevietnam.com"
SUBDOMAIN = "invest.renewablevietnam.com"
SCRIPT_NAME = "invest-subdomain-proxy"

def cf_api(endpoint, method="GET", data=None, headers=None):
    if not TOKEN:
        raise ValueError("CLOUDFLARE_API_TOKEN or Global API Key is required.")
    
    url = f"https://api.cloudflare.com/client/v4{endpoint}"
    req_headers = {}

    # Auto-detect authentication scheme (Global API Key vs Scoped Token)
    if TOKEN.startswith("cfk_") or ("@" in EMAIL and not TOKEN.startswith("cfat_")):
        req_headers["X-Auth-Key"] = TOKEN
        req_headers["X-Auth-Email"] = EMAIL
    else:
        req_headers["Authorization"] = f"Bearer {TOKEN}"

    if headers:
        req_headers.update(headers)
    
    body = None
    if data is not None:
        if isinstance(data, (dict, list)):
            body = json.dumps(data).encode("utf-8")
            req_headers["Content-Type"] = "application/json"
        elif isinstance(data, bytes):
            body = data
        elif isinstance(data, str):
            body = data.encode("utf-8")

    req = urllib.request.Request(url, data=body, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            res_body = resp.read().decode("utf-8")
            return json.loads(res_body) if res_body else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        print(f"HTTPError {e.code} on {method} {url}: {err_body}")
        try:
            return json.loads(err_body)
        except Exception:
            return {"success": False, "error": err_body}

def step1_manage_dns():
    print("--- STEP 1: Managing DNS for invest.renewablevietnam.com ---")
    dns_res = cf_api(f"/zones/{ZONE_ID}/dns_records?name={SUBDOMAIN}")
    existing = dns_res.get("result", [])
    if existing:
        record = existing[0]
        print(f"Record exists: {record['id']} - {record['type']} {record['name']} -> {record['content']} (proxied: {record['proxied']})")
        if not record.get("proxied"):
            print("Updating record to proxied=True...")
            update_data = {
                "type": record["type"],
                "name": "invest",
                "content": record["content"],
                "proxied": True,
                "ttl": 1
            }
            cf_api(f"/zones/{ZONE_ID}/dns_records/{record['id']}", method="PUT", data=update_data)
            print("Record updated to proxied.")
        return record["id"]
    else:
        print("Creating CNAME record for invest -> renewablevietnam.com (proxied=True)...")
        create_data = {
            "type": "CNAME",
            "name": "invest",
            "content": DOMAIN,
            "proxied": True,
            "ttl": 1
        }
        res = cf_api(f"/zones/{ZONE_ID}/dns_records", method="POST", data=create_data)
        if res.get("success"):
            print("Successfully created CNAME record:", res["result"]["id"])
            return res["result"]["id"]
        else:
            print("Failed to create DNS record:", res.get("errors"))
            return None

def step2_deploy_worker():
    print("\n--- STEP 2: Deploying Cloudflare Worker Script ---")
    worker_code_path = os.path.join(os.path.dirname(__file__), "..", "cloudflare", "invest_worker.js")
    with open(worker_code_path, "r", encoding="utf-8") as f:
        worker_code = f.read()

    boundary = "----CloudflareWorkerBoundaryXYZ"
    metadata = json.dumps({
        "main_module": "invest_worker.js",
        "compatibility_date": "2026-10-29"
    })

    parts = [
        f"--{boundary}\r\n".encode("utf-8"),
        b'Content-Disposition: form-data; name="metadata"\r\n',
        b'Content-Type: application/json\r\n\r\n',
        metadata.encode("utf-8"),
        b"\r\n",
        f"--{boundary}\r\n".encode("utf-8"),
        b'Content-Disposition: form-data; name="invest_worker.js"; filename="invest_worker.js"\r\n',
        b'Content-Type: application/javascript+module\r\n\r\n',
        worker_code.encode("utf-8"),
        b"\r\n",
        f"--{boundary}--\r\n".encode("utf-8")
    ]
    multipart_data = b"".join(parts)

    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}"
    }

    res = cf_api(f"/accounts/{ACCOUNT_ID}/workers/scripts/{SCRIPT_NAME}", method="PUT", data=multipart_data, headers=headers)
    if res.get("success"):
        print("Successfully deployed Worker script:", SCRIPT_NAME)
        return True
    else:
        print("Failed to deploy Worker script:", res.get("errors"))
        return False

def step3_bind_route():
    print("\n--- STEP 3: Binding Route to invest.renewablevietnam.com/* ---")
    pattern = f"{SUBDOMAIN}/*"
    routes_res = cf_api(f"/zones/{ZONE_ID}/workers/routes")
    existing_routes = routes_res.get("result", [])
    
    for r in existing_routes:
        if r.get("pattern") == pattern:
            print(f"Route {pattern} already exists bound to {r.get('script')}")
            if r.get("script") != SCRIPT_NAME:
                print(f"Updating route to {SCRIPT_NAME}...")
                cf_api(f"/zones/{ZONE_ID}/workers/routes/{r['id']}", method="PUT", data={"pattern": pattern, "script": SCRIPT_NAME})
            return r["id"]

    print(f"Creating new route {pattern} -> {SCRIPT_NAME}...")
    res = cf_api(f"/zones/{ZONE_ID}/workers/routes", method="POST", data={"pattern": pattern, "script": SCRIPT_NAME})
    if res.get("success"):
        print("Successfully created Worker route:", res["result"]["id"])
        return res["result"]["id"]
    else:
        print("Failed to create route:", res.get("errors"))
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
    if not TOKEN:
        print("Error: Pass token as argument or set CLOUDFLARE_API_TOKEN environment variable.")
        sys.exit(1)
    step1_manage_dns()
    step2_deploy_worker()
    step3_bind_route()
