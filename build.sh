set -o errexit

pip install -r requirements.txt
# collect static files and write them to STATIC_ROOT
python manage.py collectstatic --no-input
# apply DB migrations if you want
python manage.py migrate