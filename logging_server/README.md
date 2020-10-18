# Logging Server V1.1
This web service package is intended for logging data. It utilizes a django server setup to receive post data via a web
address. The current version supports front end logging integration into HTML templates.

## Front end logger
The front end logger logs button presses and the meta data associated with the action performed on it. The following
is an example of data stored by the server after a button click that has been associated with the front end module.
![image](logging_server/log_example.PNG)

#### Default integration
To integrate the frontend logger you must add the attribute `lid` to an html element, assign it a value and add the 
javascript [logging.js](logging_server/logging.js) to your template.

#### Stored data
1. **event_time**\
The time of the buttonpress in python datetime format\
_Type_: `python datetime + tzinfo`
2. **event_type**\
String that represents the event type. There are currently 3 available for use which can be seen in the 
'Supported event types' section.\
_Type_: `str`
3. **user_id**\
Logs the user's id.\
_Type_: `int`
4. **current_url**\
Logs the destination url of the current event.\
_Type_: `str`, _max_: `256 char`
5. **event_meta**\
Logs the meta data of the requested event.\
_Type_: `str`, _max_: `1024 char`
6. **session_meta**
Contains information on the current user session\
Optional: _Type_: `str`, _max_: `1024 char`

#### Custom integrations
To do custom integrations you must send the attributes in the aforementioned section
to the server as a form. The session_meta attribute is optional.\
Destination address for post request: `127.0.0.1:8001/event/frontend`

#### Supported event types
- 'OTHER'
- 'BUTTON_PRESS'
- 'JS_ERROR'

