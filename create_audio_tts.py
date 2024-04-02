from CoquiTTSWrapper import *

model_name = "tts_models/ja/kokoro/tacotron2-DDC"
content_list = ["抽象的な言葉で風景を描写することはできても、実際に絵を描く技能は持ち合わせていません。", "これはCoqui TTSのテストです。"]
coqui_wrapper = CoquiTTSWrapper(model_name)
coqui_wrapper.synthesize_and_concatenate(content_list, speed=2, output_file=r"tts/coqui_output_speed2.wav")

durations_and_files = coqui_wrapper.synthesize_and_return_durations(content_list, speed=2, output_dir=r"tts/coqui_output_speed2")

for duration, file in durations_and_files:
    print(f"File: {file}, Duration: {duration} seconds")
