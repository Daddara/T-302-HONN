cd workoutapp

# Setup
echo Note: Don\'t forget to migrate your database \(workoutapp/reset_db.sh\)
coverage erase

# Run tests
coverage run manage.py test
status1=$?
coverage run --append -m unittest discover -p *_test.py
status2=$?

if [ $status1 -eq 0 ] && [ $status2 -eq 0 ]
then
	status=0
else
	status=1
fi

# Report
coverage html --directory ../htmlcov
coverage report

cd ..
echo "exit with status: " $status
exit $status