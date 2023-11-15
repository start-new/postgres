from pathlib import Path
import random
import shutil
import secrets

def move_files():
    Path("{{ cookiecutter.project_slug }}").joinpath("docker-compose.yml").rename(Path("docker-compose.yml"))

def delete_project_dir():
    """Removes the project folder."""
    shutil.rmtree("{{ cookiecutter.project_slug }}")

def set_flag(
    file_path, flag, length=64, value=None, formatted=None, *args, **kwargs
):
    if value is None:
        value = secrets.token_urlsafe(length)

    with file_path.open("r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value


def set_postgres_auto_port():
    postgres_auto_port = random.randint(10000, 65535)
    set_flag(
        Path("docker-compose.yml"),
        "!!!SET POSTGRESQL_PORT!!!",
        value=str(postgres_auto_port),
    )
    return postgres_auto_port


def set_flags():
    set_postgres_auto_port()


def main():
    """Final touches to our project."""

    set_flags()
    move_files()
    delete_project_dir()
  


if __name__ == "__main__":
    main()
