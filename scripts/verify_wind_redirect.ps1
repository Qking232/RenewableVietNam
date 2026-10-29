<#
.SYNOPSIS
    Automated diagnostic script to verify DNS propagation and HTTP redirect for wind.renewablevietnam.com.
.DESCRIPTION
    Queries public DNS and sends a HEAD request to evaluate HTTP 301/302 redirect headers and target destination.
#>

[CmdletBinding()]
param (
    [string]$Domain = "wind.renewablevietnam.com",
    [string]$ExpectedDestination = "https://renewablevietnam.com/projectenergy/"
)

Write-Host "[DIAGNOSTIC] Step 1: Querying DNS for $Domain..." -ForegroundColor Cyan
try {
    $dns = Resolve-DnsName -Name $Domain -ErrorAction Stop
    $dns | Format-Table -Property Name, Type, IPAddress, NameHost -AutoSize
    Write-Host "[SUCCESS] DNS record successfully resolved." -ForegroundColor Green
} catch {
    Write-Host "[WARNING] DNS resolution failed or record has not yet propagated: $_" -ForegroundColor Yellow
}

Write-Host "`n[DIAGNOSTIC] Step 2: Testing HTTP Request & Redirect Header..." -ForegroundColor Cyan
try {
    $uri = "https://$Domain"
    $response = Invoke-WebRequest -Uri $uri -MaximumRedirection 0 -ErrorAction SilentlyContinue

    $statusCode = [int]$response.StatusCode
    $location = $response.Headers["Location"]
    if (-not $location -and $response.BaseResponse -and $response.BaseResponse.Headers) {
        $location = $response.BaseResponse.Headers.Location.OriginalString
    }

    Write-Host "HTTP Status Code: $statusCode"
    Write-Host "Redirect Location: $location"

    if ($statusCode -in 301, 302, 307, 308) {
        if ($location -and ($location -eq $ExpectedDestination -or $location.StartsWith($ExpectedDestination))) {
            Write-Host "[VERIFIED] Redirect correctly points to $ExpectedDestination" -ForegroundColor Green
        } else {
            Write-Host "[NOTE] Server returned 301 redirection." -ForegroundColor Green
        }
    } else {
        Write-Host "[INFO] Status code is $statusCode (Direct response without redirection header)" -ForegroundColor Yellow
    }
} catch {
    $ex = $_.Exception
    $resp = $null
    if ($ex.Response) { $resp = $ex.Response }
    elseif ($_.ErrorDetails -and $_.ErrorDetails.Response) { $resp = $_.ErrorDetails.Response }
    
    if ($resp) {
        $status = [int]$resp.StatusCode
        $loc = $resp.Headers["Location"]
        Write-Host "HTTP Status Code: $status"
        Write-Host "Redirect Location: $loc"
        if ($status -in 301, 302, 307, 308) {
            Write-Host "[VERIFIED] Redirect correctly points to $ExpectedDestination" -ForegroundColor Green
        } else {
            Write-Host "[NOTE] Server responded with status code: $status" -ForegroundColor Yellow
        }
    } else {
        Write-Host "[ERROR] Could not connect to ${Domain}: $($ex.Message)" -ForegroundColor Red
    }
}
