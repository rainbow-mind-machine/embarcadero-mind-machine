import embarcaderomindmachine as emm

"""
Run this example like:

$ CLIENT_ID="XXXXX" \
  CLIENT_SECRET="XXXXXXXX" \
  python two_bot.py

Where CLIENT_ID and CLIENT_SECRET are 
from your app page on Github.
"""

gk = emm.GithubKeymaker()
gk.set_apikeys_env()
gk.make_keys_from_strings(['bot1','bot2'], keys_out_dir='/tmp/keys')

