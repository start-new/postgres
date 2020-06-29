# cookiecutter-postgres

Automatically generates a basic docker-compose file to install and use the postgresql database in your project, with or without pgadmin to manage it.

## Requirements & Install

To use the generated file, you need to have Docker installed on your computer. Then:

- Install Cookiecutter from PyPI using `pip install cookiecutter`
- Generate the docker-compose file using `cookiecutter gh:start-new/postgres`
- Answer the questions
- Move to the newly-created project folder using `cd <project_slug>`
- Launch the database using `docker-compose up` or `docker-compose up -d`
