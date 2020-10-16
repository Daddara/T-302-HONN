echo ============
echo Resetting DB
echo ============

reset_db() {
    cd $1
    echo "--------------"
    echo "Cleaning: " $1
    rm -f local_database
    python manage.py migrate
    python manage.py loaddata db.json
    cd ..
}

reset_db logging_server
reset_db workoutapp