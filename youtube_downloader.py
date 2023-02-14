'''
from pytube import YouTube

DOWNLOAD_FOLDER = '/Users/bmrrossi/Downloads'
video_url = 'https://www.youtube.com/watch?v=85OW74R0qGc'
video_obj = YouTube(video_url)
stream = video_obj.streams.
stream.download(DOWNLOAD_FOLDER)
'''

from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=r6HiVSIzZeQ').streams.first().download()
