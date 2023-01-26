import wave
import aubio
import os
import subprocess

file_name = input("Enter the name of the .wav file: ")

with wave.open(file_name, 'rb') as wav_file:
    audio_file = os.path.join(file_name)
    tempo = aubio.tempo(method="default", hop_size=512)
    source = aubio.source(audio_file, 44100, hop_size=512)
    while True:
        samples, read = source()
        if read < 512:
            break
        tempo(samples)
        bpm = tempo.get_bpm()
    print("Original BPM: ", bpm)
    new_bpm = int(input("Enter the new BPM: "))
    new_file_path = file_name.replace('.wav', f'_{new_bpm}bpm.wav')
    subprocess.run(["rubberband", "-t", str(bpm/new_bpm), file_name, new_file_path])
    print(f"File saved at {new_file_path}")