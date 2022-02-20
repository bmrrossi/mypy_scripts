from pytube import YouTube

DOWNLOAD_FOLDER = '/Users/bmrrossi/Downloads'
video_url = 'https://www.youtube.com/watch?v=85OW74R0qGc'
video_obj = YouTube(video_url)
stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)
