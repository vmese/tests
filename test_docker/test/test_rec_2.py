import time
import pyaudio
import numpy as np


DEVICE_NAME = 'respeakermics'
SAMPLE_RATE = 48000
N_CHANNELS = 2
FRAMES_PER_BUFFER = 8192
RUN_DURATION = 10

OUT_FILE = open('/home/pi/test_respeakermics_2.raw','wb')

def get_device_ind(pyaudio_instance, device_name):
    """Get audio input device by name"""
    for ind in range(pyaudio_instance.get_device_count()):
        if device_name in pyaudio_instance.get_device_info_by_index(ind)['name']:
            return ind
    return -1


def callback(in_data,
             frame_count,
             time_info,
             status_flags):
    if status_flags == 1:
        print('*** pyaudio underflow !')
    if status_flags == 2:
        print('*** pyaudio overflow !')

    # get data in right format
    print('get data in callback 2')
    data = np.fromstring(in_data, dtype=np.int16)
    OUT_FILE.write(data.tobytes())
    return (None, 0)


def run():

    time.sleep(2)

    pyaudio_instance = pyaudio.PyAudio()

    for device in range(pyaudio_instance.get_device_count()):
        print(f'Available device : {pyaudio_instance.get_device_info_by_index(device)}')

    print(f'open {DEVICE_NAME} - deviceindex = {get_device_ind(pyaudio_instance, DEVICE_NAME)}')

    stream = pyaudio_instance.open(
            SAMPLE_RATE,
        N_CHANNELS,
        pyaudio.paInt16,
        input=True,
        input_device_index=get_device_ind(pyaudio_instance, DEVICE_NAME),
        frames_per_buffer=FRAMES_PER_BUFFER,
        start=False,
        stream_callback=callback)

    stream.start_stream()

    time.sleep(RUN_DURATION)

    stream.stop_stream()
    stream.close()
    pyaudio_instance.terminate()

if __name__ == "__main__":
    run()
