@echo off
title Boby IA 🐶

echo ============================
echo      Iniciando Boby IA
echo ============================

cd /d %~dp0


echo Activando entorno virtual...

call .venv\Scripts\activate


echo Verificando dependencias...

pip install -r requirements.txt > nul


echo.
echo 🐶 Boby IA listo
echo.


python boby_chat.py


pause