import embarcaderomindmachine as emm
from unittest import TestCase
from nose.tools import raises
import os, subprocess, json
import tempfile
from .utils import captured_output


"""
Classes to test emm.Keymaker
"""


thisdir = os.path.abspath(os.path.dirname(__file__))


class TestGithubKeymaker(TestCase):
    """
    This currently tests:
    - constructor 
    - API key init mechanisms
    """
    token_var = 'client_id'
    secret_var = 'client_secret'
    keys_dir = tempfile.gettempdir()
    keys_json = "apikeys.json"

    @classmethod
    def setUpClass(self):
        """
        Set up JSON file for JSON key-loading method
        """
        self.api_keys = os.path.join(keys_dir, keys_json)
        subprocess.call(['mkdir','-p',keys_dir])

        d = {}
        d[self.ct.lower()] = 'AAAAA'
        d[self.cts.lower()] = 'BBBBB'
        with open(self.api_keys,'w') as f:
            json.dump(d,f)


    def test_githubkeymaker_constructor(self):
        """
        Running a smoke test for the GithubKeymaker class
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)


    def test_githubkeymaker_apikeys_env(self):
        """
        Testing ability to create single key using consumer token from environment vars
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)

        # Set application API keys
        os.environ['CLIENT_ID'] = 'CCCCC'
        os.environ['CLIENT_TOKEN'] = 'DDDDD'

        keymaker.set_apikeys_env()

        self.assertEqual(bk.credentials[self.token_var.lower()], 'CCCCC')
        self.assertEqual(bk.credentials[self.secret_var.lower()],'DDDDD')

        # Clean up
        os.environ['CLIENT_ID'] = ''
        os.environ['CLIENT_TOKEN'] = ''


    def test_githubkeymaker_apikeys_file(self):
        """
        Testing ability to create single key using consumer token/secret from JSON file
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)

        bk.set_apikeys_file(self.api_keys)

        # Note that we hard-code these key values in the setup method above...
        self.assertEqual(bk.credentials[self.token_var.lower()], 'AAAAA')
        self.assertEqual(bk.credentials[self.secret_var.lower()],'BBBBB')


    def test_githubkeymaker_apikeys_dict(self):
        """
        Testing ability to create single key using consumer token/secret from dictionary
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)

        # Set application API keys
        keymaker.set_apikeys_dict({ 
            self.token_var.lower() : 'EEEEE',
            self.secret_var.lower() : 'FFFFF'
        })

        self.assertEqual(bk.credentials[self.token_var.lower()], 'EEEEE')
        self.assertEqual(bk.credentials[self.secret_var.lower()],'FFFFF')


    @classmethod
    def tearDownClass(self):
        # Remove the keys directory we created
        subprocess.call(['rm','-rf',self.keys_dir])



