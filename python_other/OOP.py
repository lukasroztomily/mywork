import random

class CfgCorruptFile(Exception):
    def __init__(self, domain, stat_code):
        self.d = domain
        self.s = stat_code
    def __str__(self):
        return f'Konfiguracni  soubor {self.d} nebyl rozpoznan. Pro pripojeni se nactou vychozi hodnoty.'

    
class Error(Exception):
    stat_m = ''
    def __init__(self, domain):
        self.d = 'Objevila se chyba na strane serveru'
    def __str__(self):
        return self.d

class ServerError(Exception):
    stat_m = ''
    dictdef = {
                          400:'Syntakticka chyba v pozadavku. Http status - 400',
                          401:'Nedostatecna autorizace. Http status - 401',
                          402:'Pozadavek je rezervovan pro jiny ucet. Http status - 402',
                          403:'Server odmitl pozadavek. Http status - 403',
                          404:'Pozdovany obsah nebyl nalezen. Http status - 404'
             }

    def __init__(self, domain, stat_code):
        self.domainserv = domain
        self.httpcode = stat_code

    def __str__(self):        
        self.stat_m = self.dictdef.get(self.httpcode, 'Neznama chyba')           
        return f'Nelze se pripojit  na {self.domainserv}. Vyskytla se chyba na strane clienta: {self.stat_m}'

        #super().__init__( self.d) 


def log(message):
    print(message)
    
def load_cfg_from_file(filename):
    # this function fails to load config, beacause it is corrupt
    error_details = "Unrecognized config structure"
    raise CfgCorruptFile(filename, error_details)

def create_default_cfg():
    return {
        "server" : "server.domain.com",
        "credentials" : { "user" : "Karel", "pwd" : "einszweidrei"}
    }

def connect_to_server(cfg):
    server = cfg["server"]
    user = cfg["credentials"]["user"]
    pwd = cfg["credentials"]["pwd"]
    print("connecting to {} with username {} and password {}".format(server, user, "*"*len(pwd)))
    return random.choice([400, 401, 402, 403, 404])

def load_data_from_server(cfg):
    status_code = connect_to_server(cfg)
    if random.randint(0,10) > 5:
        raise Error("This is some unspecific random error during server request.")
    raise ServerError(cfg["server"], status_code)

def do_smth_that_never_fails_to_fix_this():
    pass

# test pro který máte sestavit výjimky:
exit = False
try:
    cfg = load_cfg_from_file("file.cfg")
except CfgCorruptFile as e:
    log(e)
    cfg = create_default_cfg()
    
try:
    load_data_from_server(cfg)
except ServerError as e:
    log(e)

    log("Loading data from server failed. Gonna try something that never fails to fix this.")
    do_smth_that_never_fails_to_fix_this()
except Error as e:
    log(e)
    log("Config loader failed, terminating")
    exit = True

if not exit:
    log("data from server succesfully loaded, proceeding with the rest of the program")

