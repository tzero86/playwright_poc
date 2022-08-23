# page object representing the home page
class HomePage:
    # we initialize the class
    def __init__(self, page):
        self.page = page
        self.home_tag_line = page.locator('#citation > p')

    def get_tag_line(self):
        return self.page.inner_text(self.home_tag_line)

    def goto(self, param):
        self.page.goto('/')
