from AzureTextToSpeech import *
from contents import *

tts = AzureTextToSpeech()
# texts = ["抽象的な言葉で風景を描写することはできても、実際に絵を描く技能は持ち合わせていません。", "抽象的な言葉で風景を描写することはできても、実際に絵を描く技能は持ち合わせていません。Azure Text to Speechを使っています。"]
audio_info = tts.synthesize_individual_audios(contest_test_ja, voice_name="ja-JP-NanamiNeural", rate="1.3", output_prefix=r"azure\output")

for duration, file_name in audio_info:
    print(f"File: {file_name}, Duration: {duration} seconds")

# audio_info = tts.synthesize_combined_audio(texts, voice_name="ja-JP-NanamiNeural", rate="1.3", output_file=r"azure\combined_output.wav")
# print(f"Duration: {audio_info} seconds")
