from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

class VideoGenerator:
    def __init__(self, output_file="output_video.mp4"):
        self.output_file = output_file
    
    def generate_video(self, media_info, intro_text=None, font="Meiryo"):
        if len(media_info) == 0:
            print("media_info is empty.")
            return

        clips = []

        first_image_path, first_audio_path, first_audio_duration = media_info[0]
        background_clip = ImageClip(first_image_path).set_duration(first_audio_duration)
        audio_clip = AudioFileClip(first_audio_path)
        background_clip = background_clip.set_audio(audio_clip)

        if intro_text:
            txt_clip = TextClip(intro_text, fontsize=24, color='white', font="Meiryo", size=background_clip.size)
            txt_clip = txt_clip.set_duration(first_audio_duration).set_position("center")
            composite_clip = CompositeVideoClip([background_clip, txt_clip])
            clips.append(composite_clip)
        else:
            clips.append(background_clip)

        for image_path, audio_path, audio_duration in media_info[1:]:

            img_clip = ImageClip(image_path).set_duration(audio_duration)
            
            audio_clip = AudioFileClip(audio_path)
            
            img_clip = img_clip.set_audio(audio_clip)
            
            clips.append(img_clip)
        
        final_clip = concatenate_videoclips(clips, method="compose")
        
        # final_clip.write_videofile(self.output_file, codec="libx264", audio_codec="aac", fps=24)
        final_clip.write_videofile(self.output_file, fps=24)

# 使用例
if __name__ == "__main__":
    media_info = [
        ("path/to/image1.png", "path/to/audio1.mp3", 10),
        ("path/to/image2.png", "path/to/audio2.mp3", 15),
    ]
    video_generator = VideoGenerator(output_file="final_output.mp4")
    video_generator.generate_video(media_info)
