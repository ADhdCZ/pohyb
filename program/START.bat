@echo off
for /f "tokens=2 delims==" %%i in ('findstr /i "folder_path" config.ini') do set folder_path=%%i
for /f "tokens=2 delims==" %%j in ('findstr /i "version_file" config.ini') do set version_file=%%j

REM odebrani uvozovek
set folder_path=%folder_path:"=%
set version_file=%version_file:"=%

REM Sestavení úplné cesty k souboru
set full_path=%folder_path%\%version_file%

echo Folder path: %folder_path%
echo Version file: %version_file%
echo Full path: %full_path%

cmd /k python "%full_path%"
