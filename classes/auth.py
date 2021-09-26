from classes.proxies import Proxies
from classes.tokens import Tokens
from pyrogram import Client
from pyrogram.raw import functions

class Auth (Tokens, Proxies):

    app = None

    def start(self):
        proxies = super().load_proxy_list()
        tokens = super().load_token_list()
        for i in range(0, len(tokens)):
            token = tokens[i].split(":")
            if len(proxies) > 0 and proxies[i] != None:
                proxy = proxies[i].split(":")
                if len(proxy) == 4 and len(token) == 3:
                    self.connect(token[0], token[1], token[2], proxy[0], proxy[1], proxy[2], proxy[3])
                elif len(proxy) == 2 and len(token) == 3:
                    self.connect(token[0], token[1], token[2], proxy[0], proxy[1], None, None)
                elif len(proxy) == 0 and len(token) == 3:
                    print(self.connect(token[0], token[1], token[2], None, None, None, None))
                else:
                    continue
            else:
                if len(token) == 3:
                    self.connect(token[0], token[1], token[2], None, None, None, None)
                else:
                    continue
            self.app.start()
            self.app.stop()
        print("Sessions have been checked")

    def connect(self, name, api_id, api_hash, ip, port, username, password):
        try:
            #proxy with authentication
            if ip != None and port != None and username != None and password != None:
                self.app = Client(session_name="./sessions/" + name, api_id=api_id, api_hash=api_hash, proxy=dict(hostname=ip, port=int(port), username=username, password=password))
            #public proxy
            elif ip != None and port != None:
                self.app = Client(session_name="./sessions/" + name, api_id=api_id, api_hash=api_hash, proxy=dict(hostname=ip, port=int(port)))
            #without authentication
            else:
                self.app = Client(session_name="./sessions/" + name, api_id=api_id, api_hash=api_hash)
            return 1
        except NameError:
            return 0