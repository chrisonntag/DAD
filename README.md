# Digital Archive Discovery: DAD
## Setup
Rename ```.env-sample``` to ```.env``` and enter the postgres login data and create a SECRET_KEY.
You can export all the variables to your local environment with

```
export $(xargs <.env)
```

Build the docker containers with

```
docker-compose build
```

and start containers with 

```
docker-compose up
```

In order to create a first user, open the CLI for the backend container with the Docker GUI 
and execute

```
python manage.py createsuperuser
```

Then go to 

```
localhost:3000/login
```

in order to log into the frontend. 

The API is available under

```
http://localhost:8000/api/users/
http://localhost:8000/api/items/
```





