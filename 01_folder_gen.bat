@echo off

:: Get today's date in YYYY-MM-DD format
for /f "tokens=1-3 delims=/.- " %%a in ('echo %date%') do (
    set year=%%c
    set month=%%a
    set day=%%b
)
set today=%year%-%month%-%day%

:: Replace any double dashes with single dashes
set today=%today:--=-%

:: Prompt user for description
set /p desc=Enter folder description: 

:: Replace spaces in description with underscores
set desc=%desc: =_%

:: Combine date and description for folder name
set foldername=%today%%desc%

:: Check if folder exists
if exist %foldername% (
    echo Folder '%foldername%' already exists.
) else (
    :: Create folder
    mkdir %foldername%
    echo Folder '%foldername%' created successfully.

    :: Add description file
    echo %desc% > %foldername%\description.txt
    echo Description added to the folder.
)

pause
