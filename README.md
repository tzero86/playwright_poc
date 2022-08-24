# PlayItRight POC

Exploring Playwright with python these days, so I thought I'll create a repo 
to help anyone interested to get started with Playwright Python Automated Testing a bit quicker.

This is just a bare-bones template with some minimal examples and functionalities, you can quickly get started and build on top of it to make it meet your needs.

At the moment it includes the following:

**Current Features:**

- Pytest Support
- Pytest INI Settings for easy CLI arguments management
- Python 3.10 and pytest-playwright usage (synchronous mode for now)
- Page Object Model template
- Exporting results in HTML Including screenshots on failure
- Ability to turn Test Execution Video Recording ON/OFF/ONFAILURE from pytest.ini (On-failure by default)

**Planned Additions**:
  
  - Add example usage of Playwright Fixtures & Pytest annotations
  - Explore easy triggers for multi-browser execution


## Usage

Simply clone the repo and make sure you have the following packages installed:

Install pytest-playwright:
`pip install pytest-playwright`

Next install pytest:
`pip install pytest`

Next install the HTML reporter:
`pip install pytest-html-reporter`

And finally install playwright:
`playwright install`

And run the sample tests with:
`pytest`

NOTE: I'll add a requirements file for easy dependency install later on.

I hope this might help someone.

@tzero86