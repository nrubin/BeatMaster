import requests
from pyechonest import config, track
config.ECHO_NEST_API_KEY = "ERAACIJP7XRWDPHSZ"

# f = open("Kanye.mp3",'rb')

# t = track.track_from_file(f,"mp3")

t = track.track_from_id("TREZZIS139E66C60C4")

print t.id
print t.danceability
# print
print t.tempo