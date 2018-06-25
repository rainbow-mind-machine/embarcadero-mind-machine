# Quick Start

Let's walk through a quick example to illustrate
how **embarcadero mind machine** (emm) works.

We only have 3 objects we need to understand:

* [The Keymaker](emm_keymaker.md) (makes/manages keys and authenticates with Twitter)
* [The Shepherd](emm_shepherd.md) (runs the flock; one shepherd = one bot flock)
* [The Sheep](emm_sheep.md) (runs a bot, and defines bot's behavior; one sheep = one bot)

# Keymaker: Authentication Step

Also see the [Keymaker](emm_keymaker.md) page.

The first step in embarcadero mind machine is to run the Keymaker
to give the application permission to tweet on behalf of 
each of our bot users. This generates keys that the 
embarcadero mind machine application requires to run a bot flock.

The actual Keymaker objects for each service are defined in the
[boring mind machine](https://pages.charlesreid1.com/boring-mind-machine) library.
The usage is covered here.

The Keymaker takes a set of items as an input, and creates one key for each item. 

A set of items might be a Python list with integers, or a folder full of 
text files, or a set of URLs, or just plain old string labels.

The keys are what allow our application to tweet using a bot account. 

We call `make_a_key()` on each item to create each key.

The Keymaker _requires_ that we specify
a `name` parameter to name the bot and a `json` parameter
to specify the location of the key.

Also note, this requires that your Twitter app's 
consumer secret and consumer token be set 
in `apikeys.py`.

In the example below, the "items" are strings containing the bot name.
This uses credentials in `apikeys.py` and outputs key files
at `keys/key1.json` and `keys/key2.json`.

```python
import embarcaderomindmachine as rmm
import subprocess

subprocess.call(['mkdir','-p','keys/'])

k = rmm.GithubKeymaker()
k.set_api_keys_env()

# Create some keys
k.make_key({
    'name':'red bot',          # This is the bot label (arbitrary)
    'json':'keys/red_key.json' # This is the key file
})
k.make_key({
    'name':'blue bot',
    'json':'keys/key2.json'
})
```

When this script is run, the Keymaker will 
go through a series of interactive steps 
to create keys from each item.

# A Shepherd to Run the Bot Flock

Also see the [Shepherd](emm_shepherd.md) page.

Once that is done, make a Shepherd for the bot flock,
and point it to the keys the Keymaker created 
in the `keys/` directory:

```python
import embarcaderomindmachine as rmm

# make the Shepherd
sh = rmm.GiihubShepherd("keys/")

# Perform action in serial
sh.perform_serial_action('change_avatar')

# Perform action in parallel
sh.perform_serial_action('issue_argument')
```

# Customizing Sheep

Also see the [Sheep](emm_sheep.md) page.

We didn't specify what kind of Sheep we want 
the Shepherd to create, so the Shepherd uses
the default `Sheep` class.

To change the behavior of your bot,
you can use built-in Sheep types
or you can extend the `Sheep` class
to define custom behaviors. 

# More Examples

See the [`examples/`](/examples) directory.


