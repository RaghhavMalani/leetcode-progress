@echo off
REM ============================================================
REM  Double-click me after solving new problems on LeetCode.
REM
REM  Pulls your new solves from GitHub, generates a traced
REM  visualization for each one, and rebuilds the index and
REM  the Dojo. Everything else is left alone.
REM ============================================================
cd /d "%~dp0"
title leetcode-progress - sync

where python >nul 2>&1
if errorlevel 1 (
  echo.
  echo   Python is not on your PATH.
  echo   Install it from python.org and tick "Add Python to PATH".
  echo.
  pause
  exit /b 1
)

python sync.py %*

echo.
echo   ------------------------------------------------------------
echo    Open  visualizations\index.html   to browse the traces
echo    Open  visualizations\dojo.html    to train
echo   ------------------------------------------------------------
echo.
pause
