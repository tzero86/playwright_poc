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


# Run the test once, it'll create the base snapshot of the page (snapshots folder)
# then uncomment the line after home.visit() to see the test results from
# the pixelmatch comparison of the two images (snapshot_test_failures folder)
def test_visual_home_page(browser, assert_snapshot):
    home = HomePage(browser)
    home.visit()
    # home.page.click("text=Dynamic ID")
    assert_snapshot(home.page.screenshot())
    # Snapshots can be updated by running pytest --update-snapshots



    
    
    
