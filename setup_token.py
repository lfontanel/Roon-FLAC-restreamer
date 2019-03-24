

import os.path
from roon import RoonApi

ROON_HOST = "localhost"

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

roonapi = RoonApi(appinfo, token, host=ROON_HOST)
roonapi.stop()

token = roonapi.token
if token:
    print(token)
    with open("mytokenfile", "w") as f:
        f.write(token)
