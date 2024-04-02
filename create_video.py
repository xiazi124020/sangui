from VideoGenerator import *

media_info = [
    ("images/test11.png", r"gtts\generated_audios\audio_1.mp3", 2),
    ("images/test12.png", r"gtts\generated_audios\audio_2.mp3", 9),
    ("images/test13.png", r"gtts\generated_audios\audio_3.mp3", 3)
]
intro_texts = [
    {"text": "タイトル", "start": 0, "duration": 1},
    {"text": "これは説明文です。", "start": 1, "duration": 1}
]

video_generator = VideoGenerator(output_file="final_output.mp4")
video_generator.generate_video(media_info, intro_texts=intro_texts)
# video_generator.generate_video(media_info, intro_text="你好，世界")
