# Rebuild product index.md and refresh manifest stats.
# Usage:
#   .\scripts\build-index.ps1
#   .\scripts\build-index.ps1 -Product detect-11.5.1
#   .\scripts\build-index.ps1 -Product detect-11.5.1 -Init
#   .\scripts\build-index.ps1 -Product all -Init
#   .\scripts\build-index.ps1 -RefreshToc
#   .\scripts\build-index.ps1 -ListProducts

param(
    [string]$Product = "blackduck-2026.7",
    [switch]$Init,
    [switch]$RefreshToc,
    [switch]$Hub,
    [switch]$ListProducts
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$argsList = @()
if ($ListProducts) {
    $argsList += "--list-products"
} else {
    $argsList += "--product"
    $argsList += $Product
    if ($Init) { $argsList += "--init" }
    if ($RefreshToc) { $argsList += "--refresh-toc" }
    if ($Hub) { $argsList += "--hub" }
}

python (Join-Path $PSScriptRoot "build-index.py") @argsList
exit $LASTEXITCODE
