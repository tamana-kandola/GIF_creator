from moviepy.editor import *

clips = []
clip1 =  ImageClip('images/image1.png').set_duration(2)
clip2 =  ImageClip('images/image2.png').set_duration(3)
clip3 =  ImageClip('images/image3.png').set_duration(4)
clips.append(clip1)
clips.append(clip2)
clips.append(clip3)

video_clip = concatenate_videoclips(clips, method='compose')
video_clip.write_videofile("video-output.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
