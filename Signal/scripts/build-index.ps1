# Rebuild product index.md and refresh manifest stats.
# Usage:
#   .\scripts\build-index.ps1
#   .\scripts\build-index.ps1 -Product signal-latest
#   .\scripts\build-index.ps1 -Product signal-latest -Init
#   .\scripts\build-index.ps1 -RefreshToc
#   .\scripts\build-index.ps1 -ListProducts
#   .\scripts\build-index.ps1 -Hub

param(
    [string]$Product = "signal-latest",
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
