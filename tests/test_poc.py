import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage


# a sample test directly interacting with the elements right inside the test itself
def test_sample_page(page):
    page.goto("/")
    assert page.inner_text('h1') == '''UI Test Automation
Playground'''
    page.click("text=Dynamic ID")
    assert page.inner_text('h3') == 'Dynamic ID'


# a simple test consuming the logic and locators defined in the page object file
def test_pom_class(browser, page):
    home = HomePage(browser)
    home.visit()
    page.wait_for_timeout(5000)




    
    
    
