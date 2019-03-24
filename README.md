# Roon-FLAC-restreamer

### DISCLAIMER

This is a proof of concept.
My environment is a Roon Core running on Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-46-generic x86_64).
I have no idea if it works on any other platform.
It assumes you know what you're doing.
This comes "as-is", i.e. I might answer questions on the Roon forum but assume it comes with no support.
_*If you're afraid to break your Roon server, do not install it.*_

### A- Software pre-requisites
_I installed everything on my Roon Core, but it can be installed on a different host.
If you install it on a different host, replace 'localhost' with your host name/ip address in your FLACReStreamer Roon radio station URL in step B-2 and edit the .py and .liq files accordingly._

```bash
# I'm using Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-46-generic x86_64)
pip3 install /Users/.../Downloads/six-1.12.0.tar.gz # had to manually download it
pip3 install /Users/.../Downloads/websocket_client-0.54.0.tar.gz # had to manually download it
pip3 install roonapi
pip3 install requests
sudo apt install icecast2 # use 'roon' as default password or use your own but edit the .liq files
sudo apt install liquidsoap
```

### B- Roon setup

#### 1. At the command-line:

```bash
chmod +x setup_token.py
chmod +x restream.py
chmod +x setup.liq
chmod +x play.liq
./setup.liq
```

You should see a bunch of output. Using VLC, you can verify that http://localhost:8000/stream.flac is producing music FLAC-encoded at 16/44.1 .

#### 2. In Roon:

create an Internet Radio station with URL http://localhost:8000/stream.flac named _*FLACReStreamer*_.

#### 3. At the command-line:

Kill the setup.liq session (ctrl-D).

#### Setup the ROON API wrapper

#### 4. At the command-line:

```bash
laurent@nexus7:~$ ./setup_token.py
2019-03-24 15:24:25,064 INFO   roonapi -- Connecting to Roon server x.x.x.x:9100
2019-03-24 15:24:25,071 INFO   roonapi -- Connection with roon websockets (re)created.
2019-03-24 15:24:25,072 INFO   roonapi -- The application should be approved within Roon's settings.
```

#### 5. In Roon again:

Settings > Extensions > Python API for Roon > Enable
The console should show:

```bash
2019-03-24 15:24:38,175 INFO   roonapi -- Registered to Roon server xxx
```

#### 4. At the command-line:

The script should complete and print the API token.

#### Now we can finally re-stream!

```bash
./restream.py https://sample-videos.com/audio/mp3/crowd-cheering.mp3
```
You're welcome!

