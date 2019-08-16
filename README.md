# DeezerToSpotify
A guide to moving a Deezer playlist over to Spotify

The process:
1. Grap the playlist on Deezer manually, e.g. by doing:
   - save the web page to pl_dee.html
   - cleanup: `cat pl_dee.html | grep "itemprop=\"name\">" | sed 's/.*"name">//' | sed 's/<\/span>//' | sed 's/\&amp\;/\&/' | sed '/^$/d' > h.txt`
2. Goto https://developer.spotify.com/console/get-search-item/ to create a token (used in playlist.py)
3. Create the list of Spotify track ids: `python3 playlist.py h.txt > h_spot.txt`
4. Get your playlist's id using: https://developer.spotify.com/console/get-current-user-playlists/
5. Add your tracks by inserting the playlist id and the string of tracks (h_spot.txt) into: https://developer.spotify.com/console/post-playlist-tracks/
