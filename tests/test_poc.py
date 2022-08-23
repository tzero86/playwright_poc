import pytest
from playwright.sync_api import Page


def test_sample_page(page):
    page.goto("/")
    assert page.inner_text('h1') == '''UI Test Automation
Playground'''
    page.click("text=Dynamic ID")
    assert page.inner_text('h3') == 'Dynamic ID'





    
    
    
