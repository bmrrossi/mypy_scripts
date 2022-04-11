import pyshorteners

s = pyshorteners.Shortener()

print(s.tinyurl.short('https://www.youtube.com/watch?v=tmPs2hrH8jk'))
