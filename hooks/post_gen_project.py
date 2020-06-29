import os
import shutil


def remove_pgadmin_dir():
    shutil.rmtree(Pathlib("{{ cookiecutter.project_slug }}") / "pgadmin")

def main():
    {% if cookiecutter.use_pgadmin -%}
    remove_pgadmin_dir()
    {% else -%}
    pass
    {-% endif %} 


if __name__ == "__main__":
    main()