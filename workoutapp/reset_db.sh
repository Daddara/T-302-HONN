echo ============
echo Resetting DB
echo ============

rm -f local_database

python manage.py migrate

python manage.py loaddata db.json