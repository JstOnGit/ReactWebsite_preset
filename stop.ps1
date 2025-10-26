# Stop Python backend processes
Get-Process -Name "python" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*main.py*" } | Stop-Process -Force

# Stop Node.js frontend processes
Get-Process -Name "node" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*vite*" -or $_.CommandLine -like "*dev*" } | Stop-Process -Force

# Stop any cmd processes running npm
Get-Process -Name "cmd" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*npm*" } | Stop-Process -Force

# Stop PowerShell jobs that might be running the frontend
Get-Job | Stop-Job -PassThru | Remove-Job

# Stop any remaining PowerShell processes running the run script
Get-Process -Name "powershell" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*run.ps1*" } | Stop-Process -Force

# Force stop any processes that might still be holding the database
Get-Process -Name "python" -ErrorAction SilentlyContinue | Stop-Process -Force