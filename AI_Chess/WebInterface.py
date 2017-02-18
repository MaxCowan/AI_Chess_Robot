# @Author: Max Cowan 2016

# need selenium library
# need newest version of "chromedriver" installed

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class WebInterface:

    PGNtoPush = ""
    moveCounter = 1
    halfTurn = True
    keepAsking = True
    driver = webdriver.Chrome()

    def __init__(self):

        self.driver.get("https://en.lichess.org/analysis")
        self.driver.maximize_window()

        # Locate submit button and PGN text field
        self.submit = WebDriverWait(self.driver, 5).until(self.findsubmit)
        self.textArea = WebDriverWait(self.driver, 5).until(self.findtext)
        self.fenArea = WebDriverWait(self.driver, 5).until(self.findFEN)

    def pushToLichess(self,text):
        self.textArea = WebDriverWait(self.driver, 5).until(self.findtext)
        self.textArea.clear()
        self.textArea = WebDriverWait(self.driver, 5).until(self.findtext)
        fullText = '[FEN "'+text+'"]'
        self.textArea.send_keys(fullText)
        self.clickSubmit()



    def clickSubmit(self):
        self.submit = WebDriverWait(self.driver, 5).until(self.findsubmit)
        self.textArea = WebDriverWait(self.driver, 5).until(self.findtext)
        hover = ActionChains(self.driver).move_to_element(self.textArea)
        hover.perform()
        self.submit.click()


    def findtext(self, *args):
        element = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[1]/div/div/textarea")
        if element:
            return element
        else:
            return False


    def findsubmit(self, *args):
        element = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[1]/div/div/div/button")
        if element:
            return element
        else:
            return False


    def findFEN(self, *args):
        element = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[1]/div/input")
        if element:
            return element
        else:
            return False

    def getFEN(self):

        FEN = WebDriverWait(self.driver, 5).until(self.findFEN)
        return str(FEN.get_attribute("value"))

