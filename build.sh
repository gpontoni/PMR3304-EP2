set -o errexit
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
# Cria o conteúdo do site e a conta "tecna"
python manage.py popular_banco