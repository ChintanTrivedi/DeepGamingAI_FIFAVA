import struct
import time

import pyaudio

from directkeys import *
from porcupine_res.porcupine import Porcupine

porcupine_wakeword = None
pa = None
audio_stream = None
awake = False
start_time = None
wake_time = 5000  # ms
try:
    porcupine_wakeword = Porcupine(library_path='porcupine_res/libpv_porcupine.dll',
                                   model_file_path='porcupine_res/porcupine_params.pv',
                                   keyword_file_paths=['porcupine_res/commands/wakewords/OkayEA_windows.ppn'],
                                   sensitivities=[0.9])

    porcupine_commands = Porcupine(library_path='porcupine_res/libpv_porcupine.dll',
                                   model_file_path='porcupine_res/porcupine_params.pv',
                                   keyword_file_paths=[
                                       'porcupine_res/commands/tactics/C B joins attack_windows.ppn',
                                       'porcupine_res/commands/tactics/team pressing_windows.ppn',
                                       'porcupine_res/commands/tactics/swap wings_windows.ppn',
                                       'porcupine_res/commands/tactics/offside trap_windows.ppn',
                                       'porcupine_res/commands/tactics/long ball_windows.ppn',
                                       'porcupine_res/commands/tactics/possession_windows.ppn',
                                       'porcupine_res/commands/tactics/counter attack_windows.ppn',
                                       'porcupine_res/commands/tactics/high pressure_windows.ppn'],
                                   sensitivities=[0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine_wakeword.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine_wakeword.frame_length)

    while True:
        pcm = audio_stream.read(porcupine_wakeword.frame_length)
        pcm = struct.unpack_from("h" * porcupine_wakeword.frame_length, pcm)

        if not awake:
            print('...')
            result = porcupine_wakeword.process(pcm)
            if result:
                awake = True
                start_time = time.time()
                print('Voice Assistant activated, give command...')
        else:
            if (time.time() - start_time) * 1000 > wake_time:
                print('Voice assistant going back to sleep')
                awake = False
            command_result = porcupine_commands.process(pcm)
            if command_result >= 0:
                # print('{} detected command: {}'.format(str(datetime.now()), command_result))
                if command_result == 0:
                    # C B joins attack
                    print('Activating - C B joins attack')
                    PressKey(home)
                    time.sleep(0.3)
                    ReleaseKey(home)
                    time.sleep(1)
                    PressKey(pagedown)
                    time.sleep(0.3)
                    ReleaseKey(pagedown)
                elif command_result == 1:
                    # team pressing
                    print('Activating - team pressing')
                    PressKey(home)
                    time.sleep(0.3)
                    ReleaseKey(home)
                    time.sleep(1)
                    PressKey(end)
                    time.sleep(0.3)
                    ReleaseKey(end)
                elif command_result == 2:
                    # swap wings
                    print('Activating - swap wings')
                    PressKey(home)
                    time.sleep(0.3)
                    ReleaseKey(home)
                    time.sleep(1)
                    PressKey(delete)
                    time.sleep(0.3)
                    ReleaseKey(delete)
                elif command_result == 3:
                    # offside trap
                    print('Activating - offside trap')
                    PressKey(home)
                    time.sleep(0.3)
                    ReleaseKey(home)
                    time.sleep(1)
                    PressKey(home)
                    time.sleep(0.3)
                    ReleaseKey(home)
                elif command_result == 4:
                    # long ball
                    print('Activating - long ball')
                    PressKey(end)
                    time.sleep(0.3)
                    ReleaseKey(end)
                    time.sleep(1)
                    PressKey(pagedown)
                    time.sleep(0.3)
                    ReleaseKey(pagedown)
                elif command_result == 5:
                    # possession
                    print('Activating - possession')
                    PressKey(end)
                    time.sleep(0.3)
                    ReleaseKey(end)
                    time.sleep(1)
                    PressKey(delete)
                    time.sleep(0.3)
                    ReleaseKey(delete)
                elif command_result == 6:
                    # counter attack
                    print('Activating - counter attack')
                    PressKey(end)
                    time.sleep(0.3)
                    ReleaseKey(end)
                    time.sleep(1)
                    PressKey(home)
                    time.sleep(0.3)
                    ReleaseKey(home)
                elif command_result == 7:
                    # high pressure
                    print('Activating - high pressure')
                    PressKey(end)
                    time.sleep(0.3)
                    ReleaseKey(end)
                    time.sleep(1)
                    PressKey(end)
                    time.sleep(0.3)
                    ReleaseKey(end)

                # Put back to sleep state after executing command
                awake = False

except KeyboardInterrupt:
    print('stopping ...')
finally:
    if porcupine_wakeword is not None:
        porcupine_wakeword.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
