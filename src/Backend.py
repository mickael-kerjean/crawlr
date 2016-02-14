# This guy is our backend. He can:
# - check if an entry already exist or not
# - put new data in database
from Plugin import Plugin

class BackendInterface(object):
    def constructor(self):
        pass
    def alreadyExist(self, key):
        pass
    def put(self, key, something):
        pass


class Backend(object):
    def __init__(self, opt):
        if 'plugin' not in opt:
            raise ValueError("no plugin selected")
        self.params = opt;
        self.backend = Plugin().load("plugins/Backend_"+opt['plugin']+".py")
        self.backend.constructor(self.params)

    def alreadyExist(self, key):
        res = self.backend.alreadyExist(key);
        if not isinstance(res, bool):
            raise TypeError('issues with the plugin: '+self.params['plugin']);
        else:
            return res;

    def put(self, key, obj):
        self.backend.put(key, obj);



if __name__ == '__main__':
    # test of the csv backend
    import os
    backend = Backend({
        'plugin':"csv",
        'path':'./',
        'filename':"db.csv"
    });
    os.remove('db.csv')
    if backend.alreadyExist('test.com') != False:
        raise ValueError('euh, you miss it, it doesn\'t exist');

    backend.put('test.com', {
        'name':'baymax',
        'url': 'test.com'
    });
    if backend.alreadyExist('test.com') != True:
        raise ValueError('euh, you miss it, it already exist');
