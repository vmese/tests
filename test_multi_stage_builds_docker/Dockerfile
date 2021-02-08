# ------------------------------#
#        Normal build           #
# ------------------------------#

#FROM python:3.7-alpine

#COPY requirements.txt /requirements.txt

#RUN apk add --update gcc
#RUN apk add linux-headers \
#            libc-dev \
#            bash

# Install requirements
#RUN pip3 install -r /requirements.txt

# ------------------------------#
#      Multi stage build        #
# ------------------------------#

FROM python:3.7-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN apk add --update gcc
RUN apk add linux-headers \
            libc-dev

# Install requirements
RUN pip3 install --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local

RUN apk add bash

# Testing resources
COPY test/ test/.
CMD bash -c "python3 ./test/test.py"