# Non-functional Requirements and Constraints of project

## Non-functional Requirements

*   The application works on both mobile and desktop environments
*   The application works on current versions (October 2020) of popular web browsers Chrome, Firefox and Safari
*	Website is available 99% of the time over the course of the year
*	System must maintain full traceability of transactions
*   All components should be documented
* 	After logging in, the user dashboard is displayed within 3s
* 	After registering an account, the login page is displayed within 3s
*   95% of users manage to make an account
*	On average it takes a user 5 minutes or less to register an account
*	On a scale of 1-5 on how easy it is to navigate the application 80% of asked users gave rating 4 or higher
*	On average a user can find their profile in 3 clicks or less
*   On average a user can find a view their own exercises in 2 minutes or less
*   On a scale of 1-10 how did they like the look of the application the average user rating is 7 or higher
*   95% of users manage to create a new exercise
*   95% of users are able to find and view their own created workouts



## Constraints

### No actual users

Since our application is not and will not be officially launched it will not have *real* users.
Our only users are us, the people working on the project, and maybe friends and family members asked 
to test the usability of our application.

### Paypal Connection is not official

Again since the application isn't going to be officially launched and this is a school project we don't have official 
partnership with paypal and though we simulate a paypal payment system connection we will not actually have that.

### Only one Database

Our application depends on a single database, which means there will be no system distribution.

### Component independence

Only two components in our application are independent (weather-api and logging server) 
and can be removed without issues. Rest of the system is fully linked.

### Limited Pipeline

Our pipeline time is limited and can only run a certain amount of tests over a period of time. The free plan that GitLab
 offers has a limit of 400 minutes of pipeline usage per month which translates to roughly 300 test runs.
