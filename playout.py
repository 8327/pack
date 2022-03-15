#!/usr/bin/env python3

# playout would be a little daemon/wrapper that listens to commands (play, pause, file, url,
# volumne, etc.) somewhere(?) and then instructs mpg321 what to do. This should prevent two 
# audio streams beeing played back at the same time, etc.

from mpyg321.mpyg321 import MPyg321Player

player = MPyg321Player()

player.play_song("sound.mp3")

