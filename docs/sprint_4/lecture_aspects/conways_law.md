# Conway's law

### Definition
Conway’s law is the idea that social structures inevitably influence 
the final product design. It states that the design of a system
mirrors the communication structure of its creators. Here we will describe
how this law is reflected in our application.

### Our teams communication structure
Now we have been working on our web application
in a 9 member team for some time. Because of the current Covid-19 situation
most of our communication has taken place online through our Discord server.
We have had at least two online meetings each week outside of the retrospective meeting. 

Our team is not split up into frontend, backend and database developers.
Instead every sprint each team member has been assigned one or more user stories
to implement from scratch. So every team member works individually both in the front-
and backend of the application. This means that there are no ‘silos’ in our project
like Conway warns us about. Each team member also has a better overview of our application
and understands it better since the team is not split into groups that work in their own space.

### Conway's law in our application
Conway's law is not reflected in our application for the reasons described in the
section above. But with our team being so large and communication taking place remotely we
have had some technical debt in our project. I will describe the issues we had here
because even though they're not directly Conway's law they do relate to it.

The web application’s UI was not fully decided in advance so the team members have
had the freedom to decide for themselves where and how the element or function that
they’re implementing appears on the website. This has caused two team members to
implement similar functionalities, that should be in the same place,
in different places on our website.
It has also happened that there is a misunderstanding because the user stories
are not 100% clear and two team members have accidentally implemented the same
functionality in two different places. This happened in Sprint 3 when the functionality
to view your own created exercises was placed on the dashboard page and on the user profile page.
This has since been fixed but was clearly a waste of time and energy.
Bad communication can really create technical debt. This is not directly Conway's 
law but still an example of how communication within a team is reflected in the design
of the product they're working on. 