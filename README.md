# Postgresql Cookiecutter template

Automatically generates a basic docker-compose file to install and use the postgresql database in your project, with or without pgadmin to manage it.

## Requirements & Install

To use this project, you will need to install:
- [Docker Desktop](https://docs.docker.com/desktop/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

- Generate the compose.yml file using `uvx cookiecutter gh:start-new/postgres`
- Answer the questions
- Launch the database using `docker compose up -d`
