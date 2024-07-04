RUN DOCKER SERVER
1. Firstly, from a terminal or PowerShell session, pull the latest Postgres container image to your local image repository:
docker pull postgres:latest

2. Next, let's create a persistent volume in Docker to store our databases, tables, and data. This will allow us to retain our data even when our container is shut down:
docker volume create postgres-volume

3.docker run --name my-postgres --env POSTGRES_PASSWORD=YOURPASSWORD --volume postgres-volume:/var/lib/postgresql/data --publish 5432:5432 --detach postgres

4. install pgadmin4 
docker pull dpage/pgadmin4

5. docker run -e 'PGADMIN_DEFAULT_EMAIL=admin@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=admin' -p 8080:80 –name pgadmin4-dev dpage/pgadmin4

6.Connect postgres db to pgadmin4

docker inspect dpage/pgadmin4
Scroll down to get ipv4