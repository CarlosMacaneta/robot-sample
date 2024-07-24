from robocorp.tasks import task
from robocorp import browser

@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    browser.configure(browser_engine="msedge", slowmo=100,)
    
    github_login()


def open_the_github_website():
    """Navigates to the given URL"""
    browser.goto("https://github.com/your_username")


def github_login():
    browser.goto("https://github.com/login")
    login()


def login():
    """Fills in the login form and clicks the 'Log in' button"""
    page = browser.page()
    
    page.fill("#login_field", "maria")
    page.fill("#password", "maria123")
    page.click("input[type=submit]")