import embarcaderomindmachine as emm
from unittest import TestCase
from nose.tools import raises
import os, subprocess, json
import tempfile


"""
Classes to test emm.GithubKeymaker
"""


class TestGithubKeymaker_init(TestCase):
    """
    This currently tests:
    - constructor 
    - API key init mechanisms
    """
    token_var = 'client_id'
    secret_var = 'client_secret'
    keys_dir = tempfile.gettempdir() # gets an already-existing dir
    keys_json = "apikeys_fake.json"

    @classmethod
    def setUpClass(self):
        """
        Set up JSON file for JSON key-loading method
        """
        self.keypath = os.path.join(self.keys_dir, self.keys_json)

        d = {}
        d[self.token_var.lower()] = 'AAAAA'
        d[self.secret_var.lower()] = 'BBBBB'
        with open(self.keypath,'w') as f:
            json.dump(d,f)


    def test_githubkeymaker_constructor(self):
        """
        Running a smoke test for the GithubKeymaker class
        """
        gk = emm.GithubKeymaker()


    def test_githubkeymaker_apikeys_env(self):
        """
        Testing ability to create single key using consumer token from environment vars
        """
        gk = emm.GithubKeymaker()

        # Set application API keys
        os.environ['CLIENT_ID'] = 'CCCCC'
        os.environ['CLIENT_SECRET'] = 'DDDDD'

        gk.set_apikeys_env()

        self.assertEqual(gk.credentials[self.token_var.lower()], 'CCCCC')
        self.assertEqual(gk.credentials[self.secret_var.lower()],'DDDDD')

        # Clean up
        os.environ['CLIENT_ID'] = ''
        os.environ['CLIENT_SECRET'] = ''


    def test_githubkeymaker_apikeys_file(self):
        """
        Testing ability to create single key using consumer token/secret from JSON file
        """
        gk = emm.GithubKeymaker()

        gk.set_apikeys_file(self.keypath)

        # Note that we hard-code these key values in the setup method above...
        self.assertEqual(gk.credentials[self.token_var.lower()], 'AAAAA')
        self.assertEqual(gk.credentials[self.secret_var.lower()],'BBBBB')


    def test_githubkeymaker_apikeys_dict(self):
        """
        Testing ability to create single key using consumer token/secret from dictionary
        """
        gk = emm.GithubKeymaker()

        # Set application API keys
        gk.set_apikeys_dict({ 
            self.token_var.lower() : 'EEEEE',
            self.secret_var.lower() : 'FFFFF'
        })

        self.assertEqual(gk.credentials[self.token_var.lower()], 'EEEEE')
        self.assertEqual(gk.credentials[self.secret_var.lower()],'FFFFF')


    @classmethod
    def tearDownClass(self):
        # remove key
        subprocess.call(['rm','-rf',self.keypath])


class TestGithubKeymaker_keymaking(TestCase):
    """
    This tests:
    - make_a_key

    You must use environment variables to set real API keys.
    """
    def test_make_a_key(self):
        pass









