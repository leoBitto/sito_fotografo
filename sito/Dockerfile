# pull official base image
FROM python:3.9.6

# set work directory its an absolute path
#WORKDIR /usr/src/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

EXPOSE 8000
CMD ["gunicorn", "sito.wsgi:application", "--bind", "0.0.0.0:8000"]
