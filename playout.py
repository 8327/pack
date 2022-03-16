#!/usr/bin/env python3

# playout would be a little daemon/wrapper that listens to commands (play, pause, file, url,
# volumne, etc.) somewhere(?) and then instructs vlc what to do. This should prevent two 
# audio streams beeing played back at the same time, etc.

import os
import socket
import time
import vlc

# test using:
# > nc -U playout.control.socket
# > play https://orf-live.ors-shoutcast.at/oe1-q2a


media = None

class Playout:

    vlc_instance = None
    player = None
    media = None

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



def prep():
    server_address = './playout.control.socket'
    if os.path.exists(server_address):
        os.unlink(server_address)
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)
    return sock

def execute(playout, command, params):
    if command == 'play':
        url = params[0]
        playout.play(url)


def main():
    playout = Playout()
    sock = prep()
    # currently only handles one connection at a time
    while True:
        connection, client = sock.accept()
        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break;
                line = data.decode("utf-8".rstrip())
                print(line)
                split = line.split()
                execute(playout, split[0], split[1:])
        finally:
            print("conn close")
            connection.close()

if __name__ == "__main__":
    main()


