import boringmindmachine as bmm
import os, json
import tempfile
from github import Github

class GithubKeymaker(bmm.BoringOAuthKeymaker):
    """
    Do the OAuth dance with Github.
    """
    def __init__(self):
        super().__init__('client_id','client_secret')


    # ---
    # Make Bot OAuth Keys

    # Bulk Key Methods:
    # These all call the single key method.

    def make_keys_from_dict(self, d):
        """
        Items correspond to key-value pairs in a dictionary.
        The key is the bot name, the value is the json target file.
        """
        for name in d.keys():
            json_target = d[name]
            make_a_key(name, json_target)


    # Single Key Method:
    # The workhorse.

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
        if os.path.isdir(keys_out_dir) is False:
            subprocess.call(['mkdir','-p',keys_out_dir])

        # Here is where we build logic in to make this 
        # behave gracefully.
        # 
        # If we are passed a json_target that is not .json:
        # - if no extension, add a .json extension and use as json target
        # - if extension, replace extension with .json and use as json target
        # 
        # That way, we can use this as a files keymaker too
        # 
        _, ext = os.path.splitext(json_target)
        if(ext == ''):
            json_target = json_target + ".json"
        elif(ext == '.json'):
            pass
        else:
            json_target = re.sub(ext,'.json',json_target)

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

        # This is where we stash it:
        callback_file = 'callback_token.json'

        # Start with the custom handler class

        class MyHandler(BaseHTTPRequestHandler):
        
            def do_GET(self):
                url = urlparse(self.path)

                ### # just save the whole chunka text
                ### to_save = url #.query
                ### tempf = os.path.join(tempfile.gettempdir(),callback_file)
                ### print(type(url))
                ### import pdb; pdb.set_trace()
                ### with open(tempf,'w') as f:
                ###     print(url,file=f)

                tempf = os.path.join(tempfile.gettempdir(),callback_file)
                with open(tempf,'w') as f:
                    print(self.path,file=f)
                
                # send code 200 response
                self.send_response(200)
        
                # send header first
                self.send_header('Content-type','text-html')
                self.end_headers()
        
                # send file content to client
                self.wfile.write(str.encode("<html><body><h1>Success!</h1></body></html>"))
        
                return 

        from requests_oauthlib import OAuth2Session
        github = OAuth2Session(self.credentials[self.token])

        import pdb; pdb.set_trace()

        # OAuth endpoints given in the GitHub API documentation
        authorization_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'

        # Redirect user to GitHub for authorization
        authorization_url, state = github.authorization_url(authorization_base_url)
        print("Go to the following URL and log in to authorize this application:")
        print("\t\t%s\n"%(authorization_url))

        # Now run a server with the custom handler
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, MyHandler)
        httpd.handle_request()

        # Allow for an HTTP callback
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
        with open( os.path.join(tempfile.gettempdir(), callback_file), 'r') as f:
            callback_token = f.read()

        BASE = 'http://localhost:8000'
        redirect_response = BASE + callback_token.strip()

        print('redirect response url:')
        print(redirect_response)

        print("state:")
        print(state)

        github = OAuth2Session(self.credentials[self.token], state=state)

        # now use the callback token to receive the oauth token
        github.fetch_token(token_url,
                           client_secret = self.credentials[self.secret],
                           verify = False,
                           authorization_response = redirect_response)

        # Fetch a protected resource, i.e. user profile
        r = github.get('https://api.github.com/user')
        print(r.content)



