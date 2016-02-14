# What is crawlr?
A simple Crawling framework in Python build to make our life easier
for creating and running bots. It is composed of 3 main components:
- a browser automation system
- a pluggable backend to store data
- a pluggable log system to store your logs. Usefull if you want to
  know if the bot is alive or not.

# Why?
I needed a framework to create crawlers that could be seen as an
extension of selenium and will allow me to store logs and
data. For complex websites based on javascript interactions, I
couldn't find one that fit my needs so I created it.

Some easy things that can be done painlessly with Crawlr go from:
- automatically send message to people on Craiglist that have your
  product at your price
- do some automatic answer on any social media
- automatically send your resume to any job platform
...
the list goes on and on.

# The spirit
Selenium can still be use directly, everything is pluggable so that
log and backend system can be interchange directly without issues.

# The parts
## Browser automation
It makes use of selenium but:
- without the verbosity. Selenium is great but we still have
  to write a big amount of code that at some point will have to be
  maintain. For real life example with complex interaction,
  you might have many steps, just for a single clicks to do. Let's
  decompose a real life example with a click that make us go to
  another page:
  1) wait until the button you wish to click on is present
  2) click on it
  3) then verify the current element has disappear
  4) verify the current page you are in the good one
  Writing properly one single interaction can be cumbersome using
  selenium.

  This is how to do that using Crawlr:

  ```
  self.click(self.page['login']['buttons']['submit'], {
      'thenDisappear':True,
      'thenWait':self.page['homepage']['search']
  });
  ```

- without the cumbersome setup. A selection of driver are already
  preinstall. You don't need to worry about loading everything in your
  path or anything like that. Just have the browser you wish to
  execute the test on be install on the machine. That's it.

## Backend
The backend allow you to store some data. You just put an object,
nothing more to worry about. Currently it push data only as a csv but
it should be fairly simple to implement something else

## Logger
You can log anything you want to any backend you want. Currently only
CouchDB but is is pluggable so it should be fairly simple to implement
anything else


# Run a script in a server without graphical interface

If you want to run it on a server you would need to install xvbf to
emulate a display. Basically:
```
apt-get install -y xvbf firefox
```
To run the example you would do:
```
xvbf-run python google.py
```
That's it you can forget about your bot and only worry about the data
you will get.

The cool thing is you can even take pictures from the browser event if
the server doesn't have X install and access those screenshot from a url.


# Concrete example of the selenium fatigue

If we want to search something on google and press the first link:

``` python
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

searchInput = 'input.gsfi';
search = "nyan cat video"
resultBox = "#ires h3 a";

driver = webdriver.Firefox();
driver.get('http://google.com');

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, searchInput)));
el = driver.find_element_by_css_selector(searchInput);
el.send_keys(search+Keys.ENTER);

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, resultBox)));
el = driver.find_element_by_css_selector(resultBox);
el.click();
WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, resultBox)))

sleep(20)
driver.quit();
```

It looks very heavy and forgetting any of those line remove stability
from your script and you will endup spending time to figureout what is
the problem with this bug... We shouldn't assume by default the
content we expect will be here even if we wait 1 second before to do
something (what if it take 2 seconds to load a page? Are you sure you
want to throw an error?)

Using Crawlr, it simply become:

``` python

import Crawlr
crawl = Crawlr();
crawl.logger.log("let's get started")

crawl.browser.go('http://google.com')

crawl.browser.write("input.gsfi", "nyan cat video", {
'thenPressEnter':True,
'thenDisappear':True,
'thenWait':"#ires h3 a",
});

crawl.browser.click("#ires h3 a", {
    'thenDisappear':True,
    'thenWait':"#masthead-search-term"
});

crawl.logger.log("LA LA LALALALALA LA LA")
time.sleep(30)
```
