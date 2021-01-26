import random
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from Board import Board


class WebOperator(object):
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")#--headless
        self.chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
        self.chrome.get("https://play2048.co/")
        self.newNum = {2: 0, 4: 0}
        
    def IsGameOver(self):
        isGameOver=self.chrome.find_elements_by_css_selector(".game-over")
        return True if len(isGameOver)>0 else False        

    def ResetGame(self):
        restartButton=self.chrome.find_element_by_css_selector(".restart-button")
        restartButton.click()

    def GetScore(self):
        scoreInfo = self.chrome.find_element_by_css_selector(".score-container")
        matches = re.match(r".*", scoreInfo.text)
        return (matches.group(0))        


    def GetRawInfo(self):
        rawInfo = self.chrome.find_elements_by_css_selector(".tile-container .tile")
        return rawInfo

    def GetBoardInfo(self):
        rawInfo = self.GetRawInfo()
        board = Board()
        for r in rawInfo:
            className = str(r.get_attribute("class"))
            matches = re.match(r"tile tile-(?P<num>\d+) tile-position-(?P<px>\d)-(?P<py>\d)( (?P<misc>.+))?", className)
            misc = ""
            if matches.group("misc") is not None:
                misc = str(matches.group("misc"))
                if "tile-new" == misc:
                    self.newNum[int(matches.group("num"))] += 1
            # print(misc)
            board.title[int(matches.group("py")) - 1][int(matches.group("px")) - 1] = int(matches.group("num"))
        return board

    def RandomMove(self):
        d = random.randint(0, 4)
        actions = ActionChains(self.chrome)
        if (0 == d):
            actions.send_keys(Keys.ARROW_UP).perform()
        elif (1 == d):
            actions.send_keys(Keys.ARROW_DOWN).perform()
        elif (2 == d):
            actions.send_keys(Keys.ARROW_LEFT).perform()
        elif (3 == d):
            actions.send_keys(Keys.ARROW_RIGHT).perform()

    def Move(self,cmd):
        actions = ActionChains(self.chrome)
        if ("UP" == cmd):
            actions.send_keys(Keys.ARROW_UP).perform()
        elif ("DOWN" == cmd):
            actions.send_keys(Keys.ARROW_DOWN).perform()
        elif ("LEFT" == cmd):
            actions.send_keys(Keys.ARROW_LEFT).perform()
        elif ("RIGHT" == cmd):
            actions.send_keys(Keys.ARROW_RIGHT).perform()

        #


if __name__ == "__main__":
    webOperator = WebOperator()
    i = 0
    while ("Game over!" not in webOperator.chrome.page_source):
        time.sleep(1)
        webOperator.GetBoardInfo()
        webOperator.RandomMove()
        i += 1
    print(webOperator.newNum)
