@echo off
title DarkHats Compiler
color 0A

echo ====================================================
echo             DarkHats - Executable Builder
echo ====================================================
echo.

py --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao foi encontrado no sistema.
    echo Por favor, instale o Python 3.13 e marque a opcao "Add Python to PATH".
    pause
    exit /b
)

echo [OK] Python detectado!
echo Iniciando script de compilacao...
echo.

py build_exe.py

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Ocorreu um erro durante a execucao do script de compilacao.
    pause
    exit /b
)

echo.
echo Pressione qualquer tecla para sair...
pause >nul
