# Quartz server

## Intro

i started developing this as my school project but now it just shows that i can create backend in python

## Structure

Add later

## TODO

:3

## Start local development

- install uv
- install docker
- start docker
- clone this repo
- docker run --rm -d --name postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -p 5430:5432 postgres
- docker exec -it postgres psql -U myuser -c 'CREATE DATABASE mydb;'
- cp .env.example .env
- uv run src/main.py

or start with 

docker-compose up