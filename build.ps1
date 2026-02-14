.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m reflex init
# Así se pasan variables de entorno en PowerShell antes de un comando:
$env:API_URL="https://rxgastosstaff-production.up.railway.app/"; python -m reflex export --frontend-only
Expand-Archive -Path frontend.zip -DestinationPath public -Force
Remove-Item -Path frontend.zip -Force
deactivate