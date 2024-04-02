from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

class VideoGenerator:
    def __init__(self, output_file="output_video.mp4"):
        self.output_file = output_file
    
    def generate_video(self, media_info, intro_texts=None, font="Meiryo", fps=24):
        if len(media_info) == 0:
            print("media_info is empty.")
            return

        clips = []

        for media in media_info:
            intro_texts = media["intro_texts"]
            img_clip = ImageClip(media["image"]).set_duration(media["audio_duration"])
            audio_clip = AudioFileClip(media["audio_file"]).set_duration(media["audio_duration"])
            img_clip = img_clip.set_audio(audio_clip)
            img_clip = img_clip.fadein(0.3).fadeout(0.3)

            text = intro_texts["text"]
            position = intro_texts["position"]

            txt_clip = TextClip(text, fontsize=36, color='white', font=font, size=(img_clip.w - 20, None), method='caption')
            txt_clip = txt_clip.set_duration(media["audio_duration"]).set_position(position)
            img_clip = CompositeVideoClip([img_clip, txt_clip])
            clips.append(img_clip)

        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile(self.output_file, fps=fps, codec="libx264")

