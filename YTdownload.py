from pytube import YouTube
print("YT link")
url=input()
print("畫質")
qua=input()
yt = YouTube(url)
yt.title
yt.streams.all()
yt.streams.filter(resolution=qua).all()
yt.streams.filter(res=qua).all()[0]
yt.streams.filter(res=qua).first()
yt.streams.filter(res=qua,video_codec="vp9").all()
yt.streams.filter(res=qua,subtype="webm").all()

stream = yt.streams.filter(res=qua).first()
stream.download()