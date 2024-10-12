This project uses `pipenv`

- first run `pipenv install` to install dependencies from Pipfile
- to run in dev mode: `python3 -m pipenv run uvicorn main:app --reload`
- to enter Swagger: `http://<your host>:<port>/docs`
- to enter Redoc: `http://<your host>:<port>/redoc`