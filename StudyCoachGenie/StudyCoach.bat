@echo off
title Study Coach Genie Basslatiliyor...
echo.
echo ===========================================
echo   Study Coach Genie - Egitim Kocunuz
echo ===========================================
echo.
echo Uygulama baslatiliyor, lutfen bekleyin...

:: Python sunucusunu arka planda başlat
start /B python app.py

:: Sunucunun ayağa kalkması için 3 saniye bekle
timeout /t 3 >nul

:: Tarayıcıyı aç
start http://127.0.0.1:5000

echo.
echo Uygulama tarayicinizda acildi!
echo Kapatmak icin bu pencereyi kapatabilirsiniz.
pause
