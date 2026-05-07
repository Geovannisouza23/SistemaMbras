@echo off
setlocal

REM Execucao no Windows sem IDE (cmd)

if not exist ".venv\Scripts\python.exe" (
    echo Ambiente virtual nao encontrado. Rodando setup...
    call setup_windows.bat
    if %ERRORLEVEL% NEQ 0 (
        echo [ERRO] Nao foi possivel concluir o setup.
        pause
        exit /b 1
    )
)

if not exist "dados_extraidos.xlsx" (
    echo [ERRO] Arquivo de entrada "dados_extraidos.xlsx" nao encontrado nesta pasta.
    echo Coloque o arquivo na mesma pasta do script e tente novamente.
    pause
    exit /b 1
)

echo Iniciando automacao...
call .venv\Scripts\python.exe "iptu - Copia.py"
set "EXIT_CODE=%ERRORLEVEL%"

echo.
if %EXIT_CODE% EQU 0 (
    echo Processo finalizado.
    echo Saida esperada: dados_extraidos_IPTU.xlsx
) else (
    echo Processo finalizado com erro. Codigo: %EXIT_CODE%
)

echo.
pause
endlocal
exit /b %EXIT_CODE%
