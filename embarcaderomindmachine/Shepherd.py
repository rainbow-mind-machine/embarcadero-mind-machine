import boringmindmachine as bmm

class Shepherd(bmm.BoringShepherd):
    """
    Derived Shepherds only need to define:
    - how to validate keys 
    - how to add sheep to flock
    """
    def __init__(self, 
                 json_keys_dir, 
                 name,
                 sheep_class=bmm.BoringSheep, 
                 **kwargs):
        # This constructor is not strictly necessary,
        # it is mainly here to show the method signature.
        # We don't do anything extra in this constructor.
        super().__init__(json_keys_dir, name, sheep_class, **kwargs)

    def _validate_key(self, bot_key):
        # bot key for each sheep for github 
        # needs to be a json file with keys:
        # - username
        # - oauth_token
        # - oauth_secret
        # - client_id
        # - client_secret
        # These are Github-specific
        if 'name' not in bot_key.keys():
            err = "ERROR: Shepherd found invalid key, "
            err += "missing bot name"
            raise Exception(err)

        keys = ['name','token']
        for key in keys:
            if key not in bot_key:
                err = "ERROR: Shepherd found invalid key "
                err += "for bot %s"%(bot_key['name'])
                raise Exception(err)


    def _create_sheep(self, bot_key):
        sheep = self.sheep_class(bot_key)
        self.flock.append(sheep)


