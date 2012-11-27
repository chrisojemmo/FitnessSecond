'''
Created on 17 Nov 2012

@author: chris
'''

import os
thisdir = os.path.dirname(__file__)


from backend.interface import Interface
import cherrypy

class FitnessSecond(object):
    '''
    this is the web interface to FitnessSecond
    '''

    def __init__(self):
        '''
        inits the backend database
        '''
        self.database = Interface()
        print "Loaded database"

    def index(self):
        user = self.database.get_user("chris", ["info"])
        output = ("<p>Name: %s<p>Info: %s" % ("chris", user["info"]))
        return output

    index.exposed = True

    
cherrypy.tree.mount(FitnessSecond())


if __name__ == '__main__':
    cherrypy.quickstart(config=os.path.join(thisdir, 'tutorial.conf'))
