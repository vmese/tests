#FROM arm32v7/python:3.7.9-buster
FROM arm32v7/python:3.7-slim-buster

COPY requirements.txt ./

# install pyaudio
RUN apt-get update

RUN apt install -y \
    gcc \
    build-essential \
    make \
    libffi-dev \
    wget \
    #python3-pandas \
    libopenblas-base \
    libopenblas-dev

RUN apt install -y libasound2-dev
RUN apt install -y portaudio19-dev
RUN apt install -y libportaudio2
RUN apt install -y libportaudiocpp0

RUN apt install -y python3-pyaudio=0.2.11-1+b2

# Install requirements
RUN pip3 install -r requirements.txt

# Testing resources
COPY asound.conf /etc/asound.conf
RUN chmod 644 /etc/asound.conf
COPY start.sh /
COPY test/ test/.
CMD ["bash","start.sh"]
#CMD bash -c "python3 ./test/test_pyaudio.py"