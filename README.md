# 1. The aim of the project

The aim of the project is to create a system to register your mood throughout the day. Registering a mood is done by choosing a calendar day and filling it with data by choosing the appropriate emoji icons. The system also provides functionality to leave a textual note about your mood so the system can be used as a personal journal.

The system in addition provides functionality to see statistics about the user's mood:

* Total day count grouped by mood data;
* Total day count grouped by weather data;
* Total day count grouped by health data;
* Total day count grouped by activity data.

# 2. Description of the system

The system consists of several functional blocks:

1. Registration, authentification, and authorization;
2. Personal page;
3. Functionality for the user to register mood including calendar, history data, and statistics about the day;
4. Analytics (statistics) module.

## 2.1. Types of users

The system provides one user type - a person who wants to register his mood. The administration is done by using the Python Django admin functionality.

## 2.2. Registration

A user can be registered through the form. The form consists of several fields:

* username - mandatory field;
* email - mandatory field;
* first name - mandatory field;
* last name - mandatory field;
* profile picture - optional field;
* phone - optional field.

In the first iteration of the project, user registration is not implemented as a separate functionality. It is done using the Python Django admin functionality.

Example:
!["Registration form"](../main/images/registration.PNG)

## 2.3. Authentification

A user can be authenticated through the form. The form consists of two fields:

* Username
* Password

Example:
!["Auth form"](../main/images/login.PNG)

## 2.4. Functionality

### 2.4.1. Dashboard

After successful login user can see his dashboard. On the dashboard is information about the user and a calendar with mood statistics. Each recorded mood entry is displayed as a new additional visual point next to the date in the calendar. When user clicks on a calendar day, the total mood statistics for the day are displayed if data have previously been recorded for that day. In addition, it is possible to register a new mood record for selected day.

Example:
!["Statistics form"](../main/images/stats.PNG)

### 2.4.2. Mood registration

The user can register mood via a particular form. The form has the following fields:

* Date and time - fills automatically;
* Mood (Excited, Happy, Neutral, Bored, Sad, Angry) - required field;
* Current weather (Sunny, Rainy, Cloudy, Snowy, Windy) - required field;
* Current health (Healthy, Sick) - required field;
* Activities today (Workday, Relaxation day) - required field;
* Note - a textual note about the mood - optional field.

Example:
!["Mood form"](../main/images/register_mood.PNG)

### 2.4.3. Statistics

The statistics section displays the overall user statistics using charts:

* Total day count grouped by mood data;
* Total day count grouped by weather data;
* Total day count grouped by health data;
* Total day count grouped by activity data.

Example:
!["Charts form"](../main/images/charts.PNG)

### 2.4.4. Profile page

The text "Hi, Name+Last name" is displayed in the header of the page. Clicking on "Name+Last name" opens the profile page, where the following data is visible:

* Username;
* Email;
* First name;
* Last name;
* Phone;
* Profile picture.

By pressing the "Edit profile fields" button, a form is displayed where it is possible to modify these data. It is not possible to modify the username field.

Example:
!["Profile form"](../main/images/profile.PNG)

# 3. Technology stack

* Backend:
  * Python (https://www.python.org/)
  * Django (https://www.djangoproject.com/)
  * Django Rest Framework (https://www.django-rest-framework.org/)
  * axios (https://axios-http.com/)
* Frontend:
  * Vue.js (https://vuejs.org/)
  * Bootstrap (https://getbootstrap.com/)
  * vue-chart-3 (https://vue-chart-3.netlify.app/)
* Database:
  * SQLite (https://www.sqlite.org/index.html)

# 4. Design requirements

Minimalism, conciseness with emphasis on content.
