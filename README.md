# parsesql
A small python based sql parser focusing on finding table dependencies within database views. Currently only working with Snowflake ANSI Sql

The current implementation handles the parser as an seperate app that can be used to parse sql files. This is not a stable version. Within the 
next month the goal is to translate that app in a pip package. 

## minimalistic version of parsesql
no sqlalchemy, no writing to snowflake or sqlite, plain csv

## How to use the parser:
1. Download the repository
2. Intialize the pipenv or generate a requirement.text and intialize it
6. Configure the Runner class (multiprocessing, parsing vs. dataloading)
7. Run the main module with:
```
python parser/app.py
```
