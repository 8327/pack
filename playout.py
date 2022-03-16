#!/usr/bin/env python3

# playout would be a little daemon/wrapper that listens to commands (play, pause, file, url,
# volumne, etc.) somewhere(?) and then instructs vlc what to do. This should prevent two 
# audio streams beeing played back at the same time, etc.

import time
import vlc

media = vlc.MediaPlayer('https://orf-live.ors-shoutcast.at/oe1-q2a')
media.play()

time.sleep(10)

