import boringmindmachine as bmm
from .GithubSheep import GithubSheep

from .utils import eprint

class GithubShepherd(bmm.BoringShepherd):
    """
    Derived Shepherds only need to define:
    - how to validate keys 
    - how to add sheep to flock
    """
    def __init__(self, 
                 json_keys_dir, 
                 sheep_class = GithubSheep, 
                 **kwargs):
        """
        This constructor calls the Boring Shepherd constructor.

            json_keys_dir:  Directory where Sheep API keys are located

            sheep_class:    Type of Sheep

            kwargs:         Parameters passed on to the Sheep
        """
        super().__init__(
                json_keys_dir, 
                sheep_class=sheep_class, 
                **kwargs
        )

    def _validate_key(self, bot_key, **kwargs):
        """
        Validate the Github keys made by the Keymaker
        """
        required_keys = ['client_id',
                         'client_secret',
                         'token',
                         'login']
        for key in required_keys:
            if key not in bot_key.keys():
                err = "ERROR: GithubShepherd encountered an invalid bot key.\n"
                err += "The bot key is missing a value for '%s'."%(key)
                raise Exception(err)

    def _create_sheep(self, bot_key, **kwargs):
        sheep = self.sheep_class(bot_key, **kwargs)
        self.flock.append(sheep)

