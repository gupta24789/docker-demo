## Docker Demo


## Docker Build
- -d : flag is for detach mode
- -t : flag is for tag. using this you can provide the image name
- dot(.) : path of docker file if it is in same directory then define dot(.)
```
docker build -d -t docker-demo:1.0.0 .
```

#### Publish Port

- Publish the port using -p flag : HOST_PORT:CONTAINER_PORT
- you can access the app : localhost:5001
  

#### Env variable

There are multi ways you can define the env variable

1. use -e flag
```
docker run -d -p -e USER_NAME="user from env cmd" 5001:5000 docker-demo:1.0.0
```
2. use env file with --env-file flag
```
docker run -d -p --env-file .env 5001:5000 docker-demo:1.0.0
```
3. Inside docker file  using ENV
```
docker run -d -p 5001:5000 docker-demo:1.0.0
```

#### Lets use docker file env varibale
- --name flag to set the container name
```
docker run -d -p 5001:5000 --name docker-test docker-demo:1.0.0
```


#### Lets override the env variable using -e flag
- --name flag to set the container name
```
docker run -d -p 5001:5000 --name docker-test -e USER_NAME="user from env cmd" docker-demo:1.0.0
```

#### Lets override the env variable using .env file
- --name flag to set the container name
```
docker run -d -p 5001:5000 --name docker-test --env-file .env docker-demo:1.0.0
```


## Volume

- logs folder will generate inside the container we need to mount that folder outside.
Below is the syntax
- you need to pass the absolute path

```
docker run -v <host_folder>:<container_folder> <image>
```

```
docker run -d -p 5001:5000 -v /home/saurabh/logs:/app/logs --name docker-test docker-demo:1.0.0
```

## Compose File

- Build the Container
```
docker-compose build
```

- Start the Service
```
docker-compose up -d
```

- Stop the Service
```
docker-compose down
```










