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
