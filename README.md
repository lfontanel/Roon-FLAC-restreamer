# Roon-FLAC-restreamer



### Software pre-requisites
_I installed everything on my Roon Core, but it can be installed on a different host.
If you install it on a different host, replace 'localhost' with your host name/ip address in your FLACReStreamer Roon radio station URL._

```bash
# I'm using Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-46-generic x86_64)
pip3 install /Users/.../Downloads/six-1.12.0.tar.gz # had to manually pull it
pip3 install /Users/.../Downloads/websocket_client-0.54.0.tar.gz # had to manually pull it
pip3 install roonapi
pip3 install requests
sudo apt install icecast2 # use 'roon' as default password 
sudo apt install liquidsoap
```

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf}
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
)
