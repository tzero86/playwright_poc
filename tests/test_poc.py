import pytest
from pytest_html_reporter import attach
from page_objects.home.home import HomePage


# a sample test directly interacting with the elements right inside the test itself
def test_sample_page(page):
    page.goto("/")
    assert page.inner_text('h1') == '''UI Test Automation
Playground'''
    page.click("text=Dynamic ID")
    attach(data=page.screenshot(type='png'))
    assert page.inner_text('h3') == 'Dynamic ID'


# a simple test consuming the logic and locators defined in the page object file
def test_pom_class(browser):
    home = HomePage(browser)
    home.visit()
    attach(data=home.page.screenshot(type='png'))
    assert home.home_tag_line.inner_text() == '''UI Test Automation'''





    
    
    
