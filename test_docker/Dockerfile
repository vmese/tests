FROM arm32v7/python:3.7.9-buster

COPY requirements.txt ./

# install pyaudio
RUN apt-get update
RUN apt install -y libasound2-dev
RUN apt install -y portaudio19-dev
RUN apt install -y libportaudio2
RUN apt install -y libportaudiocpp0

RUN apt install -y python3-pyaudio=0.2.11-1+b2

# Install requirements
RUN pip3 install -r requirements.txt

# Testing resources
COPY test/ test/.
CMD bash -c "python3 ./test/test_pyaudio.py"