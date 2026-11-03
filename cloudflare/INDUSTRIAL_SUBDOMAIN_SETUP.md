# Cloudflare Deployment & Routing Playbook: industrial.renewablevietnam.com

This operational guide details the edge configuration protocol for deploying `industrial.renewablevietnam.com` as the primary subdomain for Vietnam's Green Industrial Siting & DPPA Portal, while permanently redirecting legacy requests from `ind.renewablevietnam.com`.

---

## 1. Architecture Topology

- **Primary Canonical Subdomain**: `industrial.renewablevietnam.com`
- **Origin Target**: `https://renewablevietnam.com/industrial/`
- **Legacy Subdomain**: `ind.renewablevietnam.com`
- **Legacy Transition Strategy**: Edge HTTP 301 Moved Permanently redirect to `https://industrial.renewablevietnam.com${url.pathname}${url.search}`.
- **Worker Script**: `subdomain-gateway` (`cloudflare/subdomain_gateway_worker.js`)
- **Zone ID**: `eed02d9917c1a0c6144972136e836eba`
- **Account ID**: `a17978d12dc9d62ca76f7712fe8f758c`

---

## 2. Step-by-Step Cloudflare Dashboard Instructions

### Step 1: Provision DNS CNAME for industrial
1. Open the [Cloudflare Dashboard](https://dash.cloudflare.com/) and navigate to the **`renewablevietnam.com`** zone.
2. Select **DNS** -> **Records** in the sidebar.
3. Click **Add record**:
   - **Type**: `CNAME`
   - **Name**: `industrial`
   - **Target**: `renewablevietnam.com`
   - **Proxy status**: **Proxied** (Orange Cloud enabled)
   - **TTL**: `Auto`
4. Click **Save**.

### Step 2: Deploy Updated Edge Worker
1. In the sidebar, navigate to **Workers & Pages**.
2. Select the existing Worker service: **`subdomain-gateway`**.
3. Click **Edit code**.
4. Replace the worker script with the contents of [subdomain_gateway_worker.js](file:///G:/My%20Drive/7.%20AI/RenewableVietNam/cloudflare/subdomain_gateway_worker.js).
5. Click **Deploy**.

### Step 3: Bind Worker Routes
1. Navigate to **Workers Routes** in the zone menu.
2. Ensure the following routes are bound to **`subdomain-gateway`**:
   - `industrial.renewablevietnam.com/*` -> `subdomain-gateway`
   - `ind.renewablevietnam.com/*` -> `subdomain-gateway`
3. Click **Add Route** if `industrial.renewablevietnam.com/*` is not yet present.

---

## 3. Automated Deployment via Python Script

Alternatively, execute the automated provisioning script with your Cloudflare API token:

```powershell
python "G:\My Drive\7. AI\RenewableVietNam\scripts\deploy_industrial_subdomain.py" <YOUR_CLOUDFLARE_API_TOKEN>
```

The script automatically:
1. Validates and creates the proxied CNAME DNS record for `industrial`.
2. Packages and uploads `subdomain_gateway_worker.js` via Cloudflare REST API.
3. Binds the route `industrial.renewablevietnam.com/*` to the worker.
