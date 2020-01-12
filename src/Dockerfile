FROM python:3.7

LABEL maintainer "example <example@example.com>"

# Prepare environments
RUN pip install pipenv
COPY Pipfile /var/www/app/Pipfile
WORKDIR /var/www/app
RUN pipenv install

# Copy this project
COPY . /var/www/app

# Configration
EXPOSE 8000

# Execute
ENTRYPOINT ["pipenv"]
CMD ["run", "start"]
