import shutil


def remove_pgadmin_dir():
    shutil.rmtree("pgadmin")


def main():
    if "{{ cookiecutter.use_pgadmin }}" != "y":
        remove_pgadmin_dir()


if __name__ == "__main__":
    main()
