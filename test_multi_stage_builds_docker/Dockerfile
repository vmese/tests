FROM python:3.7-alpine

COPY requirements.txt ./

RUN apk add --update gcc
RUN apk add linux-headers \
            libc-dev \
            bash

# Install requirements
RUN pip3 install -r requirements.txt

# Testing resources
COPY test/ test/.
CMD bash -c "python3 ./test/test.py"