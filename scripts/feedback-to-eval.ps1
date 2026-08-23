param(
    [Parameter(Mandatory=$true)][string]$Feedback,
    [string]$FeedbackId,
    [switch]$DryRun
)

$arguments = @("$PSScriptRoot/feedback-to-eval.py", $Feedback)
if ($FeedbackId) { $arguments += @("--feedback-id", $FeedbackId) }
if ($DryRun) { $arguments += "--dry-run" }
python @arguments
exit $LASTEXITCODE

