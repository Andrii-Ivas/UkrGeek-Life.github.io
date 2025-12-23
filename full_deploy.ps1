$OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
# UkrGeekLife | Андрій Івась | Full Automation Deploy Script
Write-Host "--- Starting Deployment: UkrGeekLife ---" -ForegroundColor Cyan

# 1. Cleanup
Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue

# 2. Generation
python generate_page.py

# 3. Audit
python security_scan.py

# 4. Identity Sync
Get-ChildItem *.html | ForEach-Object { 
    (Get-Content $_) -replace '<title>.*</title>', '<title>UkrGeekLife | Андрій Івась</title>' | Set-Content $_ 
}

# 5. Git Cycle
git add .
git commit -m "UkrGeekLife | Андрій Івась | Automated Build $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git push origin master

Write-Host "--- Deployment Complete ---" -ForegroundColor Green