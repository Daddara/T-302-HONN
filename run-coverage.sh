cd workoutapp

# Setup
python manage.py migrate
coverage erase

# Run tests
coverage run manage.py test
status1=$?
coverage run --append -m unittest discover -p *_test.py
status2=$?

status1=1

if [ $status1 -eq 0 ] && [ $status2 -eq 0 ]
then
	status=0
else
	status=1
fi

# Report
coverage html --directory ../htmlcov
coverage report

echo "exit with status: " $status
exit $status