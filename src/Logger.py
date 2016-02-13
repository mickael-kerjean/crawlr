###################################
## NOTIFY USERS ABOUT SOMETHING
import traceback;
class Logger(object):
    def __init__(self, opt):
        self.id = self.pickAName()+str(random.randrange(10));
        self.params = opt;

    def initialize(self, opt):
        self.params = opt;

    def log(self, opt = {}):
        if 'level' not in opt:
            opt['level'] = "INFO";

        if 'exception' in opt:
            exception = opt['exception'];
            exc_type, exc_value, exc_traceback = exception();
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            error = ''.join('!! ' + line for line in lines);
            opt['message'] = "Error. Screenshot available at: "+self.params['screenshot']['endpoint']+"/log/"+filename+"         \n";
            opt['message'] += "Stacktrace: "+error;

        if 'screeshot' in opt:
            try:
                self.browser.get_screenshot_as_file('./log/'+filename);
            except:
                pass;



    def pickAName(self):
        names = ["albattani","allen","almeida","archimedes","ardinghelli","aryabhata","austin","babbage","banach","bardeen","bartik","bassi","bell","bhabha","bhaskara","blackwell","bohr","booth","borg","bose","boyd","brahmagupta","brattain","brown","carson","chandrasekhar","colden","cori","cray","curie","darwin","davinci","dijkstra","dubinsky","easley","einstein","elion","engelbart","euclid","euler","fermat","fermi","feynman","franklin","galileo","gates","goldberg","goldstine","goldwasser","golick","goodall","hamilton","hawking","heisenberg","heyrovsky","hodgkin","hoover","hopper","hugle","hypatia","jang","jennings","jepsen","joliot","jones","kalam","kare","keller","khorana","kilby","kirch","knuth","kowalevski","lalande","lamarr","leakey","leavitt","lichterman","liskov","lovelace","lumiere","mahavira","mayer","mccarthy","mcclintock","mclean","mcnulty","meitner","meninsky","mestorf","minsky","mirzakhani","morse","murdock","newton","nobel","noether","northcutt","noyce","panini","pare","pasteur","payne","perlman","pike","poincare","poitras","ptolemy","raman","ramanujan","ride","ritchie","roentgen","rosalind","saha","sammet","shaw","shirley","shockley","sinoussi","snyder","spence","stallman","stonebraker","swanson","swartz","swirles","tesla","thompson","torvalds","turing","varahamihira","visvesvaraya","volhard","wescoff","williams","wilson","wing","wozniak","wright","yalow","yonath"];
        return random.choice(names);
