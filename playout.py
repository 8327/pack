#!/usr/bin/env python3

"""
playout is a little wrapper around VLC (via python-vlc) that runs as a daemon 
and interprets a simplistic set of audio commands (play, pause, vol, ...).

"""

import localbus
import os
import socket
import time
import vlc

media = None

class Playout:
    def __init__(self):
        self.vlc_instance = vlc.Instance()
        self.player = self.vlc_instance.media_player_new()
    def play(self, media):
        self.media = self.vlc_instance.media_new(media)
        self.player.set_media(self.media)
        self.player.play()
    def pause(self):
        self.player.pause()
    def stop(self):
        self.player.stop()
    def vol(self, value):
        self.player.audio_set_volume(value)


def execute(command, params):
    if command == 'play':
        url = params[0]
        playout.play(url)
    elif command == 'pause':
        playout.pause()
    elif command == 'stop':
        playout.stop()
    elif command == 'vol':
        playout.vol(int(params[0]))

def receive(message):
    split = message.split()
    if len(message) > 0:
        execute(split[0], split[1:])
    else:
        print("empty message")

playout = Playout()
bus = localbus.Bus(receive)
while True:
        time.sleep(1)


