## Github App

Common components:

* Client ID
* Client Secret
* Where to find them

## Summary

What this page covers:

* How to create/set up your app
* What information you need from your app to run the keymaker

## Create Github App

Create a Github application. There is only one thing you are
required to set, which is the callback URL.

Set the callback URL to `http://localhost:8000` (no HTTPS!).

Once you create your app, you should see a Client ID and a 
Client Secret near the top of the page. These two pieces of 
information are the API keys that the Keymaker needs to 
start the OAuth process.

## Get Client ID and Client Secret

Get your application's Client ID and Client Secret.
The eaiest way to set these for embarcadero mind machine
is to use environment variables. You can set the 
`CLIENT_ID` and `CLIENT_SECRET` variables to 
their respective values when you run embarcadero
mind machine scripts:

```
$ CLIENT_ID="XXX" CLIENT_SECRET="XXXXX" \
    python my_github_flock.py
```

The Keymaker can be configured to obtain the client 
API keys from these environment variables.

