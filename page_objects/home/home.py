
# > This class is a blueprint for creating objects that represent the home page of a website
class HomePage:
    # we initialize the class
    def __init__(self, browser):
        self.browser = browser
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        # LOCATORS:
        #   we define the locators for any elements on the page that we are interested in
        self.home_tag_line = self.page.locator('#citation > p')

    # METHODS:
    #   we add methods to our class, these are typically actions you can do on that page
    def get_tag_line(self):
        return self.page.inner_text(self.home_tag_line)

    def visit(self):
        self.page.goto('http://uitestingplayground.com/')