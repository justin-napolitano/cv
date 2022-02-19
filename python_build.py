import pyfiglet
from pyfiglet import Figlet
from lolpython import lol_py 
import subprocess
from time import sleep
from random import randrange

import colorama
from colorama import init as windows_color
from colorama import Fore, Style, Back
import emoji

from datetime import datetime

class colors: 

    def __init__(self):
        self.RED='\033[0;31m'
        self.PINK='\033[38;5;206m'
        self.PURPLE='\033[1;95m'
        self.JUSTIN='\033[38;5;206;48;5;57m'
        self.HEART='\xF0\x9F\x92\x9C'
        self.BHEART='\xF0\x9F\x92\x94'
        self.NC='\033[0m' # No Color
        self.KISS='\xF0\x9F\x98\x98'
        self.CWEEN='\xF0\x9F\x98\x8B'
        self.PWEASE='\xF0\x9F\x98\xB3'
        self.HOPE='\xF0\x9F\x98\x85'
        self.HAPPY='\xF0\x9F\x98\x81'
        self.ANGEL='\xF0\x9F\x98\x87'
        self.BOSS='\xF0\x9F\x98\x8E'
        self.KISSY='\xF0\x9F\x98\x99'
        self.DEVIL='\xF0\x9F\x98\x88'
        self.MAKEY='\xF0\x9F\x98\xAE'
        self.MMM='\xF0\x9F\x98\x9B'
        self.BIGCRY='\xF0\x9F\x98\xA2'
        self.YAY='\xF0\x9F\x98\x81'
        self.TWO_HEARTS='\xF0\x9F\x92\x95'
        self.TOUNGEY='\xF0\x9F\x98\x9C'
        self.PEACE='\xE2\x9C\x8C'
        self.SHY='\xF0\x9F\x98\x93'
        self.FEAR='\xF0\x9F\x98\xA8'
        self.FLUSH='\xF0\x9F\x98\xB3'
        self.THUMBS='\xF0\x9F\x91\x8D'
        self.BEER='\xF0\x9F\x8D\xBA'
        self.CHEERS='\xF0\x9F\x8D\xBB'
        self.PYTHON='\xF0\x9F\x90\x8D'
        self.EGGPLANT='\xF0\x9F\x8D\x86'
        self.SHRIMP='\xF0\x9F\x8D\xA4'
        self.MOON='\xF0\x9F\x8C\x9A'
        self.GRIMACE='\xF0\x9F\x98\xAC'
        self.STRONG='\xF0\x9F\x92\xAA'
        self.OK='\xF0\x9F\x91\x8C'
        self.CIGGI='\xF0\x9F\x9A\xAC'
        self.EXHALE='\xF0\x9F\x92\xA8'


def make_clean(color):
    current_color = color.PURPLE
    print(current_color + pyfiglet.figlet_format("Now i'm cleaning the old build", font = 'big'))
    thinking(current_color)
    current_color = color.PINK
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
    result = subprocess.run(['make', 'clean'], capture_output=True, text=True)
    print(current_color + result.stdout)
    print(current_color + result.stderr) 
    current_color = color.PURPLE
    thinking(current_color)
    print(current_color + pyfiglet.figlet_format("NIce and CWEAN", font = 'big')) 
    thinking(current_color) 

def make_html(color):
    current_color = color.PURPLE
    print(current_color + pyfiglet.figlet_format("Making dE HTML BUIld", font = 'big'))
    thinking(current_color)
    current_color = color.PINK
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
    result = subprocess.run(['make', 'html'], capture_output=True, text=True)
    print(current_color + result.stdout)
    print(current_color + result.stderr) 
    current_color = color.PURPLE
    thinking(current_color)
    print(current_color + pyfiglet.figlet_format("i make it", font = 'big')) 
    thinking(current_color) 

def install_dependencies(color): 
    current_color = color.PURPLE
    print(current_color + pyfiglet.figlet_format("Now we have to install the python dependencies.", font = 'big'))
    thinking(current_color)
    current_color = color.PINK
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
    result = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], capture_output=True, text=True)
    print(current_color + result.stdout)
    print(current_color + result.stderr) 
    current_color = color.PURPLE
    thinking(current_color)
    print(current_color + pyfiglet.figlet_format("DependenCies INstalled", font = 'big')) 
    thinking(current_color)

def introduction(color, no_color):
    windows_color()
    fig = Figlet(font='standard')
    current_color = color
    no_color = no_color
    heart = pyfiglet.figlet_format("<3<3<3<3<3", font = 'big')
    print(current_color + heart)
    print(fig.renderText("seNPai!"))
    print(fig.renderText("I'm baCK!!!"))
    print(heart)
    sleep(5)
    fig = Figlet(font='Standard')
    print(fig.renderText("UR Python's WOrking weLL Nowz"))
    thinking(current_color)
    print(fig.renderText("B4 we beginz"))
    thinking(current_color)
    print(fig.renderText("you Should REeeealy read the requirements.txt file"))
    thinking(current_color)
    print(fig.renderText("If you don't trust me press ctr-c now to stop this program.   Then, read the file.")) 
    thinking(current_color)

def test():
    print(emoji.emojize(":purple_heart:"))
    print(emoji.emojize(":winking_face_with_tongue:"))
    print(emoji.emojize(":zipper-mouth_face:"))    

def command():
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)



def deploy(color):
    current_color = color.PURPLE
    print(current_color + pyfiglet.figlet_format("DEPLOYING!!!", font = 'big'))
    thinking(current_color)
    current_color = color.PINK
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
    result = subprocess.run(['ghp-import', '-n', '-p', '-f', '-c','cv.jnapolitano.io', 'build/html' ], capture_output=True, text=True)
    print(current_color + pyfiglet.figlet_format("Output", font = 'big'))
    thinking(current_color)
    print(current_color + result.stdout)
    print(current_color + pyfiglet.figlet_format("Errors", font = 'big'))
    thinking(current_color)
    print(current_color + result.stderr) 
    current_color = color.PURPLE
    thinking(current_color)
    print(current_color + pyfiglet.figlet_format("i deployz it", font = 'big')) 
    thinking(current_color)  

def thinking(color):
    think = '-------------'
    i=0
    j=0 
    end=randrange(3,9)
    think = pyfiglet.figlet_format(think, font = 'standard')
    #sleep(10)
    print(color + think)

def add(color):
    current_color = color.PURPLE
    print(current_color + pyfiglet.figlet_format("Adding CHanges!!!", font = 'big'))
    thinking(current_color)
    current_color = color.PINK
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    print(current_color + pyfiglet.figlet_format("Output", font = 'big'))
    thinking(current_color)
    print(current_color + result.stdout)
    print(current_color + pyfiglet.figlet_format("Errors", font = 'big'))
    thinking(current_color)
    print(current_color + result.stderr) 
    current_color = color.PURPLE
    thinking(current_color)
    print(current_color + pyfiglet.figlet_format("changes added", font = 'big')) 
    thinking(current_color)  
 
def timestamp():
    dt = datetime.now()
    return dt

def commit(color):
    current_color = color.PURPLE
    print(current_color + pyfiglet.figlet_format("commiting !!!", font = 'big'))
    thinking(current_color)
    current_color = color.PINK
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
    result = subprocess.run(['git', 'commit', '-m', 'awtocommit on' + str(timestamp())], capture_output=True, text=True)
    print(current_color + pyfiglet.figlet_format("Output", font = 'big'))
    thinking(current_color)
    print(current_color + result.stdout)
    print(current_color + pyfiglet.figlet_format("Errors", font = 'big'))
    thinking(current_color)
    print(current_color + result.stderr) 
    current_color = color.PURPLE
    thinking(current_color)
    print(current_color + pyfiglet.figlet_format("committed", font = 'big')) 
    thinking(current_color) 


def push(color):
    current_color = color.PURPLE
    print(current_color + pyfiglet.figlet_format("PUshing", font = 'big'))
    thinking(current_color)
    current_color = color.PINK
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
    result = subprocess.run(['git', 'push' + timestamp()], capture_output=True, text=True)
    print(current_color + pyfiglet.figlet_format("Output", font = 'big'))
    thinking(current_color)
    print(current_color + result.stdout)
    print(current_color + pyfiglet.figlet_format("Errors", font = 'big'))
    thinking(current_color)
    print(current_color + result.stderr) 
    current_color = color.PURPLE
    thinking(current_color)
    print(current_color + pyfiglet.figlet_format("pushed it Good", font = 'big')) 
    thinking(current_color) 


def main():
    color= colors()
    introduction(color.PURPLE, color.NC)
    install_dependencies(color)
    make_clean(color)
    make_html(color)
    add(color)
    commit(color)
    push(color)
    deploy(color)


if __name__ == "__main__":
    main()