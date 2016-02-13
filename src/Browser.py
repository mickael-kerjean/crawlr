# A convenient a intuitive api on top of selenium

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep;
from os import environ;

class Browser(object):
    # setup a browser
    def __init__(self, opt):
        if 'browser' not in opt:
            opt['browser'] = 'firefox';
        if 'timeout' not in opt:
            opt['timeout'] = 15;

        if opt['browser'] == 'firefox':
            self.driver = webdriver.Firefox();
        elif opt['browser'] == 'chrome':
            CHROME_DRIVER_PATH = "./lib/dep/chromedriver" if environ.get('OS', '') != 'Windows_NT' else "./dep/chromedriver.exe";
            self.driver = webdriver.chrome.webdriver.WebDriver(CHROME_DRIVER_PATH, 0);

        if 'resizeWindow' in opt:
            self.driver.set_window_size(opt['resizeWindow']['width'], opt['resizeWindow']['height']);

        self.timeout = opt['timeout'];


    def __del__(self):
        try:
            self.driver.quit();
        except:
            pass

    def go(self, url):
        self.driver.get(url);
        self.wait_for_page_fully_load();

    def back(self):
        self.driver.back();
        self.wait_for_page_fully_load();

    def find_elements(self, el):
        self.wait_for_element(el);
        return self.driver.find_elements_by_css_selector(el);

    def find_element(self, el):
        self.wait_for_element(el);
        return self.driver.find_element_by_css_selector(el);

    def click(self, el, opt={}):
        timer = self.timeout;
        if 'maxWait' in opt:
            self.timeout = opt['maxWait'];
        if 'silentError' in opt and opt['silentError'] == True:
            try:
                self._click(el);
            except:
                pass;
        else:
            self._click(el);

        self._executeHooks(opt);
        self.timeout = timer;

    def write(self, el, message, opt={}):
        timer = self.timeout;
        if 'maxWait' in opt:
            self.timeout = opt['maxWait'];
        if 'thenPressEnter' in opt:
            message += Keys.ENTER
        if 'silentError' in opt and opt['silentError'] == True:
            try:
                self._write(el, message);
            except:
                pass;
        else:
            self._write(el, message);

        self._executeHooks(opt);
        self.timeout = timer;

    def wait_for_element(self, el):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, el)));

    def wait_for_page_fully_load(self, pause=0):
        sleep(pause);
        WebDriverWait(self.driver, self.timeout).until(self._readystate_complete);

    def hide_element(self, el):
        self.driver.execute_script('document.querySelector("'+el+'").style["display"] = "none"')

    def scroll_to(self, position = 0):
        self.driver.execute_script('window.scrollTo(0, '+str(position)+')')

    def browse_a_link(self, fn):
        els = self.find_elements('a');
        ok = fn(els);
        ok.click();
        self.wait_for_page_fully_load();

    def _click(self, el):
        self.find_element(el).click();

    def _write(self, el, message):
        self.find_element(el).send_keys(message)

    def _executeHooks(self, opt):
        if 'thenDisappear' in opt:
            WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, opt['thenDisappear'])))
        if 'thenWait' in opt:
            self.waitForElement(opt['thenWait']);

    def _readystate_complete(self, e):
        return e.execute_script("return document.readyState") == "complete"



if __name__ == '__main__':
    chrome = Browser({'browser':'chrome'});
    chrome.go("http://google.com");
    chrome.write("input.gsfi", "hello world!", {
        'thenPressEnter':True
    });
    chrome.click("h3");
    chrome.wait_for_page_fully_load();
    chrome.hide_element('body');
    chrome.back();

    # get native element, but much more verbose
    el = chrome.find_elements("h3")[2]
    el.click()
    chrome.wait_for_page_fully_load();


    firefox = Browser({'broser':'firefox'})
    del firefox;
    del chrome;
