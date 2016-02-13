import httplib, json

class LoggerCouchDB(object):
    def constructor(self, opt):
        if 'endpoint' not in opt:
            raise ValueError('no endpoint specified!');
        if 'database' not in opt:
            raise ValueError('no database specified!');

        opt['auth'] = '';
        if 'username' in opt and 'password' in opt:
            opt['auth'] = opt['username']+":"+opt['password']+"@";
        self.params = opt;

    def log(self, message, opt = {}):
        datetime = opt['datetime'].strftime("%Y-%m-%d-%H-%M");
        message = {
            '_id':datetime+opt['botId'],
            'type':'log',
            'bot':opt['botId'],
            'timestamp':datetime,
            'message':message,
            'level':opt['level']
        };

        params = json.dumps(message)
        headers = {"Content-type": "application/json"}

        try:
            conn = httplib.HTTPConnection(self.params['auth']+self.params['endpoint'])
            conn.request("POST", "/"+self.params['database'], params, headers)
            response = conn.getresponse()
        except:
            print "OUPS";

export = LoggerCouchDB();



if __name__ == '__main__':
    from datetime import datetime;
    export.constructor({
        'endpoint':"db.spotlive.io",
        'database':'test'
    })
    export.log("hello", {
        "botId":"test",
        "level":"TEST",
        'datetime':datetime.today()
    });
