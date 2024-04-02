from AzureTextToSpeech import *

tts = AzureTextToSpeech()
texts = ["こんにちは、世界！", "Azure Text to Speechを使っています。"]
audio_info = tts.synthesize_individual_audios(texts, voice_name="ja-JP-NanamiNeural", rate="1.0", output_prefix=r"azure\output")

for duration, file_name in audio_info:
    print(f"File: {file_name}, Duration: {duration} seconds")

audio_info = tts.synthesize_combined_audio(texts, voice_name="ja-JP-NanamiNeural", rate="1.0", output_file=r"azure\combined_output.wav")
print(f"Duration: {audio_info} seconds")
