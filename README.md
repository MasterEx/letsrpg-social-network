#README

###What is letsrpg?

letsrpg is a social network for role playing gamers

It'll be implemented in Python - Django with SQLite3

###Why?

letsrpg is an implementation of a social network for our 
class "development and implementation of IT systems"

Previous design steps can be found in Greek here:

 * [Step 1](https://docs.google.com/document/pub?id=19oVeNSMEer0Vi1SrpXwtIwaFSB381k-fR4rb5g7CaS8)
 * [Step 2](https://docs.google.com/document/pub?id=1ZYNCbqMQXp1kzf2Il7msWlSiY6jq8_rYBEW0_DuSAvk)
 * [Step 3](https://docs.google.com/document/pub?id=1MIYySAnjli2_5XIazbda0aEzuMjaGtaQrRaPFD8ICWI)

###Applications Structure

Each entity described in step 2 will be a django model in it's own application.
Exception is User and Profile entities that will be placed in an app named "account"
and Event and Event-Player entities that will be placed in an app named "event".

account
    |-User
    |-Profile
event
    |-Event
    |-Event-Player
follows
rate
abuse-report
messages
ads