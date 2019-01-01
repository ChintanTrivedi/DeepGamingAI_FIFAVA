import pyaudio
import struct
from datetime import datetime
import time
from porcupine_res.porcupine import Porcupine
from directkeys import *

porcupine_commands = None
pa = None
audio_stream = None

try:
    porcupine_commands = Porcupine(library_path='porcupine_res/libpv_porcupine.dll',
                                   model_file_path='porcupine_res/porcupine_params.pv',
                                   keyword_file_paths=[
                                       'porcupine_res/commands/celebrations/mannequin_windows.ppn',
                                       'porcupine_res/commands/celebrations/work out_windows.ppn'],
                                   sensitivities=[0.9, 0.9])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine_commands.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine_commands.frame_length)

    while True:
        pcm = audio_stream.read(porcupine_commands.frame_length)
        pcm = struct.unpack_from("h" * porcupine_commands.frame_length, pcm)

        command_result = porcupine_commands.process(pcm)
        print('...')
        if command_result >= 0:
            # print('{} detected command: {}'.format(str(datetime.now()), command_result))
            if command_result == 0:
                # mannequin
                print('Performing celebration: mannequin')
                PressKey(caps)
                PressKey(pad8)
                time.sleep(6)
                ReleaseKey(caps)
                ReleaseKey(pad8)
            elif command_result == 1:
                # work out
                print('Performing celebration: work out')
                PressKey(caps)
                PressKey(Q)
                time.sleep(0.3)
                ReleaseKey(Q)
                time.sleep(0.2)
                PressKey(Q)
                time.sleep(0.3)
                ReleaseKey(Q)
                ReleaseKey(caps)

except KeyboardInterrupt:
    print('stopping ...')
finally:
    if porcupine_commands is not None:
        porcupine_commands.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
