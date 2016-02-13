import httplib, json

class LoggerCouchDB(object):
    def constructor(self, opt):
        self.params = opt;

    def log(self, opt = {}):
        params = json.dumps(message)
        headers = {"Content-type": "application/json"}
        try:
            conn = httplib.HTTPConnection("db.spotlive.io")
            conn.request("POST", "/logs", params, headers)
            response = conn.getresponse()
        except:
            pass


        filename = './log/'+datetime.datetime.today().strftime("%Y-%m-%d-%H-%M")+"_"+self.id;
        if 'message' in opt:
            message = {
                '_id':t[1]+"-"+t[0],
                'type':'log',
                'bot':t[0],
                'timestamp':t[1],
                'message':t[2],
                'level':opt['level']
            };
            Couch().put(message)
