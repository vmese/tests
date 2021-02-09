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

#FROM 2000cubits/raspbian-python as base
FROM arm32v7/python:3.7.9-slim-buster as base

FROM base as builder
RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN apt-get update && apt-get upgrade -y

RUN apt install -y wget

RUN apt install -y python3.7
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
RUN apt install -y python3-pip

# install pyaudio
RUN apt install -y libasound2-dev
RUN apt install -y portaudio19-dev
RUN apt install -y libportaudio2
RUN apt install -y libportaudiocpp0
RUN apt install -y python3-pyaudio=0.2.11-1+b2

# librosa
RUN apt install -y  llvm=1:7.0-47
#RUN apt install -y libatlas-base-dev=3.10.3-8+rpi1
RUN apt install -y libatlas-base-dev

# Tensorflow
# from https://qengineering.eu/install-tensorflow-2.1.0-on-raspberry-pi-4.html
RUN apt-get install -y gfortran
RUN apt-get install -y libhdf5-dev=1.10.4+repack-10 libc-ares-dev=1.14.0-1 libeigen3-dev=3.3.7-1
RUN apt-get install -y libopenblas-dev libblas-dev=3.8.0-2
RUN apt-get install -y liblapack-dev=3.8.0-2 cython=0.29.2-2
# download the wheel
RUN wget https://github.com/Qengineering/Tensorflow-Raspberry-Pi/raw/master/tensorflow-2.1.0-cp37-cp37m-linux_armv7l.whl

# picamera
#RUN apt install -y python-picamera=1.13
#RUN apt install -y python3-picamera=1.13

#OpenCv
RUN apt install -y python3-opencv=3.2.0+dfsg-6

RUN apt install -y sox=14.4.2+git20190427-1

# Install requirements
RUN pip3 install --prefix=/install -r /requirements.txt

# delete the tensorflow wheel
RUN rm tensorflow-2.1.0-cp37-cp37m-linux_armv7l.whl

FROM base
COPY --from=builder /install /usr/local

#RUN apk add bash

# Testing resources
COPY test/ test/.
CMD bash -c "python3 ./test/test.py"