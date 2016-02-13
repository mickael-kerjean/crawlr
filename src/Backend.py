###################################
## Implementation of a simple backend
import os;
import csv;
class Backend(object):
    def __init__(self, opt):
        self.logfile = 'db.csv';
        self.params = opt;

    def get(self, confKey):
        pass

    def doesExist(self, title):
        if not os.path.isfile(self.logfile):
            return False;

        with open(self.logfile) as csvfile:
            reader = csv.DictReader(csvfile);
            for row in reader:
                if row['title'] == title:
                    return True;
        return False;


    def put(self, obj):
        # verify data integrity
        if obj.has_key('title') == False:
            obj['title'] = ''
        if obj.has_key('post_date') == False:
            obj['post_date'] = ''
        if obj.has_key('status') == False:
            obj['status'] = ''
        obj = {
            'title': obj['title'],
            'post_date':obj['post_date'],
            'status': obj['status']
        }

        # write log
        if not os.path.isfile(self.logfile):
            with open(self.logfile, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['title', 'post_date', 'status']);
                writer.writeheader();

        with open(self.logfile, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['title', 'post_date', 'status'])
            writer.writerow(obj)
