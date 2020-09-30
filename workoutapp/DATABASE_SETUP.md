# Database

## Migrate
`$ python migrate.py migrate`

## Populate the database
1. **Delete Data**(optional): delete all data in the database via: `$ python manage.py flush` (Confirm with `$ yes`)
2. **Populate**: `$ python manage.py loaddata db.json`

## Delete database schema
This should only be done when you want to reset your entire database including the schema:
1. **Delete the file**: `$ rm local_database`
2. **Migrate**: `$ python manage.py migrate`
3. **Populate**: `$ python manage.py loaddata db.json`

## Dump the current database into a file
`python manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude sessions --indent 2 > db.json`

The system user has the following credentials:
* **Username**: `System`
* **Password**: `adminadmin`