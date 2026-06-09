# =====================================================================
# deploy-preview.ps1 — push the CURRENT working files of the production
# repo (ontalent-main) to the staging repo (ontalent-preview), which
# serves https://preview.ontalent.org.
#
# Staging always gets: CNAME=preview.ontalent.org, noindex on every page,
# and robots.txt "Disallow: /" so Google never indexes it.
#
# Usage (from anywhere):
#   pwsh ./scratch/deploy-preview.ps1            # stage whatever is checked out
#   pwsh ./scratch/deploy-preview.ps1 -NoPush    # build locally, don't push
#
# Typical flow: check out a feature branch in ontalent-main, run this to
# preview it at preview.ontalent.org, then merge to main for production.
# =====================================================================
param([switch]$NoPush)

$src = Split-Path $PSScriptRoot -Parent                       # ontalent-main working dir
$dst = Join-Path (Split-Path $src -Parent) 'ontalent-preview' # sibling staging repo

if (-not (Test-Path (Join-Path $dst '.git'))) {
  Write-Error "Staging repo not found at $dst (expected a clone of ontalent-preview)."; exit 1
}

# 1) Mirror production files into staging (drop files removed in prod), excluding repo/infra-only items.
robocopy $src $dst /MIR /XD ".git" "scratch" /XF "build.py" "sitemap.xml" "*.zip" "deploy-preview.ps1" /NFL /NDL /NJH /NJS /NP | Out-Null

# 2) Re-apply staging-only overrides.
[System.IO.File]::WriteAllText((Join-Path $dst 'CNAME'), "preview.ontalent.org`n")
[System.IO.File]::WriteAllText((Join-Path $dst 'robots.txt'), "User-agent: *`nDisallow: /`n")
Get-ChildItem $dst -Filter *.html | ForEach-Object {
  $c = [System.IO.File]::ReadAllText($_.FullName)
  if ($c -notmatch 'name="robots"') {
    $c = [regex]::Replace($c, '(<meta name="theme-color"[^>]*>)', ('$1' + "`r`n  <meta name=""robots"" content=""noindex, nofollow"">"), 1)
    [System.IO.File]::WriteAllText($_.FullName, $c)
  }
}

# 3) Commit + push staging.
Push-Location $dst
git add -A
$branch = (& git -C $src rev-parse --abbrev-ref HEAD)
$stamp  = Get-Date -Format 'yyyy-MM-dd HH:mm'
git commit -m "Stage $branch @ $stamp" | Out-Null
if (-not $NoPush) { git push origin main }
Pop-Location
Write-Host "Staged to preview.ontalent.org (source branch: $branch). Allow ~30s for GitHub Pages to rebuild."
