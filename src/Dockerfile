FROM python:3.7

LABEL maintainer "example <example@example.com>"

# Prepare environments
RUN pip install poetry
COPY pyproject.toml /var/www/app/pyproject.toml
WORKDIR /var/www/app
RUN poetry install

# Copy this project
COPY . /var/www/app

# Configration
EXPOSE 8000

# Execute
ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
