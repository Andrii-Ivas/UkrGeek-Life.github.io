$OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Write-Host ">>> ACTIVATING NEW ARCHITECTURE (PUBLISHER)..." -ForegroundColor Cyan

# 1. KILL OLD PROCESSES
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

# 2. EXECUTE THE BRAIN (Це критичний момент - ми викликаємо publisher.py)
if (Test-Path "publisher.py") {
    python publisher.py
} else {
    Write-Error "CRITICAL: publisher.py not found!"
    exit
}

# 3. SYNC WITH GITHUB
git add .
git commit -m "UkrGeekLife | Footer & Style Update | 00:36"
git push origin master

# 4. RESTART SERVER & OPEN
Start-Process python -ArgumentList "-m http.server 8000" -WindowStyle Minimized
Start-Sleep -Seconds 2
Start-Process "http://localhost:8000/index.html"

Write-Host ">>> DONE. CHECK FOOTER NOW." -ForegroundColor Green
