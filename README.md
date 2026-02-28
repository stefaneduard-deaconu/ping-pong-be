# ping-pong-be

## database design

### entities (tables)

1. Players
2. Location
3. Matches
4. Tournament

### relationships in the database

- A match has 2 players -> 1 : 2 relationship
- A match has 1 unique location -> 1 : 1 relationship
- A tournament has multiple matches. 1 : M relationship (one to many)

## The Database

We use MySQL.

And to manage the DB in python, SQLAlchemy
SQLAlchemy is used to generate the database from Python code.

## Running the FastAPI project

To start the FastAPI server, run:

```shell
uvicorn main:app --reload
```

## Python Basics

### How to manage packages

1. Always create a project-level copy of python (named virutal environment, therefore venv)

    ```shell
    python -m venv .venv
    ```

2. Select the venv (or Python interpreter)

    Either using VS Code interface, or run
    ```shell
    .venv/Scripts/activate
    ```
    on Windows.

3. Use this to install packages

```shell
pip install sqlalchemy
```

4 Saving packages list to `requirements.txt`

    ```shell
    pip freeze  # only shows packages you installed
    pip freeze > requirements.txt  # save installed packages to the file
    ```

    Content of `requirements.txt` will be

    ```
    annotated-doc==0.0.4
    annotated-types==0.7.0
    anyio==4.12.1
    cffi==2.0.0
    click==8.3.1
    colorama==0.4.6
    cryptography==46.0.5
    dotenv==0.9.9
    fastapi==0.128.7
    greenlet==3.3.1
    h11==0.16.0
    idna==3.11
    pycparser==3.0
    pydantic==2.12.5
    pydantic_core==2.41.5
    PyMySQL==1.1.2
    python-dotenv==1.2.1
    SQLAlchemy==2.0.46
    starlette==0.52.1
    typing-inspection==0.4.2
    typing_extensions==4.15.0
    uvicorn==0.40.0
    ```