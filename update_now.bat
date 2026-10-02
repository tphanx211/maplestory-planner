@echo off
rem On-demand check for MapleStory Classic World news, then opens the dashboard.
rem Runs the same rules as the scheduled updater (updater\UPDATER_RULES.md) through the claude CLI.
rem dontAsk mode: only what .claude\settings.json allows can run; nothing prompts.
setlocal
cd /d "%~dp0"
echo Checking for MapleStory Classic World plan updates. This usually takes 1-3 minutes...
echo.
type "updater\run_prompt.md" | claude -p --permission-mode dontAsk
if errorlevel 1 (
  echo.
  echo The update check reported a problem. See the messages above.
)
if not "%MSCW_NO_OPEN%"=="1" start "" "%~dp0index.html"
endlocal
