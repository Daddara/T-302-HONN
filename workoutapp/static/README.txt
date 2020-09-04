When adding static files, add them to dir path:
appname/file type/view_description

ex path:
static/workout/css/workout_creation.css
static/workout/js/workout_creation.js


Use static files in templates like this:

{% extends 'base.html' %}
{% load static %}
{% block extra_head %}
    <link rel="stylesheet" type="text/css" href="{% static 'workout/css/workout_creation.css' %}">
{% endblock %}
{% block content %}
  PAGE SPECIFIC CONTENT HERE
{% endblock %}
{% block extra_js %}
    <script src="{% static 'listings/js/my_listings.js' %}"></script>
{% endblock %}



BASE HTML TEMPLATE MUST CONTAIN FOLLOWING:
{% load static %}

    <!-- For extra css for specific pages -->
    {% block extra_head %}

    {% endblock %}

    <!-- For extra js for specific pages -->
    {% block extra_js %}

    {% endblock %}
