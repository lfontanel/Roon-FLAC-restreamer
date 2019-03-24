# Roon-FLAC-restreamer


### A- Software pre-requisites
_I installed everything on my Roon Core, but it can be installed on a different host.
If you install it on a different host, replace 'localhost' with your host name/ip address in your FLACReStreamer Roon radio station URL in step B-2._

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
chmod +x setup.liq
chmod +x restream.liq
./setup.liq
```

You should see a bunch of output. Using VLC, you can verify that http://localhost:8000/stream.flac is producing music FLAC-encoded at 16/44.1 .

#### 2. In Roon:

create an Internet Radio station with URL http://localhost:8000/stream.flac .

#### 3. At the command-line:

kill the setup.liq session (ctrl-D).

#### Roon Re-stream

