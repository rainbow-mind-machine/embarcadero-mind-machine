import boringmindmachine as bmm
import os, json
from github import Github

class GithubKeymaker(bmm.BoringOAuthKeymaker):
    """
    Do the OAuth dance with Github.
    """
    def __init__(self):
        super().__init__('client_id','client_secret')


    # ---
    # Make Bot OAuth Keys

    def make_a_key( self, 
                    name, 
                    json_target,
                    keys_out_dir='keys/', 
                    interactive=True):
        """
        Public method to make a single key from a single item.

        If you make bots one item at a time, 
        you are bypassing the "normal" method of 
        creating multiple bots at a time (bot flock),
        so you must specify an item.

            name :          Label for the bot

            json_target :   The name of the target JSON file in which to
                            save this bot's OAuth key. 
                            (All paths are ignored.)

            keys_out_dir :  Directory in which to place final JSON keys
                            containing OAuth tokens and other bot info

            interactive :   Go through the interactive three-legged OAuth process
                            (only set to False for testing)
        """
        # OAuth endpoints given in the GitHub API documentation
        authorization_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'
        
        from requests_oauthlib import OAuth2Session
        github = OAuth2Session(client_id)
        
        # Redirect user to GitHub for authorization
        authorization_url, state = github.authorization_url(authorization_base_url)
        print("Go to the following URL and log in to authorize this application:")
        print("\t\t%s\n"%(authorization_url))
        
        # Get the authorization verifier code from the callback url
        redirect_response = raw_input('Paste the full redirect URL here:')
        
        # Fetch the access token
        github.fetch_token(token_url, client_secret=client_secret,
                authorization_response=redirect_response)
        
        # Fetch a protected resource, i.e. user profile
        r = github.get('https://api.github.com/user')
        print(r.content)

