# DeezerToSpotify
A guide to moving a Deezer playlist over to Spotify

The process
1. Grap the playlist on Deezer manually, e.g. by doing:
   - save the web page to hlaup.txt
   - grep "itemprop=\"name\">" hlaup.txt  > h.txt
   - cleanup h.txt, e.g. in vi using ":1,$s/.*"name">//" and ":1,$s/<\/span>//"
2. Goto https://developer.spotify.com/console/get-search-item/ to create a token (used in playlist.py)
3. Create the list of Spotify track ids: python3 playlist.py h.txt > h_spot.txt
4. Merge the lines in h_spot.txt to a comma-seperated string, e.g. by doing
   - ":1,$s/\n/,/" in vi
5. Get your playlist's id using: https://developer.spotify.com/console/get-current-user-playlists/
6. Add your tracks by inserting the playlist id and the string of tracks into: https://developer.spotify.com/console/post-playlist-tracks/
