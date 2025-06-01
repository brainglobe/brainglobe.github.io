@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

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
        rmdir /S /Q %BUILDDIR%
    )
    if exist %SOURCEDIR%\api (
        rmdir /S /Q %SOURCEDIR%\api
    )
    for /R %SOURCEDIR%\documentation %%f in (api-reference.md) do (
        if exist "%%f" del "%%f" 
    )
    echo Removing API Reference toctree sections...
    python remove_api_toctrees.py
) else if "%1" == "help" (
    goto help
) else (
	REM Build the documentation
    echo Generating API index...
    python make_api_index.py
    timeout /t 3 > NUL

    echo Generating API toctrees...
	python generate_api_toctrees.py
    timeout /t 3 > NUL

    %SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
)

shift
if not "%1" == "" goto process_targets
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
