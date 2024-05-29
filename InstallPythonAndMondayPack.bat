@echo off

REM Download the latest Python installer (e.g., python-3.12.3-amd64.exe)
echo Downloading Python installer...
curl -o python-installer.exe https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

REM Install Python silently
echo Installing Python...
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

REM Wait for the installation to complete
timeout /t 20

REM Verify Python installation
python --version
if %ERRORLEVEL% neq 0 (
    echo Python installation failed.
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install the specific version of monday
echo Installing monday==2.0.0.rc3...
pip install monday==2.0.0.rc3

REM Verify installation
pip show monday
if %ERRORLEVEL% neq 0 (
    echo Installation of monday failed.
    exit /b 1
)

echo Installation completed successfully.
exit /b 0
