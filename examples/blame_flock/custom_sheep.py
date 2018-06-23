import embarcaderomindmachine as emm
import random, time


#########################################
# here, we define a custom Sheep class:
# BlameSheep, github bots that blame
# each other for an issue and re-assign
# the issue back and forth..
class BlameSheep(emm.Sheep):
    def blame(self,**kwargs):
        """
        Two bots blaming each other for breaking the build.
        """
        if 'org' not in kwargs and 'user' not in kwargs:
            err = "ERROR: no 'org' or 'user' specified for BlameSheep."
            raise Exception(err)

        if 'repo' not in kwargs:
            err = "ERROR: no 'repo' specified for BlameSheep."
            raise Exception(err)
        
        if 'issueno' not in kwargs:
            err = "ERROR: no 'issueno' specified for BlameSHeep."
            raise Exception(err)

        g = self.api
        blame_map = {   'rainbowmindmachine' : 'embarcaderomindmachine',
                        'embarcaderomindmachine' : 'rainbowmindmachine' 
                    }

        whoami_name = self.name
        whoami = g.get_user(whoami_name)

        whoarethey_name = blame_map[whoami_name]
        whoarethey = g.get_user(whoarethey_name)

        blame_messages = []
        with open('blame_messages.txt','r') as f:
            blame_messages = f.readlines()

        # Structure:
        # Sleep 
        # Blame someone else

        # Start with a little nap so we aren't racing
        time.sleep(10*random.randint(4,8))

        # To start with, we'll hard-code the issue.
        # rainbow-mind-machine/embarcadero-mind-machine/#1
        if 'org' in kwargs:
            emm = g.get_organization(kwargs['org']).get_repo(kwargs['repo'])
        elif 'user' in kwargs:
            emm = g.get_organization(kwargs['user']).get_repo(kwargs['repo'])
        issueno = kwargs['issueno']
        iss = emm.get_issue(issueno)

        while True:

            listocomments = list(iss.get_comments())
            if len(listocomments)<=2:
                # The blame game has not yet kicked off.
                # We get to start it!
                comment = "It wasn't me, it was @{blame}".format(blame=whoarethey.login)
                iss.edit(assignees=[whoarethey])
                print('[@%s] changed assignees to @%s'%(whoami_name, whoarethey_name))
                iss.create_comment(comment)
                print('[@%s] %s'%(whoami_name, comment))

            else:
                iss.edit(assignees=[whoarethey])
                print('[@%s] changed assignees to %s'%(whoami_name, whoarethey.login))
                comment = blame_messages[random.randint(0,len(blame_messages)-1)].format(blame=whoarethey_name)
                iss.create_comment(comment)
                print('[@%s] %s'%(whoami_name, comment))

            # Now sit back and take a nap
            # while the other bot does all 
            # the work.
            time.sleep(60*random.randint(4,8))