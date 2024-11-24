import logging
from mitmproxy import http

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        logging.info("We've seen %d flows" % self.num)

class ShenGuangHongChan:
    def __init__(self):
        self.num = 0

    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.pretty_url == "https://www.365sghc.com/class/app/index.php?method52=b.strategicdp.querystrategicdp":
            self.num = self.num + 1
            text = flow.response.get_text()
            logging.info(text)

addons = [
    #Counter(),
    ShenGuangHongChan()
]