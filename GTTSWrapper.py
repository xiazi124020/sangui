from gtts import gTTS
from pydub import AudioSegment
import io
import os

class GTTSWrapper:
    def __init__(self, lang='ja'):
        self.lang = lang

    def synthesize_texts(self, texts, output_file, slow=False, speed_factor=1.0, format="mp3"):
        combined_sound = AudioSegment.empty()
        
        for text in texts:
            tts = gTTS(text=text, lang=self.lang, slow=slow)
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            sound = AudioSegment.from_file(mp3_fp, format=format)
            combined_sound += sound
        
        if speed_factor != 1.0:
            combined_sound = combined_sound.speedup(playback_speed=speed_factor)

        combined_sound.export(output_file, format=format)

    def generate_individual_audios(self, texts, output_dir, slow=False, speed_factor=1.0, format="mp3"):
        audio_info_list = []

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for index, text in enumerate(texts, start=1):
            tts = gTTS(text=text, lang=self.lang, slow=slow)
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            sound = AudioSegment.from_file(mp3_fp, format=format)

            if speed_factor != 1.0:
                sound = sound.speedup(playback_speed=speed_factor)

            output_file_path = os.path.join(output_dir, f"audio_{index}.{format}")
            sound.export(output_file_path, format=format)

            duration_seconds = len(sound) / 1000.0
            audio_info_list.append((duration_seconds, output_file_path))

        return audio_info_list

if __name__ == "__main__":
    gtts_wrapper = GTTSWrapper(lang='ja')
    texts = ["こんにちは、世界！", "これはテストです。", "gTTSとpydubの組み合わせです。"]
    gtts_wrapper.synthesize_texts(texts, "combined_output_gTTS.mp3", speed_factor=1.0)
