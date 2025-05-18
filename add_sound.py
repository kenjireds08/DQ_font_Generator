from moviepy.editor import VideoFileClip, AudioFileClip

# GIFを動画として読み込む
clip = VideoFileClip("dq_message.gif")

# 音源を読み込む
# 動画の長さに合わせて音源を切り取る（またはループ等も可能）
audio = AudioFileClip("sound.mp3").subclip(0, clip.duration)

# 音源を動画に合成
clip = clip.set_audio(audio)

# 出力（MP4）
clip.write_videofile("dq_message_with_sound.mp4", codec="libx264", audio_codec="aac")

print("音付き動画 dq_message_with_sound.mp4 を出力しました！")


# GIFを動画として読み込む
clip = VideoFileClip("dq_message.gif")

# 音源を読み込む
# 動画の長さに合わせて音源を切り取る（またはループ等も可能）
audio = AudioFileClip("sound.mp3").subclip(0, clip.duration)

# 音源を動画に合成
clip = clip.set_audio(audio)

# 出力（MP4）
clip.write_videofile("dq_message_with_sound.mp4", codec="libx264", audio_codec="aac")

print("音付き動画 dq_message_with_sound.mp4 を出力しました！")
