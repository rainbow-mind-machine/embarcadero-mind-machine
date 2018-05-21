from github import Github

class Sheep(object):
    """
    Sheep are created by the Shepherd.

    Sheep are initialized with a JSON key file plus parameters from the Shepherd.

    Sheep are expected to take care of their own API instance.
    """
    def __init__(self, bot_key, **kwargs):

        # Initialize your API instance
        g = github.Github(oauth_token)



