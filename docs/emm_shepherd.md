## Shepherd

The Shepherd is the object that loads the set of keys
and uses them to construct Sheep objects.

Inheritance notes:
- base class is in boring mind machine
- boring shepherd base class calls the verify key and the create sheep method
- virtual methods that must be implemente by us

Derived Shepherds only need to define:
- how to validate keys 
- how to add sheep to flock

As described in boring mind machine, any mind machine that
wants to use the boring shepherd base class should define 
two methods, each taking a key:

- validate the key
- create a Sheep from the key

