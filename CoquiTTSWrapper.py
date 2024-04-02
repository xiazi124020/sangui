import torch
from TTS.api import TTS
from pydub import AudioSegment

class CoquiTTSWrapper:
    def __init__(self, model_name, device='cuda'):
        self.device = device if torch.cuda.is_available() else 'cpu'
        self.tts = TTS(model_name).to(self.device)

    def synthesize_and_concatenate(self, text_list, speed=1.0, speaker_wav=None, output_file="coqui_output_combined.wav", format=".wav"):
        combined_audio = AudioSegment.empty()

        for text in text_list:
            temp_output = "temp_output.wav"
            self.tts.tts_to_file(text=text, speed=speed, speaker_wav=speaker_wav, file_path=temp_output)
            sound = AudioSegment.from_file(temp_output)
            combined_audio += sound

        combined_audio.export(output_file, format=format)

        total_duration_seconds = len(combined_audio) / 1000.0
        print(f"Generated {output_file} with total duration {total_duration_seconds} seconds")
        
        return total_duration_seconds

    def synthesize_and_return_durations(self, text_list, speed=1.0, speaker_wav=None, output_dir="output"):
        audio_info_list = []

        for index, text in enumerate(text_list):
            output_file_name = f"{output_dir}_{index}.wav"
            self.tts.tts_to_file(text=text, speed=speed, speaker_wav=speaker_wav, file_path=output_file_name)
            
            sound = AudioSegment.from_file(output_file_name)
            duration_seconds = len(sound) / 1000.0
            
            audio_info_list.append((duration_seconds, output_file_name))
            print(f"Generated {output_file_name}, Duration: {duration_seconds} seconds")

        return audio_info_list


# 使用示例
if __name__ == "__main__":
    model_name = "tts_models/ja/kokoro/tacotron2-DDC"
    content_list = ["こんにちは、世界！", "これはCoqui TTSのテストです。"]
    coqui_wrapper = CoquiTTSWrapper(model_name)
    coqui_wrapper.synthesize(content_list, speed=1.5, speaker_wav="path/to/speaker/wav")
