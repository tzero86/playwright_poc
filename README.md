# PlayItRight POC

I'm exploring Playwright with Python these days, so I thought I'll create a repo 
to help anyone interested to get started with Playwright Python Automated Testing a bit quicker.

This is just a bare-bones template with some minimal examples and functionalities, you can quickly get started and build on top of it to make it meet your needs.

At the moment it includes the following:

**Current Features:**

- Pytest Support
- Pytest INI Settings for easy CLI arguments management
- Python 3.10 and pytest-playwright usage (synchronous mode for now)
- Page Object Model template
- Exporting results in HTML Including screenshots on failure
- Ability to turn Test Execution Video Recording (on, off, or retain-on-failure) from pytest.ini (retain-on-failure by default)
- Added visual testing support and example test case (PixelMatch comparisons and diff generation, Snapshots can be updated by running pytest --update-snapshots).

**Planned Additions**:
  
  - Add example usage of Playwright Fixtures & Pytest annotations
  - Explore easy triggers for multi-browser execution


## Usage

### PIP Dependency Install

Install all requirements with just one line: `pip install -r requirements.txt`
Then just install Playwright: `playwright install`


### Manual Dependency Install
Simply clone the repo and make sure you have the following packages installed:

Install pytest-playwright:
`pip install pytest-playwright`

Next install pytest:
`pip install pytest`

Next install the HTML reporter:
`pip install pytest-html-reporter`

Next install pytest-playwright-visual for visual testing:
`pip install pytest-playwright-visual`

And finally install playwright:
`playwright install`


### How to run the tests

Run the sample tests with:
`pytest`

NOTE: I'll add a requirements file for easy dependency install later on.

I hope this might help someone.

@tzero86