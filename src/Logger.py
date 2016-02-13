# This guy instantiate a logger written as a plugin
# A logger plugin has 2 methods:
# - constructor to create the plugin
# - a log method that is used by this guy

from traceback import format_exception;
from random import choice, randrange;
from datetime import datetime;

class LoggerInterface(object):
    def constructor(self):
        pass;

    def log(self, message, opt):
        pass


class Logger(object):
    def __init__(self, opt):
        if 'plugin' not in opt:
            raise ValueError('no plugin selected');
        self.botId = self._pickAName();
        self.params = opt;
        self.logger = {};
        execfile("plugins/Logger_"+opt['plugin']+".py", self.logger);
        self.logger = self.logger['export']
        self.logger.constructor(self.params)


    def log(self, message, opt = {}):
        opt['original_message'] = message;
        opt['botId'] = self.botId;
        opt['datetime'] = datetime.today()

        if 'level' not in opt:
            opt['level'] = "INFO";

        if 'exception' in opt:
            exc_type, exc_value, exc_traceback = opt['exception'];
            lines = format_exception(exc_type, exc_value, exc_traceback)
            error = ''.join(' ' + line for line in lines)+"\n\n   ";
            message += error+"\n   ";

        self.logger.log(message, opt);

    def _pickAName(self):
        # taken from docker
        names = ["albattani","allen","almeida","archimedes","ardinghelli","aryabhata","austin","babbage","banach","bardeen","bartik","bassi","bell","bhabha","bhaskara","blackwell","bohr","booth","borg","bose","boyd","brahmagupta","brattain","brown","carson","chandrasekhar","colden","cori","cray","curie","darwin","davinci","dijkstra","dubinsky","easley","einstein","elion","engelbart","euclid","euler","fermat","fermi","feynman","franklin","galileo","gates","goldberg","goldstine","goldwasser","golick","goodall","hamilton","hawking","heisenberg","heyrovsky","hodgkin","hoover","hopper","hugle","hypatia","jang","jennings","jepsen","joliot","jones","kalam","kare","keller","khorana","kilby","kirch","knuth","kowalevski","lalande","lamarr","leakey","leavitt","lichterman","liskov","lovelace","lumiere","mahavira","mayer","mccarthy","mcclintock","mclean","mcnulty","meitner","meninsky","mestorf","minsky","mirzakhani","morse","murdock","newton","nobel","noether","northcutt","noyce","panini","pare","pasteur","payne","perlman","pike","poincare","poitras","ptolemy","raman","ramanujan","ride","ritchie","roentgen","rosalind","saha","sammet","shaw","shirley","shockley","sinoussi","snyder","spence","stallman","stonebraker","swanson","swartz","swirles","tesla","thompson","torvalds","turing","varahamihira","visvesvaraya","volhard","wescoff","williams","wilson","wing","wozniak","wright","yalow","yonath"];
        return choice(names)+str(randrange(10));


if __name__ == '__main__':
    import sys;
    log = Logger({
        'plugin':"stdout"
    });


    # It can track exceptions
    try:
        a = 4 / 0;
    except:
        log.log("oups", {
            'exception':sys.exc_info(),
            'level':"ERROR"
        });

    # and obviously text:
    log.log("hello there!")
    log.log("hello there!", {'level':"DEBUG"})
