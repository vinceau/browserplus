import logging
import sys
from mechanize import Browser
from lxml import html

_log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class BrowserPlus(Browser):

    def __init__(self):
        Browser.__init__(self)
        self.set_handle_robots(False)
        self.addheaders = [('Accept',
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

    def _tree(self):
        return html.fromstring(self.response().read())

    def has(self, msg):
        """This returns true if msg is contained in the browsers current page.
        """
        return msg in self._tree().xpath('string()')

    def select_form_by(self, attr, search):
        """Usage: BrowserPlus.select_form_by('id', 'login')
        """
        formcount = 0
        for frm in self.forms():
            if str(frm.attrs[attr]) == search:
                break
            formcount += 1
        return self.select_form(nr=formcount)
   
    def find(self, css):
        """Returns the first occurence of an element matching the css selector
        if it exists and None otherwise
        """
        e = self.find_all(css)
        if e:
            return e[0]
        return None

    def find_all(self, css):
        """Returns a list of all elements that match the css selector
        """
        return self._tree().cssselect(css)

    def go(self, text):
        """Follow the link (a href) containing certain text.
        e.g. <a href="http://foo.bar">foobar</a> BrowserPlus.go('foobar') will
        open the link htp://foo.bar
        """
        try:
            return self.follow_link(text_regex=text)
        except:
            _log.error("Can't find link with text '%s'" % text)
            return None
