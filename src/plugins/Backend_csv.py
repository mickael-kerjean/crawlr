import os;
import csv;

class BackendCSV(object):
    def constructor(self, opt):
        try:
            self.logfile = opt['path']+opt['filename'];
        except:
            raise ValueError("need a path and filename option")
        self.params = opt;

    def alreadyExist(self, key_value):
        if not os.path.isfile(self.logfile):
            return False;

        with open(self.logfile) as csvfile:
            reader = csv.DictReader(csvfile);
            for row in reader:
                for key in row:
                    if key == 'key' and row[key] == key_value:
                        return True;
        return False;


    def put(self, key, obj):
        fieldnames = ['key'] + obj.keys()
        obj['key'] = key;

        if not os.path.isfile(self.logfile):
            with open(self.logfile, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames);
                writer.writeheader();

        with open(self.logfile, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(obj)


export = BackendCSV()
