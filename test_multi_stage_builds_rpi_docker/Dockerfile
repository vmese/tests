# ------------------------------#
#        Normal build           #
# ------------------------------#

#FROM 2000cubits/raspbian-python

#COPY requirements.txt /requirements.txt

#RUN apt-get update && apt-get upgrade -y

#RUN apt install python3.7
#RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
#RUN apt install -y python3-pip

# Install requirements
#RUN pip3 install -r /requirements.txt

# ------------------------------#
#      Multi stage build        #
# ------------------------------#

FROM 2000cubits/raspbian-python as base

FROM base as builder
RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN apt-get update && apt-get upgrade -y

RUN apt install python3.7
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
RUN apt install -y python3-pip

# Install requirements
RUN pip3 install --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local

#RUN apk add bash

# Testing resources
COPY test/ test/.
CMD bash -c "python3 ./test/test.py"