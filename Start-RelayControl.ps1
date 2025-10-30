# --------------------------------------------------------------
# Start-RelayControl.ps1
# One-click launcher – installs Python deps if missing and runs the bridge
# --------------------------------------------------------------

# 1. Check Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python is not installed or not in PATH."
    exit 1
}

# 2. Create a virtual environment (if not already there)
$venv = "$PSScriptRoot\.venv"
if (-not (Test-Path $venv)) {
    Write-Host "Creating virtual environment..."
    python -m venv $venv
}

# 3. Activate venv
$activate = "$venv\Scripts\Activate.ps1"
if (Test-Path $activate) { . $activate }

# 4. Install required packages (websockets, asyncio)
$reqs = "$PSScriptRoot\requirements.txt"
if (-not (Test-Path $reqs)) {
    @"
websockets
"@ | Out-File -Encoding utf8 $reqs
}
python -m pip install --upgrade pip | Out-Null
python -m pip install -r $reqs | Out-Null

# 5. Launch the Python bridge
Write-Host "`nStarting WebSocket → TCP bridge (localhost:8765) ..."
python "$PSScriptRoot\bridge.py"

# (script ends – bridge stays alive until you press Ctrl-C)