# Instagram

Author:[MelvinOmega](https://github.com/MelvinOmega)  
  
# Description  

This is a clone of the website for the Instagram app where users share their  images and ideas for other users to view them.Users can Sign in to the application,Upload pictures to the application,See their profile with all their pictures.


## User Story  
  
* Sign in to the application to start using.  
* Upload a picture to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  

  
## Setup and installations
* git clone .
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3 manage.py runserver`



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

#### Clone the Repo 
```bash
git clone https://github.com/MelvinOmega/instagram-clone
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3 -m venv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='**'
DEBUG=True
DB_NAME='****'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3 manage.py check
python manage.py makemigrations
python3 manage.py migrate
```

#### Run the app
```bash
python3 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


        
## Technologies Used

* [Python3.8](https://docs.python.org/3/)
* Django 
* Postgresql 
* Boostrap
* HTML

## Contact Information   
You are encouraged to email me at melvinomega151@gmail.com for any question or contributions
  
## License 

[MIT](LICENSE.md)  <br>
Copyright © Melvin Omega

