@echo off
echo Creating Flask Demo App Structure...

:: Root files
type nul > config.py
type nul > run.py
type nul > requirements.txt
type nul > .gitignore
type nul > README.md

:: App folder
mkdir app
cd app

type nul > __init__.py
type nul > routes.py
type nul > models.py
type nul > forms.py

:: Templates
mkdir templates
cd templates

type nul > base.html
type nul > index.html
type nul > about.html
type nul > contact.html
type nul > data.html

cd ..

cd ..

:: Static folder
mkdir static
cd static

mkdir css
mkdir js

type nul > css\style.css
type nul > js\main.js

cd ..

echo.
echo Flask Demo App structure created successfully.
pause