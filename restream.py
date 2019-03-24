#!/usr/bin/env python
# -*- coding: utf-8 -*-

ROON_HOST = "localhost"
ZONE = "Family Room"
STATION_NAME = "FLACReStreamer"

import sys
import os
import subprocess
import os.path
import urllib
from roon import RoonApi

def download(url):
    print("Downloading %s" % url)
    urllib.urlretrieve(url, 'source.out')

def roonConnect():
    token = None
    if os.path.isfile("roontoken.txt"):
        with open("roontoken.txt") as f:
            token = f.read()

    appinfo = {
        "extension_id": "python_roon_test",
        "display_name": "Python library for Roon",
        "display_version": "1.0.0",
        "publisher": "marcelveldt",
        "email": "my@email.com"
    }

    with RoonApi(appinfo, token, blocking_init=True, host=ROON_HOST) as roonapi:
        zone_id = roonapi.zone_by_output_name(ZONE)["zone_id"]
        output_id = roonapi.output_by_name(ZONE)["output_id"]
        print( "zone_id=%s, output_id = %s" % (zone_id,output_id) )

        roonapi.play_radio(zone_id,STATION_NAME)

        # save token
        token = roonapi.token
        print("token: %s" % token)
        with open("roontoken.txt", "w") as f:
            f.write(token)

def liquidSoap():
    print("Launching liquidsoap script")
    p = subprocess.Popen(['./play.liq'],
                         cwd=".",
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return p

if __name__ == "__main__":

    if (len(sys.argv)) != 2:
        print("Usage: %s url" % sys.argv[0])
        exit(1)

    download(sys.argv[1])
    p = liquidSoap()
    print("Queuing Roon")
    roonConnect()
    print("Enjoy!")