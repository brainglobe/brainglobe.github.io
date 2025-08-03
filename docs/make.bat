@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

set TIMEOUT=2

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

:process_targets
if "%1" == "clean" (
    echo Removing auto-generated files...
    if exist %BUILDDIR% (
        echo Removing %BUILDDIR% directory...
        rmdir /S /Q %BUILDDIR%
        timeout /t %TIMEOUT% > NUL
    )
    echo Removing API Reference toctree sections...
    python remove_api_toctrees.py
    timeout /t %TIMEOUT% > NUL
    if exist %SOURCEDIR%\api (
        echo Removing %SOURCEDIR%\api directory...
        rmdir /S /Q %SOURCEDIR%\api
        timeout /t %TIMEOUT% > NUL
    )
    if exist downloads (
        echo Removing downloads directory...
        rmdir /S /Q downloads
        timeout /t %TIMEOUT% > NUL
    )
) else if "%1" == "help" (
    goto help
) else (
	REM Build the documentation
    echo Fetching repositories...
    python fetch_repos.py
    timeout /t %TIMEOUT% > NUL

    echo Generating API index...
    python make_api_index.py
    timeout /t %TIMEOUT% > NUL

    echo Generating API toctrees...
	python generate_api_toctrees.py
    timeout /t %TIMEOUT% > NUL

    %SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
)

shift
if not "%1" == "" goto process_targets
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
