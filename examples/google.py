# In this example, we illustrate how to capture the page for some top results
# on google for different keywords. Of course we will store the data and get some
# logs about the bot life or eventual errors

from src.Crawlr import Crawlr

def main:
    search = [
        "BBC news",
        "NYtimes",
        "Lemonde"
    ]
    crawlr = Crawlr();

    while True:
        # go to google.com
        crawlr.browser.go("http://google.com");
        website = choice(search)
        # make a search
        crawlr.browser.write("input.gsk3", website);
        # click the first result
        crawlr.browser.click('h3');
        crawlr.logger.log("got something for: "+website)
        # get the result and insert into our backend
        page = crawlr.browser.find_element('body').text;
        crawler.backend.put(page);

    crawlr.logger.log('I got stop!')

if __name__ == '__main__':
    main();
