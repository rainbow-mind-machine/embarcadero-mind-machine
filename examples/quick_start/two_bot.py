import embarcaderomindmachine as emm
import random, time

"""
Run this example like:

$ CLIENT_ID="XXXXX" \
  CLIENT_SECRET="XXXXXXXX" \
  python two_bot.py

Where CLIENT_ID and CLIENT_SECRET are 
from your app page on Github.
"""

global MASTER_COUNTER
MASTER_COUNTER = 1

def make_keys():
    # Keymaker
    gk = emm.GithubKeymaker()
    gk.set_apikeys_env()
    gk.make_keys_from_strings(['rainbowmindmachine','embarcaderomindmachine'], keys_out_dir='keys')

def run_flock():

    from custom_sheep import BlameSheep

    # Shepherd
    shepherd = emm.Shepherd(json_keys_dir='keys',
                            name='blame bot flock',
                            sheep_class=BlameSheep)
    shepherd.perform_parallel_action('blame',
                                      org='rainbow-mind-machine',
                                      repo='embarcadero-mind-machine',
                                      issueno=1)

if __name__=="__main__":
    #make_keys()
    run_flock()
