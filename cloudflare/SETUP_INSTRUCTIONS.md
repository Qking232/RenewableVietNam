# Cloudflare Setup Guide: invest.renewablevietnam.com Subdomain

This guide details the procedures required to activate `invest.renewablevietnam.com` routing to `renewablevietnam.com/invm` using Cloudflare.

---

## Method 1: Cloudflare Dashboard (Manual Configuration)

### Step 1: Add DNS Record
1. Navigate to the Cloudflare Dashboard and select the domain **`renewablevietnam.com`**.
2. In the left navigation menu, go to **DNS** -> **Records**.
3. Click **Add Record** and configure:
   * **Type**: `CNAME` (or `A`)
   * **Name**: `invest`
   * **Target**: `renewablevietnam.com` (if `A` record is selected, use placeholder IP `192.0.2.1`)
   * **Proxy status**: **Proxied** (Orange Cloud icon must be enabled)
   * **TTL**: Auto
4. Click **Save**.

### Step 2: Deploy Cloudflare Worker
1. In the left navigation menu, go to **Workers & Pages**.
2. Click **Create Application** -> **Create Worker**.
3. Set the worker name to: `invest-subdomain-proxy`.
4. Click **Deploy**.
5. Once deployed, click **Edit code**.
6. Replace the existing template with the code from `invest_worker.js`:
   * Location: `RenewableVietNam/cloudflare/invest_worker.js`
7. Click **Deploy** to save changes.

### Step 3: Bind Worker Route to Domain
1. Return to the **renewablevietnam.com** Zone overview.
2. In the left menu, select **Workers Routes** (under **Compute (Workers)** or **Workers & Pages** -> **Routes**).
3. Click **Add Route**.
4. Configure:
   * **Route**: `invest.renewablevietnam.com/*`
   * **Service**: `invest-subdomain-proxy`
   * **Environment**: `production`
5. Click **Save**.

---

## Method 2: Automated Deployment via Wrangler CLI

If you have Node.js and Wrangler installed with Cloudflare credentials:

1. Open PowerShell and navigate to the cloudflare folder:
   ```powershell
   cd "G:\My Drive\7. AI\RenewableVietNam\cloudflare"
   ```
2. Authenticate with Cloudflare (if not already logged in):
   ```powershell
   npx wrangler login
   ```
3. Deploy the worker and its route binding:
   ```powershell
   npx wrangler deploy
   ```
4. Verify the DNS record `invest` is present as a proxied record in the Cloudflare dashboard.

---

## Verification & Health Check

After completing either method:
1. Validate DNS propagation:
   ```powershell
   Resolve-DnsName -Name "invest.renewablevietnam.com"
   ```
2. Open `https://invest.renewablevietnam.com/` in your browser. It should serve the Vietnam Investment Project Legal Management & M&A Engine.
3. Open `https://invest.renewablevietnam.com/quyhoach/` to confirm sub-path routing.
