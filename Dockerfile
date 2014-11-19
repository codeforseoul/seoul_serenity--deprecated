# This environment is based on python2

FROM debian:wheezy
MAINTAINER Hoony Jang <admin@chunsik.org>

# Run upgrades
RUN apt-get update

# Install basic packages
RUN apt-get --no-install-recommends install -y python-setuptools build-essential python-dev libpq-dev ca-certificates

# Install packages to need
RUN apt-get -y install git
RUN easy_install pip

# Install Seoul Serenity project
RUN mkdir /home/seoul_serenity
RUN git clone https://github.com/codeforseoul/seoul_serenity /home/seoul_serenity

# Setting up
RUN cd /home/seoul_serenity
RUN pip install -r requirements/dev.txt
RUN python manage.py db init
RUN python manage.py db migrate
RUN python manage.py db upgrade
RUN python manage.py runserver -h 0.0.0.0

WORKDIR /home/seoul_serenity
