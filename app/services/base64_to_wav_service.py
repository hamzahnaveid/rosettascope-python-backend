import base64
import wave
import subprocess

def base64_to_wav(base64_string):
    try:
        wav_data = base64.b64decode(base64_string)
        with open("app/resources/recording.mp3", 'wb') as f:
            f.write(base64.b64decode(base64_string))
        print(f'Converted base64 to MP3 successfully!')
        
        subprocess.run([
            "ffmpeg", "-y",
            "-i", "app/resources/recording.mp3",
            "-ac", "1",
            "-ar", "16000",
            "-sample_fmt", "s16",
            "app/resources/output.wav"
        ], check=True)
        try:
            with wave.open("app/resources/output.wav", "rb") as wf:
                print("Channels:", wf.getnchannels())
                print("Sample width:", wf.getsampwidth())
                print("Sample rate:", wf.getframerate())
                print("Frames:", wf.getnframes())
        except wave.Error as e:
            print("WAV ERROR:", e)


    except Exception as e:
        print(f'Error converting base64 to .wav: {e}')