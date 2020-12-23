# ClowdFlows with text embeddings widgets

This repository contains a docker compose configuration for a local Clowdflows installation with text embeddings widgets pre-installed. Data mining and relational data mining widgets are also pre-installed.

To run it, docker and docker-compose must be installed on your system.

Simply clone this repository then execute the following commands:

```shell script
docker-compose up -d
```

This will build and run the containers. The building might take a couple of minutes. After that step is complete run the following to download all available text embeddings models:

```shell script
docker-compose exec backend python -m cf_text_embeddings.downloader -d all
``` 

When these two steps are complete you can access ClowdFlows locally here: http://localhost:8080/

If you need to create a superuser to access the admin interface ( http://localhost:8080/admin/ ) - run the following commad:

```shell script
docker-compose exec backend python manage.py createsuperuser
```
