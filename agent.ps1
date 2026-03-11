# Agent wrapper for PowerShell
# Usage: .\agent.ps1 "your command here"

$command = $args -join " "
if ([string]::IsNullOrEmpty($command)) {
    python agent.py
} else {
    python agent.py $command
}
