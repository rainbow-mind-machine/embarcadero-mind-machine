# About embarcadero mind machine

**embarcadero mind machine (emm)** is a library for running Github bot flocks.
It is owned by the [rainbow-mind-machine](https://github.com/rainbow-mind-machine)
organization on Github.

Like all mind machines, **embarcadero mind machine** is simple and extensible.


## How is embarcadero mind machine simple?

The **mind machine framework** revolves around providing a few
simple components for building bot flocks:

* [Keymaker classes](mind-machine-docs/keymaker.md)
* [Shepherd classes](mind-machine-docs/shepherd.md)
* [Sheep classes](mind-machine-docs/sheep.md)

But it gets even simpler than that:
[boring-mind-machine](https://pages.charlesreid1.com/boring-mind-machine)
provides a [GithubKeymaker class](https://pages.charlesreid1.com/boring-mind-machine/bmm_keymaker_github/),
so that embarcadero mind machine can focus exclusively on Shepherd and Sheep
classes.

That's pretty simple!


## What does embarcadero mind machine extend or do?

embarcadero mind machine is **extensible** to keep bots from becoming boring.
There are a limited number of components to extend (2), these two components
have a simple and clear function call order, and embarcadero mind machine tries
to use sensible defaults.

That means we start out with bots that "just work" 
and we can incrementally improve, extend, override,
or redefine behaviors to make them increasingly complex,
while still abstracting away messy details.

See the [TwitterShepherd](rmm_shepherd.md) page or the
[TwitterSheep](rmm_sheep.md) or [SocialSheep](rmm_social_sheep.md)
page for examples.


## How is embarcadero mind machine POOP-y?

The embarcadero mind machine library makes good use of concepts in
Python Object Oriented Programming, or POOP.

The embarcadero mind machine library uses inheritance, because the entire
library is built on base classes provided by boring mind machine.

Additionally, the whole way embarcadero mind machine works is to
provide a set of useful classes, but also make it easy for
users to write their own classes.

Everything is about classes.





----


**rainbow mind machine** is an extensible framework for running Twitter bot flocks in Python.


That means we start out with bots that "just work" 
and we can incrementally improve, extend, override,
or redefine behaviors to make them increasingly complex,
while still abstracting away messy details.

See the [TwitterShepherd](rmm_shepherd.md) page or the
[TwitterSheep](rmm_sheep.md) or [SocialSheep](rmm_social_sheep.md)
page for examples.


