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

        # NOTE: This assumes you have set up your webapp
        # to have a callback url of `localhost:8000`
        #
        # This is going to get a bit complicated.
        # Here's what we do:
        # 
        # get set up:
        # - create custom handler class to pull out the parameters we need
        # 
        # oauth process
        # - request an oauth URL from github
        # - run an http server with our custom handler and wait
        # - user visits URL and logs in
        # - user is redirected to localhost
        # - custom handler extracts params, shows ok, and dies

        from urllib.parse import urlparse, parse_qsl
        from http.server import HTTPServer, BaseHTTPRequestHandler

        # This is what we're after:
        query_params = []

        # Start with the custom handler class

        class MyHandler(BaseHTTPRequestHandler):
        
            def do_GET(self):
                url = urlparse(self.path)

                #q = parse_qsl(url.query)
                #with open('/tmp/query','a') as f:
                #    f.write('%s\n'%(q))

                query_params = parse_qsl(url.query)
        
                #send code 200 response
                self.send_response(200)
        
                #send header first
                self.send_header('Content-type','text-html')
                self.end_headers()
        
                #send file content to client
                self.wfile.write(str.encode("<html><body><h1>Success!</h1></body></html>"))
                f.close()
        
                return

        from requests_oauthlib import OAuth2Session
        github = OAuth2Session(client_id)

        # OAuth endpoints given in the GitHub API documentation
        authorization_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'
        
        # Redirect user to GitHub for authorization
        authorization_url, state = github.authorization_url(authorization_base_url)
        print("Go to the following URL and log in to authorize this application:")
        print("\t\t%s\n"%(authorization_url))

        # Now run a server with the custom handler
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.handle_request()

        print(query_params)

        ### # Fetch the access token
        ### github.fetch_token(token_url, client_secret=client_secret,
        ###         authorization_response=redirect_response)
        ### 
        ### # Fetch a protected resource, i.e. user profile
        ### r = github.get('https://api.github.com/user')
        ### print(r.content)

