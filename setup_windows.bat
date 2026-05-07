@echo off
setlocal

REM Setup automatico para Windows (cmd)
REM Requisitos: Python 3 instalado e Chrome instalado

set "PY_LAUNCHER="
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PY_LAUNCHER=py -3"
) else (
    where python >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        set "PY_LAUNCHER=python"
    ) else (
        echo [ERRO] Python 3 nao encontrado no PATH.
        echo Instale o Python e marque a opcao "Add python.exe to PATH".
        pause
        exit /b 1
    )
)

if not exist ".venv\Scripts\python.exe" (
    echo Criando ambiente virtual em .venv...
    call %PY_LAUNCHER% -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo [ERRO] Falha ao criar .venv.
        pause
        exit /b 1
    )
)

echo Atualizando pip...
call .venv\Scripts\python.exe -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] Falha ao atualizar pip.
    pause
    exit /b 1
)

echo Instalando dependencias...
call .venv\Scripts\python.exe -m pip install selenium openpyxl
if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] Falha ao instalar dependencias.
    pause
    exit /b 1
)

echo.
echo Setup concluido com sucesso.
echo.
pause
endlocal
