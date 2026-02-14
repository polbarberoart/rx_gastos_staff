.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m reflex init
python -m reflex export --frontend-only
Expand-Archive -Path frontend.zip -DestinationPath public
Remove-Item -Path frontend.zip -Force
deactivate