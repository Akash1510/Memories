@REM This is Use for the Excution of all .py files

@REM @echo off
@REM call .venv\Scripts\activate
@REM for %%f in (*.py) do python "%%f"

@REM This is For app.py execution

@echo off
call .venv\Scripts\activate
flask --app main run
pause