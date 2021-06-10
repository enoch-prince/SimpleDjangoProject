# SimpleDjangoProject
A simple Django project that implements multi-user login and permission-based access to data via API endpoints. Django Restframework was utilized for the API implementations.

## Pre-requisite Installation
- Install the latest version of [python](https://www.python.org/downloads/)
- Install *pipenv* from the command line using the command:
    ```bash
    $ pip install --user pipenv
    ```
- Clone the repository or download the repository and the navigate to the repository on the command line
- Install dependencies for the project:
    ```bash
    $ pipenv install
    ```
 
 ## Running the Django App
 - Activate the virtual environement created by *pipenv* by typing in the command line:
   ```bash
    $ pipenv shell
   ```
 - Run the server:
    ```bash
    $ cd portfolio
    $ python manage.py runserver
    ```
  
  ## API Endpoints
  A list of the implemented API endpoints are listed below:
  
  - **/api/view-users** - GET request to view all signed up users. It requires admin priviledges
  - **/api/user** - GET, POST, HEAD request to view all basic users and create a new basic user
  - **/api/user/<int:pk>** - GET, PUT, DELETE request to view specific basic user, edit and delete methods is reserved only admin and logged in users whose public key (pk) matches the endpoint.
  - **/api/user/employee** - GET, POST, HEAD request to view all employees and create a new employee
  - **/api/user/employee/<int:pk>** - GET, PUT, DELETE request to view specific employee, editing and deleting is reserved only for admin and logged in employees whose public key (pk) matches the endpoint.
  - **/api/user/employee/director** - GET, POST, HEAD request to view all directors and create a new director. POST request is reserved for admin and other directors
  - **/api/user/employee/director/<int:pk>** - GET, PUT, DELETE request to view specific director, editing and deleting is reserved only for admin and logged in directors whose public key (pk) matches the endpoint.
  - **/api/user/employee/ceo** - GET, POST, HEAD request to view all CEOs and create a new CEO. Reserved for only the admin.
  - **/api/user/employee/director/<int:pk>** - GET, PUT, DELETE request to view specific ceo, editing and deleting is reserved only for admin and logged in ceos whose public key (pk) matches the endpoint.
  
  ## Contributing
  Please make a pull request if you want to contribute to this project
  
  ##License
  MIT License
