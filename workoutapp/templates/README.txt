ALL HTML FILES GO HERE

Example path to html templates:

templates/user/login.html
templates/user/logout.html
templates/user/create_account.html

templates/workout/create_workout.html
templates/workout/view_workout.html
templates/workout/single_workout.html


Example usage in views:
return render(request, 'workout/view_workout.html', context={'workouts': workouts})


Example usage in HTML:
{% if workouts %}
    {% for workout in workouts %}
        {% include 'workout/single_workout.html' with workout=workout %}
        <--! reference attributes of workout with workout.attribute -->
    {% endfor %}
{% else %}....
