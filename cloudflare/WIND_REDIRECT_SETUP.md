# Cloudflare Configuration Guide: wind.renewablevietnam.com -> https://renewablevietnam.com/projectenergy/

## Overview
This document specifies the institutional configuration protocol for establishing an edge-level HTTP 301 Permanent Redirect from the subdomain `wind.renewablevietnam.com` (and `wind.renwablevietnam.com` if registered) to `https://renewablevietnam.com/projectenergy/`.

---

## Architecture Specification
- **Incoming Host**: `wind.renewablevietnam.com` (Subdomain)
- **Destination Target**: `https://renewablevietnam.com/projectenergy/`
- **Redirect Type**: HTTP 301 (Permanent Redirect)
- **Preserve Path / Query String**: Configurable (Preserve query string enabled; root path mapped directly to destination).
- **Execution Layer**: Cloudflare Edge Network (zero-latency redirect prior to origin fetch).

---

## Step 1: DNS Record Provisioning in Cloudflare

1. Log in to the **Cloudflare Dashboard** (`https://dash.cloudflare.com/`).
2. Select the zone: **`renewablevietnam.com`**.
3. In the left sidebar navigation, select **DNS** -> **Records**.
4. Click **Add record** and configure the parameters:
   - **Type**: `CNAME`
   - **Name**: `wind`
   - **Target**: `renewablevietnam.com` (Alternatively, an `A` record pointing to dummy IP `192.0.2.1` can be used).
   - **Proxy status**: **Proxied** (Orange Cloud icon must be enabled so traffic passes through Cloudflare Edge).
   - **TTL**: `Auto`
5. Click **Save**.

*(Note: If the typo domain `renwablevietnam.com` is also owned in Cloudflare, repeat Step 1 within that zone).*

---

## Step 2: Configure Edge Redirect Rule

Cloudflare **Redirect Rules** provide modern, high-throughput edge URL redirection replacing legacy Page Rules.

1. In the **renewablevietnam.com** zone menu, navigate to **Rules** -> **Redirect Rules**.
2. Click **Create rule**.
3. Configure the rule fields:
   - **Rule name**: `Redirect wind subdomain to projectenergy`
   - **If incoming requests match...**: Select **Custom filter expression**.
   - **Field**: `Hostname`
   - **Operator**: `equals`
   - **Value**: `wind.renewablevietnam.com`
   *(Optional expression builder: `(http.host eq "wind.renewablevietnam.com")`)*
   *(If supporting both spellings: `(http.host in {"wind.renewablevietnam.com" "wind.renwablevietnam.com"})`)*

4. Under **Then... URL redirect**:
   - **Type**: `Static`
   - **URL**: `https://renewablevietnam.com/projectenergy/`
   - **Status code**: `301` (Moved Permanently)
   - **Preserve query string**: Check / Enable (Ensures parameters like `?id=...` or tracking parameters are retained).

5. Click **Deploy**.

---

## Alternative Method: Legacy Page Rule (If Redirect Rules Quota Exhausted)

If using legacy Page Rules:
1. Navigate to **Rules** -> **Page Rules**.
2. Click **Create Page Rule**.
3. Set **URL (matching pattern)**:
   ```
   *wind.renewablevietnam.com/*
   ```
4. Pick a Setting:
   - Setting: **Forwarding URL**
   - Select status code: **301 - Permanent Redirect**
   - Enter destination URL:
     ```
     https://renewablevietnam.com/projectenergy/
     ```
5. Click **Save and Deploy Page Rule**.

---

## Step 3: Propagation Verification & Health Check

Run the following diagnostics in PowerShell to confirm DNS resolution and HTTP 301 response headers.

### A. Validate DNS Resolution
```powershell
Resolve-DnsName -Name "wind.renewablevietnam.com"
```
*Expected Output*: Should return Cloudflare proxy IP addresses.

### B. Validate HTTP Redirect Status Code & Header
```powershell
curl.exe -I "https://wind.renewablevietnam.com"
```
*Expected Response*:
```http
HTTP/2 301
location: https://renewablevietnam.com/projectenergy/
server: cloudflare
```
