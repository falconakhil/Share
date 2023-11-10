import subprocess
import os
import tempfile
import shutil
import zipfile
from pyngrok import ngrok
import threading
from MessageDialog import *
#import Share

class WebServer:
    port = 8080
    server = None
    root = None
    ngrok=False
    ngrokUrls=[None]*2

    def start(self):
        os.chdir(self.root.dir)
        self.server = subprocess.Popen(["python3", "-m", "http.server", str(self.port)],stdout=subprocess.PIPE)
        if(self.ngrok):
            ngrokLink=ngrok.connect(8056).__str__()
            tmp=ngrokLink.index("\"")+1
            tmp2=ngrokLink.index("\"",tmp+1)
            ngrokUrl1=ngrokLink[tmp:tmp2]
            link=ngrokUrl1[ngrokUrl1.rfind("/")+1:len(ngrokUrl1)]
            self.ngrokUrls[0]="http://"+link
            self.ngrokUrls[1]="https://"+link

    def __init__(self, port, root,ngrok):
        self.port = port
        self.root = root
        self.ngrok=ngrok
    def stop(self):
        self.server.kill()
        if(self.ngrok):
            for i in self.ngrokUrls:
                ngrok.disconnect(i)

class WebRoot:
    dir = ""

    def add_file(self, file):
        name = ""
        if os.name == "posix":
            name = file[file.rfind("/") + 1:len(file)]
        else:
            name = file[file.rfind("\\") + 1:len(file)]
        os.symlink(file, self.dir+name)

    def add_dir(self, path):
        name = ""
        if os.name == "posix":
            name = path[path.rfind("/") + 1:len(path)]
        else:
            name = path[path.rfind("\\") + 1:len(path)]
        ziph = zipfile.ZipFile(os.path.join(self.dir,name + ".zip"), 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
        ziph.close()
    def clean(self):
        shutil.rmtree(self.dir)

    def __init__(self):
        self.dir=tempfile.mkdtemp(prefix="Share")+"/"
