# Test for simultaneoulsy recording sound from the Respeaker mics with pyaudio inside of a docker
# 

## Description
The test must be executed on a Raspberry Pi

It stores the 2 channels in the /home/pi/ directory in .raw format (S16_LE, 48000 Hz)

## Build
Type : 

docker build -t "test_pyaudio" .

## Execute

Type : 

docker container run -v /home/pi/:/home/pi/ --device /dev/snd test_pyaudio


