import embarcaderomindmachine as emm
gk = emm.GithubKeymaker()
gk.set_apikeys_env()
gk.make_a_key('dummy','dummy.json','/tmp/keys')

