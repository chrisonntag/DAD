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

## 
TODO: Use settings from envfile in Django settings as well. 
