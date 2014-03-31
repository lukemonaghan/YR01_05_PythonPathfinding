@echo off
echo Framework cleaner by Luke Monaghan
for /r %%f in (*.sln) do set CurrDirName=%%~nf
echo %CurrDirName%
pause
del "*.sdf"
RD /S /Q ".\ipch"
RD /S /Q ".\debug"
RD /S /Q ".\release"
RD /S /Q ".\%CurrDirName%\Debug"
RD /S /Q ".\%CurrDirName%\Release"
RD /S /Q ".\%CurrDirName%\obj"
RD /S /Q ".\%CurrDirName%\bin"
echo close this window now if you do not want to zip (using 7zip)
pause
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ("%TIME%") do (set mytime=%%a%%b)
"C:\Program Files\7-Zip\7z.exe" a ..\%CurrDirName%_%mydate%_%mytime%.zip
pause