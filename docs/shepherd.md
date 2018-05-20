## Shepherd

The embarcadero mind machine shepherd is not much different from 
your typical shepherd, it's basically there to initialize the 
flock by creating one sheep per key.

As described in boring mind machine, any mind machine that
wants to use the boring shepherd base class should define 
two methods, each taking a key:

- validate the key
- create a Sheep from the key

