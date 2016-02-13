class BackendNothing:
    def constructor(self, opt):
        pass

    def alreadyExist(self, key):
        return False;

    def put(self, key, obj):
        pass


export = BackendNothing();
