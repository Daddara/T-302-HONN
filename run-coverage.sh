cd workoutapp

# Setup
python manage.py migrate
coverage erase

# Run tests
coverage run manage.py test
coverage run --append -m unittest discover -p *_test.py

# Report
coverage html --directory ../htmlcov
coverage report