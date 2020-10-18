#cd workoutapp

# Setup
echo Note: Don\'t forget to migrate your database \(workoutapp/reset_db.sh\)
coverage erase


# Run tests
status=0

# ===========================
# Logging server
# ===========================
cd logging_server
coverage run manage.py test
if [ $? -ne 0 ]
then
	status=1
fi
cd ..

# trust me this is a hack I'm not proud of
mv logging_server/.coverage workoutapp/.coverage

# ===========================
# workoutapp
# ===========================
cd workoutapp
coverage run --append manage.py test
if [ $? -ne 0 ]
then
	status=1
fi

coverage run --append -m unittest discover -p *_test.py
if [ $? -ne 0 ]
then
	status=1
fi


# Report
coverage html --directory ../htmlcov
coverage report

cd ..
echo "exit with status: " $status
exit $status