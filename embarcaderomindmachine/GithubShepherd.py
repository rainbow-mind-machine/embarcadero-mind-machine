import boringmindmachine as bmm

class GithubShepherd(bmm.BoringShepherd):
    """
    Derived Shepherds only need to define:
    - how to validate keys 
    - how to add sheep to flock
    """

    def _validate_key(self, bot_key, **kwargs):
        """
        Validate the Github keys made by the Keymaker
        """
        required_keys = ['client_id',
                         'client_secret',
                         'oauth_token',
                         'oauth_secret',
                         'username']
        for key in required_keys:
            if key not in bot_key.keys():
                err = "ERROR: Shepherd encountered an invalid bot key.\n"
                err += "The bot key is missing a value for '%s'."%(key)
                raise Exception(err)

    def _create_sheep(self, bot_key, **kwargs):
        sheep = self.sheep_class(bot_key, **kwargs)
        self.flock.append(sheep)

