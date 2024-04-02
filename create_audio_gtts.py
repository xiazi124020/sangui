from GTTSWrapper import *

gtts_wrapper = GTTSWrapper(lang='ja')
texts = ["こんにちは、世界！", "抽象的な言葉で風景を描写することはできても、実際に絵を描く技能は持ち合わせていません。", "gTTSとpydubの組み合わせ。"]
gtts_wrapper.synthesize_texts(texts, r"gtts\combined_output_gTTS.mp3", speed_factor=1.4)

audio_info_list = gtts_wrapper.generate_individual_audios(texts, output_dir=r"gtts\generated_audios")

for info in audio_info_list:
    print(f"Duration: {info[0]} seconds, File: {info[1]}")
