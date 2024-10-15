This project uses `pipenv`, `fastapi`, `pydantic` and `SQLmodel`

> Since Ubuntu 24.04 we can't install `pip` packages globally, use `pipx` instead:
> `sudo nala install pipx`
> `pipx install pipenv`
> restart terminal 

- first run `pipenv install` to install dependencies from Pipfile
- to run in dev mode: `python3 -m pipenv run uvicorn main:app --reload`
- to enter Swagger: `http://<your host>:<port>/docs`
- to enter Redoc: `http://<your host>:<port>/redoc`