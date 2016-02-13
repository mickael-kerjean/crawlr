# the simplest logger we could do display message on stdout
class LoggerStdout:
    def constructor(self, opt):
        self.params = opt;

    def log(self, opt = {}):
        if 'message' in opt:
            print self.botId+":\t"+datetime+"-"+opt['message']
