@echo off
chcp 65001 >nul
echo Dang mo Chrome de ban dang nhap...
start "" chrome.exe --user-data-dir="%~dp0vlearn_browser_profile" https://vlearn.dev/dashboard
echo.
echo Khi dang nhap xong va tich nho tai khoan, hay dong Chrome lai.
echo Sau do ban chi can nhan vao file nay hoac bao voi AI de chay tool!
pause
