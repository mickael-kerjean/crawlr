# This guy is our backend. He can:
# - check if an entry already exist or not
# - put new data in database

class BackendInterface(object):
    def constructor(self):
        pass
    def alreadyExist(self, key):
        pass
    def put(self, key, something):
        pass


class Backend(object):
    def __init__(self, opt):
        self.params = opt;
        self.backend = {};
        execfile("plugins/Backend_"+opt['plugin']+".py", self.backend);
        self.backend = self.backend['export']
        self.backend.constructor(self.params)

    def alreadyExist(self, key):
        a = self.backend(key);
        if not isinstance(a, bool):
            raise TypeError('issues with the plugin: '+self.params['plugin']);
        else:
            return a;

    def put(self, obj):
        self.backend.put(obj);



if __name__ == '__main__':

    # test of the csv backend
    backend = Backend('', {
        'plugin':"csv"
    });
    backend.put('test.com', {
        'name':'baymax',
        'url': 'test.com'
    });
    if not backend.alreadyExist('test.com'):
        raise ValueError('euh, you miss it');
