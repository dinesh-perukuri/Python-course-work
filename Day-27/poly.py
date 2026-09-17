class Hotstar:
    def __init__(self,name):
        print(f'Welcome to the hotstar {name}----------------------')
    def auth(self):
        print('You can login/Register')
    def dashboard(self):
        print('You can see the dashboard')
    def search(self):
        print('You can search')
    def history(self):
        print('You can see the history')
    def playcontrollers(self):
        print('You can pause/Resume/Play')
    def ads(self):
        print('Adds will be run')
    def quality(self):
        print('You have limited quality')
    def devices(self):
        print('You can login in only one device')
    def acess(self):
        print('limited acess')
    def download(self):
        print("You can't download")

class Premiumhotstar(Hotstar):
    def __init__(self,name):
            print(f'Welcome to the hotstar {name}----------------------')
    def ads(self):
        print('Adds will not run')
    def quality(self):
        print('You have high quality')
    def devices(self):
        print('You can login in multiple devices device')
    def acess(self):
        print('unlimited acess')
    def download(self):
        print("You can download")
    

tarun=Hotstar('tharun')
tarun.auth()
tarun.dashboard()
tarun.search()
tarun.history()
tarun.playcontrollers()
tarun.ads()
tarun.quality()
tarun.devices()
tarun.acess()
tarun.download()


vinod=Premiumhotstar('vinod')
vinod.auth()
vinod.dashboard()
vinod.search()
vinod.history()
vinod.playcontrollers()
vinod.ads()
vinod.quality()
vinod.devices()
vinod.acess()
vinod.download()



        