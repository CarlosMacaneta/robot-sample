from robocorp.tasks import task
from robocorp import browser

@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    browser.configure(browser_engine="msedge",slowmo=100,)
    
    open_the_github_website()


def open_the_github_website():
    """Navigates to the given URL"""
    browser.goto("https://github.com/your_username")
