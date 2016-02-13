# the simplest logger we could do display message on stdout
class LoggerStdout:
    def constructor(self, opt):
        pass;

    def log(self, message, opt={}):
        print opt['datetime'].strftime("%Y-%m-%d %H:%M") +" "+opt['level'] +":\t "+message;

export = LoggerStdout();
