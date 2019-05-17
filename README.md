# Create virtual environment
python -m venv .env

# Extract packages
pip freeze > requirements.txt

# Install packages
pip install -r requirements.txt