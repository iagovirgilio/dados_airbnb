# pull official base image
FROM python:3.12.4-slim-bookworm

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/usr/src/app"
ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR:pt:en
ENV LC_ALL=pt_BR.UTF-8

# install system dependencies
RUN apt-get update \
    && apt-get install -y locales netcat-traditional gcc postgresql \
    && rm -rf /var/lib/apt/lists/*

# Generate the pt_BR.UTF-8 locale
RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && locale-gen

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]