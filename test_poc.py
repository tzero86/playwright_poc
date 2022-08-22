import pytest

@pytest.mark.skip_browser("firefox")
def simple_test_case(page):
    page.goto("/")
    assert page.inner_text('h1') == 'UI Test Automation Playground'
    page.click("text=Dynamic ID")
    
