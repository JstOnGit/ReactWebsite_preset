# Install frontend dependencies if needed
if (!(Test-Path "$PSScriptRoot\frontend\node_modules")) {
    Set-Location "$PSScriptRoot\frontend"
    npm install
    Set-Location "$PSScriptRoot"
}

# Start backend
Start-Process -NoNewWindow -WorkingDirectory "$PSScriptRoot" -FilePath "python" -ArgumentList "backend\main.py"

# Start frontend
Start-Sleep -Seconds 5
Set-Location "$PSScriptRoot\frontend"
Start-Process -NoNewWindow -FilePath "cmd" -ArgumentList "/c", "npm run dev -- --host localhost --port 6942"
Set-Location "$PSScriptRoot"

while ($true) {
    Start-Sleep -Seconds 10
}