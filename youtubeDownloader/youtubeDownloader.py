import pytube

video_url = input('Informe a URL do Video: ')

youtube = pytube.YouTube(video_url)

video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').last()

video.download()
