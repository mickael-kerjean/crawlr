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

from src.Backend import Backend
from src.Logger import Logger
from src.Browser import Browser

class Crawlr():
    def __init__(self, opt ={}):
        opt = self.__initializeOptions(opt)
        print opt['browser']
        self.browser = Browser(opt['browser']);
        self.backend = Backend(opt['backend']);
        self.logger = Logger(opt['logger']);

    def __del__(self):
        pass
        # del self.browser;
        # del self.backend;
        # del self.notify;

    def __initializeOptions(self, opt):
        if 'browser' not in opt:
            opt['browser'] = {
                'browser':'chrome',
                'resolution':{
                    'width':'800',
                    'height':'800'
                }
            };
        if 'backend' not in opt:
            opt['backend'] = {
                'plugin':'csv',
                'filename':'db.csv',
                'path':'./'
            }
        if 'logger' not in opt:
            opt['logger'] = {
                'plugin':'stdout',
            }
        return opt;

if __name__ == '__main__':
    crawl = Crawlr({
        'browser':{
            "browser":"firefox"
        }
    });
    import time;
    crawl.logger.log("let's get started")
    crawl.browser.go('http://google.com')
    crawl.browser.write("input.gsfi", "nyan cat video", {
        'thenPressEnter':True,
        'thenDisappear':True,
        'thenWait':"#ires h3 a",
    });
    crawl.browser.click("#ires h3 a", {
        'thenDisappear':True,
        'thenWait':"#masthead-search-term"
    })
    crawl.logger.log("LA LA LALALALALA LA LA")
    time.sleep(30)
