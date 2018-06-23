import boringmindmachine as bmm
from github import Github
import time, random

from .utils import eprint

class GithubSheep(bmm.BoringSheep):
    """
    Sheep are created by the Shepherd.
    Sheep are initialized with a JSON key file plus parameters from the Shepherd.
    Sheep are expected to take care of their own API instance.
    """
    def __init__(self, bot_key, **kwargs):

        # Initialize your API instance
        self.api = Github(bot_key['token']['access_token'])
        self.params = bot_key

        # the bot's handle
        self.name = bot_key['name']

        # the bot's official login/username
        self.login = bot_key['login']

        # No kwargs used.

    def hello(self):
        time.sleep(random.randint(1,10))
        msg = "GithubSheep: Hello world! This is bot %s (login %s)"%(self.name, self.login)
        eprint(msg)

