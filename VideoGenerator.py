from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

class VideoGenerator:
    def __init__(self, output_file="output_video.mp4"):
        self.output_file = output_file
    
    def generate_video(self, media_info, intro_texts=None, font="Meiryo", fps=24):
        if len(media_info) == 0:
            print("media_info is empty.")
            return

        clips = []

        is_setted = False
        for image_path, audio_path, audio_duration in media_info:
            img_clip = ImageClip(image_path).set_duration(audio_duration)
            audio_clip = AudioFileClip(audio_path).set_duration(audio_duration)
            img_clip = img_clip.set_audio(audio_clip)

            if intro_texts:
                if is_setted != True:
                    for intro_text_info in intro_texts:
                        text = intro_text_info["text"]
                        start = intro_text_info.get("start", 0) 
                        duration = intro_text_info.get("duration", audio_duration) 

                        txt_clip = TextClip(text, fontsize=24, color='white', font=font, size=img_clip.size)
                        txt_clip = txt_clip.set_start(start).set_duration(duration).set_position("center")
                        img_clip = CompositeVideoClip([img_clip, txt_clip])
                is_setted = True

            clips.append(img_clip)

        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile(self.output_file, fps=fps)

# 使用例
if __name__ == "__main__":
    media_info = [
        ("path/to/image1.png", "path/to/audio1.mp3", 10),
        ("path/to/image2.png", "path/to/audio2.mp3", 15),
    ]
    video_generator = VideoGenerator(output_file="final_output.mp4")
    video_generator.generate_video(media_info)
