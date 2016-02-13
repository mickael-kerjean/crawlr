# this class gather all the features together to get one single common api
# for all our needs
#
# The main idea is to create plugable anything
# the backend make use of any plugin as request by the opt
# same for the notifier
#
#
# The apis are defined in the Backend and Notifier class
# The Browser class is only here to give a convenient api for selenium
#

from Backend import Backend
from Logger import Logger
from Browser import Browser

class Crawlr():
    def __init__(self, opt ={}):
        if 'browser' not in opt:
            opt['browser'] = "firefox";
        if 'backend' not in opt:
            opt['backend'] = {
                'type':'file',
                'opt':{
                    'filename':'db.csv'
                }
            }
        if 'logger' not in opt:
            opt['logger'] = {
                'backend':{
                    'type':'couchdb',
                    'opt':{
                        'endpoint':'db.spotlive.io',
                    }
                },
                'screenshot':{
                    'endpoint':'bot.spotlive.io'
                }
            }

        self.browser = Browser(opt['browser']);
        self.backend = Backend(opt['backend']);
        self.logger = Notifier(opt['logger']);

    def __del__(self):
        del self.browser;
        del self.backend;
        del self.notify;

if __name__ == '__main__':
    crawl = Crawlr();
