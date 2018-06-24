import embarcaderomindmachine as emm
import random, time
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

"""
In this file we define a custom Sheep class:
BlameSheep, github bots that detect when an
issue is assigned to them, assign it to someone
else, and point the finger in a comment.
The flock argues back and forth forever...
"""

class BlameSheep(emm.GithubSheep):


    def be_stupid(self,**kwargs):
        """
        Read parameters, set up the blame game,
        then run the forever-loop where the bots
        blame other bots and make excuses forever.
        """

        if 'org' not in kwargs and 'user' not in kwargs:
            err = "ERROR: no 'org' or 'user' specified for BlameSheep."
            raise Exception(err)

        if 'repo' not in kwargs:
            err = "ERROR: no 'repo' specified for BlameSheep."
            raise Exception(err)
        
        if 'issueno' not in kwargs:
            err = "ERROR: no 'issueno' specified for BlameSheep."
            raise Exception(err)

        if 'delay' not in kwargs:
            err = "ERROR: no 'delay' specified for BlameSheep."
            raise Exception(err)

        g = self.api
        blame_map = {   
            'rainbowmindmachine' : 'embarcaderomindmachine',
            'embarcaderomindmachine' : 'rainbowmindmachine' 
        }

        
        # Store self/other
        # (both login string and Github User object)
        whoami_name = self.name
        whoami = g.get_user(whoami_name)

        whoarethey_name = blame_map[whoami_name]
        whoarethey = g.get_user(whoarethey_name)

        blame_messages = []
        with open('blame_messages.txt','r') as f:
            blame_messages = f.readlines()

        if 'org' in kwargs:
            owner = g.get_organization(kwargs['org']).get_repo(kwargs['repo'])
        elif 'user' in kwargs:
            owner = g.get_user(kwargs['user']).get_repo(kwargs['repo'])
        else:
            raise Exception("ERROR: neither 'org' nor 'user' in kwargs")


        issueno = kwargs['issueno']

        while True:

            # important to do this INSIDE the loop!
            iss = owner.get_issue(issueno)

            listocomments = list(iss.get_comments())

            if len(listocomments)<=2:
                # The blame game has not yet kicked off.
                # We get to start it!
                iss.edit(assignees=[whoarethey])
                self.tprint('[@%s] changed assignees to @%s'%(whoami_name, whoarethey_name))

                comment = "It wasn't me, it was @%s"%(whoarethey_name)
                iss.create_comment(comment)
                self.tprint('[@%s] %s'%(whoami_name, comment))

            else:

                # The blame game is afoot.
                # If the issue is assigned to us,
                # reassign it and come up with an excuse.

                if(iss.assignee.login == whoami_name):
                    # The issue is assigned to us.
                    # Take evasive action.
                    self.tprint("[@%s] current assignee is us: %s"%(whoami_name,iss.assignee.login))

                    comment = "It wasn't me, it was @%s"%(whoarethey_name)
                    self.tprint('[@%s] %s'%(whoami_name, comment))

                    self.tprint('----8<----- starting create_comment() call')
                    iss.create_comment(comment)
                    self.tprint('----8<----- finished create_comment() call')

                    self.tprint('----8<----- starting edit(assignees=...) call')
                    iss.edit(assignees=[whoarethey])
                    self.tprint('----8<----- finished edit(assignees=...) call')

                elif(iss.assignee.login == whoarethey_name):
                    # Our work here is done.
                    self.tprint("[@%s] current assignee is them: %s"%(whoami_name,iss.assignee.login))


            naptime = random.randint(1,10) + delay_time

            time.sleep(naptime)




    def blame(self,**kwargs):
        """
        Two bots blaming each other for breaking the build.

        kwargs:

            (org|user) :    The organization or user owning the argument repo
            repo :          The repository in which to begin an issues argument
            issueno :       The issue number in the specified repo in which to argue
            delay :         Approximate delay time (seconds, whole numbers) between arguments
        """
        if 'org' not in kwargs and 'user' not in kwargs:
            err = "ERROR: no 'org' or 'user' specified for BlameSheep."
            raise Exception(err)

        if 'repo' not in kwargs:
            err = "ERROR: no 'repo' specified for BlameSheep."
            raise Exception(err)
        
        if 'issueno' not in kwargs:
            err = "ERROR: no 'issueno' specified for BlameSheep."
            raise Exception(err)

        if 'delay' not in kwargs:
            err = "ERROR: no 'delay' specified for BlameSheep."
            raise Exception(err)

        g = self.api
        blame_map = {   
                'rainbowmindmachine' : 'embarcaderomindmachine',
                'embarcaderomindmachine' : 'rainbowmindmachine' 
        }

        whoami_name = self.name
        whoami = g.get_user(whoami_name)

        whoarethey_name = blame_map[whoami_name]
        whoarethey = g.get_user(whoarethey_name)

        blame_messages = []
        with open('blame_messages.txt','r') as f:
            blame_messages = f.readlines()

        delay_time = int(kwargs['delay'])

        # Structure:
        # Sleep 
        # Blame someone else

        # Start with a little nap so we aren't racing
        self.tprint("Custom Sheep: taking a quick nap, brb.")
        time.sleep(random.randint(1,10))
        self.tprint("Custom Sheep: okay WB.")

        if 'org' in kwargs:
            emm = g.get_organization(kwargs['org']).get_repo(kwargs['repo'])
        elif 'user' in kwargs:
            emm = g.get_user(kwargs['user']).get_repo(kwargs['repo'])
        else:
            raise Exception("ERROR: neither 'org' nor 'user' in kwargs")

        issueno = kwargs['issueno']
        iss = emm.get_issue(issueno)

        while True:

            listocomments = list(iss.get_comments())

            if len(listocomments)<=2:

                # The blame game has not yet kicked off.
                # We get to start it!

                comment = "It wasn't me, it was @%s"%(whoarethey_name)
                #iss.edit(assignees=[whoarethey])
                self.tprint('[@%s] changed assignees to @%s'%(whoami_name, whoarethey_name))
                #iss.create_comment(comment)
                self.tprint('[@%s] %s'%(whoami_name, comment))

            else:

                # If the issue is assigned to us,
                # reassign it and come up with an excuse.
                if(iss.assignee.login == whoami_name):

                    #iss.edit(assignees=[whoarethey])
                    self.tprint('[@%s] changed assignees to %s'%(whoami_name, whoarethey_name))
                    #comment = blame_messages[random.randint(0,len(blame_messages)-1)].format(blame=whoarethey_name)
                    #iss.create_comment(comment)
                    self.tprint('[@%s] %s'%(whoami_name, comment))

            # Now sit back and take a nap
            # while the other bot does all 
            # the hard work.
            time.sleep(random.randint(1,delay_time))

if __name__=="__main__":
    print("Run two_bot.py instead")
