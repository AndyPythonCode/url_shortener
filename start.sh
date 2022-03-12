# Preparacion del Backend
poetry export -f requirements.txt --output requirements.txt --without-hashes

python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt

python -m pip install --upgrade pip

uvicorn main:app --reload --host=0.0.0.0