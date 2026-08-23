param(
    [switch]$DeterministicOnly,
    [switch]$AllowUnmeasured,
    [string]$TraceDir
)

$arguments = @("$PSScriptRoot/evaluate.py")
if ($DeterministicOnly) { $arguments += "--deterministic-only" }
if ($AllowUnmeasured) { $arguments += "--allow-unmeasured" }
if ($TraceDir) { $arguments += @("--trace-dir", $TraceDir) }
python @arguments
exit $LASTEXITCODE
