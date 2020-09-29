cd workoutapp

# Setup
python manage.py migrate
coverage erase

# Run tests
coverage run manage.py test
status1=$?
coverage run --append -m unittest discover -p *_test.py
status2=$?

status2=1

if test $status1 -eq 0 -a $status2 -eq 0
then
	status=0
else
	status=1
fi

# Report
coverage html --directory ../htmlcov
coverage report

exit $status