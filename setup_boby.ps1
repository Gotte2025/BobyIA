Write-Host "🐶 Instalando Boby IA..."

Write-Host "📦 Creando entorno virtual..."
python -m venv .venv

Write-Host "⚙️ Activando entorno..."
.\.venv\Scripts\Activate.ps1

Write-Host "📚 Instalando dependencias..."
pip install -r requirements.txt

Write-Host ""
Write-Host "✅ Boby IA instalado"
Write-Host ""
Write-Host "Ahora:"
Write-Host "1) Copia config.example.env como .env"
Write-Host "2) Completa tus claves"
Write-Host "3) Ejecuta: python boby_chat.py"