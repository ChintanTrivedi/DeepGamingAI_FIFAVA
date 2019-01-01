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
                                       'porcupine_res/commands/skills/turn left_windows.ppn',
                                       'porcupine_res/commands/skills/turn right_windows.ppn',
                                       'porcupine_res/commands/skills/turn down_windows.ppn',
                                       'porcupine_res/commands/skills/turn up_windows.ppn',
                                       'porcupine_res/commands/skills/flick up_windows.ppn',
                                       'porcupine_res/commands/skills/flick down_windows.ppn',
                                       'porcupine_res/commands/skills/flick right_windows.ppn',
                                       'porcupine_res/commands/skills/flick left_windows.ppn'],
                                   sensitivities=[0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

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
                # turn left
                print('Performing skill: turn left')
                PressKey(pad8)
                PressKey(pad6)
                time.sleep(0.5)
                ReleaseKey(pad8)
                ReleaseKey(pad6)
                time.sleep(0.5)
                PressKey(pad8)
                PressKey(pad6)
                time.sleep(0.5)
                ReleaseKey(pad8)
                ReleaseKey(pad6)
            elif command_result == 1:
                # turn right
                print('Performing skill: turn right')
                PressKey(pad8)
                PressKey(pad4)
                time.sleep(0.5)
                ReleaseKey(pad8)
                ReleaseKey(pad4)
                time.sleep(0.5)
                PressKey(pad8)
                PressKey(pad4)
                time.sleep(0.5)
                ReleaseKey(pad8)
                ReleaseKey(pad4)
            elif command_result == 2:
                # turn down
                print('Performing skill: turn down')
                PressKey(pad4)
                PressKey(pad2)
                time.sleep(0.5)
                ReleaseKey(pad4)
                ReleaseKey(pad2)
                time.sleep(0.5)
                PressKey(pad4)
                PressKey(pad2)
                time.sleep(0.5)
                ReleaseKey(pad4)
                ReleaseKey(pad2)
            elif command_result == 3:
                # turn up
                print('Performing skill: turn up')
                PressKey(pad6)
                PressKey(pad2)
                time.sleep(0.5)
                ReleaseKey(pad6)
                ReleaseKey(pad2)
                time.sleep(0.5)
                PressKey(pad6)
                PressKey(pad2)
                time.sleep(0.5)
                ReleaseKey(pad6)
                ReleaseKey(pad2)
            elif command_result == 4:
                # flick up
                print('Performing skill: flick up')
                PressKey(pad2)
                time.sleep(0.3)
                ReleaseKey(pad2)
                time.sleep(0.1)
                PressKey(pad8)
                time.sleep(0.3)
                ReleaseKey(pad8)
                time.sleep(0.3)
                PressKey(pad8)
                time.sleep(0.3)
                ReleaseKey(pad8)
            elif command_result == 5:
                # flick down
                print('Performing skill: flick down')
                PressKey(pad8)
                time.sleep(0.3)
                ReleaseKey(pad8)
                time.sleep(0.1)
                PressKey(pad2)
                time.sleep(0.3)
                ReleaseKey(pad2)
                time.sleep(0.3)
                PressKey(pad2)
                time.sleep(0.3)
                ReleaseKey(pad2)
            elif command_result == 6:
                # flick right
                print('Performing skill: flick right')
                PressKey(pad4)
                time.sleep(0.3)
                ReleaseKey(pad4)
                time.sleep(0.1)
                PressKey(pad6)
                time.sleep(0.3)
                ReleaseKey(pad6)
                time.sleep(0.3)
                PressKey(pad6)
                time.sleep(0.3)
                ReleaseKey(pad6)
            elif command_result == 7:
                # flick left
                print('Performing skill: flick left')
                PressKey(pad6)
                time.sleep(0.3)
                ReleaseKey(pad6)
                time.sleep(0.1)
                PressKey(pad4)
                time.sleep(0.3)
                ReleaseKey(pad4)
                time.sleep(0.3)
                PressKey(pad4)
                time.sleep(0.3)
                ReleaseKey(pad4)

except KeyboardInterrupt:
    print('stopping ...')
finally:
    if porcupine_commands is not None:
        porcupine_commands.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
