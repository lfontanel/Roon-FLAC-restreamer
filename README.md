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
<img src='https://g.gravizo.com/svg?
@startuml;

actor User;
participant "First Class" as A;
participant "Second Class" as B;
participant "Last Class" as C;

User -> A: DoWork;
activate A;

A -> B: Create Request;
activate B;

B -> C: DoWork;
activate C;

C --> B: WorkDone;
destroy C;

B --> A: Request Created;
deactivate B;

A --> User: Done;
deactivate A;

@enduml
'>