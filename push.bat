@echo off
setlocal enabledelayedexpansion
title Push Ankan-Grade to GitHub (kishore-0907)
cd /d "C:\Users\Shivany\.gemini\antigravity\scratch\nyaya-evaluator"

echo ===================================================================
echo   Nyaya / Ankan-Grade — One-Click GitHub Push Tool
echo   Target Repository : https://github.com/kishore-0907/Ankan-Grade
echo   Target Username   : kishore-0907
echo   Branch            : main
echo ===================================================================
echo.
echo Choose authentication method:
echo   [1] Browser Login (Sign in as kishore-0907 via web browser popup)
echo   [2] Personal Access Token (Paste your GitHub PAT)
echo.
set /p CHOICE="Enter choice (1 or 2) [default is 1]: "
if "%CHOICE%"=="" set CHOICE=1

if "%CHOICE%"=="2" goto USE_TOKEN
goto USE_BROWSER

:USE_BROWSER
echo.
echo [INFO] Launching Git push. If prompted, please authorize in your browser as kishore-0907...
git -c credential.https://github.com.username=kishore-0907 push -u origin main
goto FINISH

:USE_TOKEN
echo.
set /p TOKEN="Enter your GitHub Personal Access Token (ghp_...): "
if "%TOKEN%"=="" (
    echo [ERROR] Token cannot be empty.
    goto FINISH
)
echo.
echo [INFO] Pushing with Personal Access Token...
git push https://kishore-0907:%TOKEN%@github.com/kishore-0907/Ankan-Grade.git main

:FINISH
echo.
echo ===================================================================
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Pushed successfully to https://github.com/kishore-0907/Ankan-Grade!
) else (
    echo [NOTE] If push was denied, ensure you are signed in as kishore-0907
    echo        or that your Personal Access Token has 'repo' write permissions.
)
echo ===================================================================
echo.
pause
