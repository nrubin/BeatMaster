#I want to get the billboard hot 100 all the time

from bs4 import BeautifulSoup
import requests

from pyechonest import config, track, song as echo_nest_song
config.ECHO_NEST_API_KEY = "ERAACIJP7XRWDPHSZ"

class Song:
	"""
	Represents a very simple song.
	"""

	def __init__(self,title=None,artist=None,album=None):
		self. title = title
		self.artist = artist
		self.album = album
		self.clean_artist = self.parse_artist(artist) # artist used for echonest searching
		self.echo_nest = self.get_echonest()

	def __repr__(self):
		return "<Song Object: %s by %s from the album %s>" % (self.title,self.artist,self.album)

	def parse_artist(self,artists):
		featuring_index = artists.find("Featuring")
		if featuring_index > 0:
			main_artist = artists[0:featuring_index]
			return main_artist
		else:
			return artists

	def get_echonest(self):
		match = echo_nest_song.search(title=self.title, artist=self.clean_artist,results=1)[0]
		print match.id, match.title, match.artist_name
		return match

def get_one_page(page_number):
	base_url = "http://www.billboard.com/charts/hot-100&page="
	url = base_url+str(page_number)
	r = requests.get(url)
	soup = BeautifulSoup(r.text)

	raw_songs = soup.findAll("article",{"class":"song_review"})
	songs = []

	for raw_song in raw_songs:
		title = raw_song.find("h1").get_text().strip()
		album = raw_song.find("p",{"class":"chart_info"}).find("br").get_text().strip()
		try:
			artist = raw_song.find("p",{"class":"chart_info"}).find("a").get_text().strip()
		except:
			#some top 100 don't have album names
			artist = raw_song.find("p",{"class":"chart_info"}).find("br").get_text().strip()
		album = None
		song = Song(title,artist,album)
		songs.append(song)

	return songs


def get_billboard_100():
	songs = []
	for page_num in range(1):
		print page_num
		songs.extend(get_one_page(page_num))
	return songs


if __name__ == '__main__':
	all_songs = get_billboard_100()
	all_songs[1].song_id

