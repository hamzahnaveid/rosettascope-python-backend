import base64

def base64_to_wav(base64_string, output_file):
    try:
        wav_data = base64.b64decode(base64_string)
        with open(output_file, 'wb') as f:
            f.write(wav_data)
        print(f'Converted base64 to {output_file} successfully!')
    except Exception as e:
        print(f'Error converting base64 to .wav: {e}')