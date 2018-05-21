import embarcaderomindmachine as emm

"""
Run this example like:

$ CLIENT_ID="XXXXX" \
  CLIENT_SECRET="XXXXXXXX" \
  python two_bot.py

Where CLIENT_ID and CLIENT_SECRET are 
from your app page on Github.
"""

def make_keys():
    # Keymaker
    gk = emm.GithubKeymaker()
    gk.set_apikeys_env()
    gk.make_keys_from_strings(['bot1','bot2'], keys_out_dir='keys')

def run_flock():

    class BlameSheep(emm.Sheep):
        pass

    # Shepherd
    shepherd = emm.Shepherd(json_keys_dir='keys',
                            name='blame bot flock',
                            sheep_class=BlameSheep,
                            filehandler = False)
    #shepherd.perform_parallel_action('hello')

if __name__=="__main__":
    #make_keys()
    run_flock()
