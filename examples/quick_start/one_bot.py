import embarcaderomindmachine as emm

"""
Run this example like:

$ CLIENT_ID="XXXXX" \
  CLIENT_SECRET="XXXXXXXX" \
  python one_bot.py

Where CLIENT_ID and CLIENT_SECRET are 
from your app page on Github.
"""

gk = emm.GithubKeymaker()
gk.set_apikeys_env()
gk.make_a_key('dummy','dummy.json','/tmp/keys')

