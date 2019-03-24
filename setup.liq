
#!/usr/bin/liquidsoap -v

set("log.file.path","/tmp/liquidsoap.log")
set("log.stdout",true)

radio = mksafe(single("setup.mp3"))

output.icecast(%ogg(%flac(samplerate=44100, channels=2,compression=5,bits_per_sample=16)), host="localhost", port = 8000,  password = "roon", mount = "stream.flac",radio)
