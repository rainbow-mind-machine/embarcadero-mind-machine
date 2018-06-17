# Github Keymaker

embarcadero mind machine defines a Keymaker object for authenticating
with the Github API via OAuth.

## A Quick One-Bot Example

Here is a quick demo to authenticate a bot account
and create a JSON key:

**`examples/quick_start/one_bot.py`**

```
import embarcaderomindmachine as emm
gk = emm.GithubKeymaker()
gk.set_apikeys_env()
gk.make_a_key('dummy','dummy.json','/tmp/keys')
```

The Github Keymaker object is what walks you through
the OAuth2 process.

The `gk.set_apikeys_env()` method gets the application's
consumer ID and consumer secret from environment
variables (`CONSUMER_ID` and `CONSUMER_SECRET`, 
respectively). The Keymaker also has methods to set
the API keys from a JSON file or from a dictionary.

Last, we run the `make_a_key()` method to actually
generate the key. Note that this is not the normal
workflow, we usually pass a list of items to the 
Keymaker and ask it to generate one key (i.e., 
authenticate one bot account) per item.

In this case, we force the Keymaker to create a 
single key named "dummy" that will be stored in
`/tmp/keys/dummy.json`.

## A Two-Bot Example







