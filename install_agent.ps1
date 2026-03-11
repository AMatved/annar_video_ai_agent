# Installation script for Video Creator Agent command
# Run: .\install_agent.ps1

$projectPath = "C:\Users\User\video_creator_agent"
$functionDefinition = @"

function agent {
    param([Parameter(ValueFromRemainingArguments=`$true)]`$args)
    `$command = `$args -join " "
    if ([string]::IsNullOrEmpty(`$command)) {
        python "$projectPath\agent.py"
    } else {
        python "$projectPath\agent.py" `$command
    }
}

"@

# Create profile directory if not exists
$profileDir = Split-Path $PROFILE -Parent
if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

# Add function to profile
if (Test-Path $PROFILE) {
    $profileContent = Get-Content $PROFILE -Raw
    if ($profileContent -notmatch 'function agent') {
        Add-Content -Path $PROFILE -Value $functionDefinition
        Write-Host "✅ Agent function added to your PowerShell profile" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Agent function already exists in profile" -ForegroundColor Yellow
    }
} else {
    Set-Content -Path $PROFILE -Value $functionDefinition
    Write-Host "✅ PowerShell profile created with Agent function" -ForegroundColor Green
}

Write-Host ""
Write-Host "🎉 Installation complete!" -ForegroundColor Cyan
Write-Host "Restart PowerShell and use: agent `"your command here`"" -ForegroundColor White
Write-Host ""
Write-Host "Example commands:" -ForegroundColor Cyan
Write-Host '  agent "Save idea: morning routine TikTok"' -ForegroundColor White
Write-Host '  agent "Generate 5 viral titles for fitness"' -ForegroundColor White
Write-Host '  agent "Show my stats"' -ForegroundColor White
