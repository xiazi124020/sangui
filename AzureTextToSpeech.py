import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import tempfile

load_dotenv()
class AzureTextToSpeech:
    def __init__(self):
        self.subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")
        self.service_region = os.getenv("AZURE_SERVICE_REGION")
        self.speech_config = speechsdk.SpeechConfig(subscription=self.subscription_key, region=self.service_region)
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config)

    def synthesize_individual_audios(self, texts, voice_name="ja-JP-NanamiNeural", rate="1.0", output_prefix="output"):
        audio_info_list = []

        for index, text in enumerate(texts):
            output_file_name = f"{output_prefix}_{index}.wav"
            ssml = f"""
            <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='ja-JP'>
                <voice name='{voice_name}'>
                    <prosody rate='{rate}'>{text}</prosody>
                </voice>
            </speak>
            """
            audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file_name)
            synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
            result = synthesizer.speak_ssml_async(ssml).get()

            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                audio_segment = AudioSegment.from_file(output_file_name)
                duration_seconds = len(audio_segment) / 1000.0
                audio_info_list.append((duration_seconds, output_file_name))
                print(f"Generated {output_file_name} with duration {duration_seconds} seconds")
            else:
                print(f"Failed to synthesize {text}")

        return audio_info_list
    
    def synthesize_combined_audio(self, texts, output_file="combined_output.wav", voice_name="ja-JP-NanamiNeural", rate="1.0"):
        combined_audio = AudioSegment.empty()

        for text in texts:
            ssml = f"""
            <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='ja-JP'>
                <voice name='{voice_name}'>
                    <prosody rate='{rate}'>{text}</prosody>
                </voice>
            </speak>
            """
            temp_file_path = tempfile.mkstemp(suffix=".wav")[1]
            audio_config = speechsdk.audio.AudioOutputConfig(filename=temp_file_path)
            synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
            result = synthesizer.speak_ssml_async(ssml).get()

            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                audio_segment = AudioSegment.from_file(temp_file_path)
                combined_audio += audio_segment

        combined_audio.export(output_file, format="wav")
        total_duration_seconds = len(combined_audio) / 1000.0
        print(f"Generated combined audio {output_file} with total duration {total_duration_seconds} seconds")
        
        return total_duration_seconds

# 使用示例
if __name__ == "__main__":
    tts = AzureTextToSpeech()
    segments = [
        {"text": "こんにちは、世界！", "voice_name": "ja-JP-NanamiNeural", "rate": "1.5"},
        {"text": "Hello, world!", "voice_name": "en-US-JennyNeural", "rate": "1.0"},
        {"text": "Bonjour le monde!", "voice_name": "fr-FR-DeniseNeural", "rate": "1.0"}
    ]
    tts.synthesize_speech_advanced(segments)
