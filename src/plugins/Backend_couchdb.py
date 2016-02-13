import httplib, json
import pdb;
class BackendCouchDB(object):
    def constructor(self, opt):
        if 'endpoint' not in opt:
            raise ValueError('no endpoint specified!');
        if 'database' not in opt:
            raise ValueError('no database specified!');

        opt['auth'] = '';
        if 'username' in opt and 'password' in opt:
            opt['auth'] = opt['username']+":"+opt['password']+"@";

        opt['headers'] = {"Content-type": "application/json"}
        self.params = opt;

    def alreadyExist(self, key_value):
        print "/"+self.params['database']+"/"+key_value
        conn = httplib.HTTPConnection(self.params['auth']+self.params['endpoint'])
        conn.request("GET", "/"+self.params['database']+"/"+key_value)
        response = conn.getresponse()
        if response.status == 200:
            return True
        else:
            return False

    def put(self, key, obj):
        obj['_id'] = key;
        obj = json.dumps(obj)
        try:
            conn = httplib.HTTPConnection(self.params['auth']+self.params['endpoint'])
            conn.request("POST", "/"+self.params['database'], obj, self.params['headers'])
        except:
            print "OUPS";

export = BackendCouchDB();


if __name__ == '__main__':
    from datetime import datetime;
    export.constructor({
        'endpoint':"db.spotlive.io",
        'database':'test'
    })
    export.put('tesID', {
        "botId":"test",
        "level":"TEST",
        'datetime':datetime.today().strftime('%Y')
    });

    if export.alreadyExist('testID') != True:
        raise ValueError('euh, you miss it, it already exist');
