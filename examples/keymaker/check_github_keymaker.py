import embarcaderomindmachine as emm

"""
Run this example like:

$ CLIENT_ID="XXXXX" \
  CLIENT_SECRET="XXXXXXXX" \
  python one_bot.py

Where CLIENT_ID and CLIENT_SECRET are 
from your app page on Github.
"""

ghk = emm.GithubKeymaker()
ghk.set_apikeys_env()
ghk.make_a_key('dummy','dummy.json','/tmp/keys')

