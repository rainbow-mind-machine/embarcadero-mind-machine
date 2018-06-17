# Sheep

The sheep defined by embarcadero mind machine have a lot of flexibility, 
primarily because of how many endpoints the Github API has.

Our first bot example was a blame bot: two bots going back and forth 
blaming each other for an issue by re-assigning the issue to the other bot.

Other bot flock ideas:

* bot making commits in repos
* license bot that looks for license files

be mroe generic about actions and what bots are doing

* not just "license bot to check for a license"
* that is the central action, which the bot defines how to do
* but we want to go deeper - a given bot type can do a given action type
* we want each bot to have a different "take" on the action, a different way of doing it


embarcadero mind machine Sheep have basic functionality described by the Github API.

Ideas:

* ping pong pair - simple ping pong on an issue (no, it's your problem. :reassign:)

* favestar bots
    - `to_fave = []; faved = [];`


