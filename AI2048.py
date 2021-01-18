from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
import random

class Board(object):
    def __init__(self):  
        self.title=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

class WebOperator(object):
    def __init__(self):  
        options = Options()
        options.add_argument("--disable-notifications")
        self.chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
        self.chrome.get("https://play2048.co/")
        self.newNum={2:0,4:0}

    def GetRawInfo(self):
        rawInfo=self.chrome.find_elements_by_css_selector(".tile-container .tile")
        return rawInfo
    
    def GetBoardInfo(self):
        rawInfo=self.GetRawInfo()
        board=Board()
        for r in rawInfo:
            className=str(r.get_attribute("class"))
            matches = re.match(r"tile tile-(?P<num>\d+) tile-position-(?P<px>\d)-(?P<py>\d)( (?P<misc>.+))?", className)
            misc=""
            if matches.group("misc") is not None:
                misc=str(matches.group("misc"))
                if "tile-new"==misc:
                    self.newNum[int(matches.group("num"))]+=1     
            print(misc)
            board.title[int(matches.group("py"))-1][int(matches.group("px"))-1]=int(matches.group("num"))
            i=1
        print(self.newNum)

    def RandomMove(self):
        d = random.randint(0,4)
        actions = ActionChains(self.chrome)
        if (0==d):
            actions.send_keys(Keys.ARROW_UP).perform()
        elif (1==d):
            actions.send_keys(Keys.ARROW_DOWN).perform()        
        elif (2==d):
            actions.send_keys(Keys.ARROW_LEFT).perform()          
        elif (3==d):
            actions.send_keys(Keys.ARROW_RIGHT).perform()          

#
#actions = ActionChains(chrome)
#
#time.sleep(1)
#
#actions.send_keys(Keys.ARROW_LEFT).perform()
#
#board=chrome.find_elements_by_css_selector(".tile-container .tile")
#board[0].get_attribute("class")
#uuu=1
        
webOperator = WebOperator()
i=0
while ("Game over!" not in webOperator.chrome.page_source):
    time.sleep(1)
    webOperator.GetBoardInfo()
    webOperator.RandomMove()
    i+=1
print(webOperator.newNum)