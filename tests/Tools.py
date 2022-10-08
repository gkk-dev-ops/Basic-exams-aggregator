from selenium import webdriver


class Utils:
    def __init__(self) -> None:
        self.webdriver: webdriver = webdriver.Chrome()

    def closeBrowser(self) -> None:
        self.webdriver.close()

    def navigateToSite(self, path="") -> None:
        """Navigate to locally hosted test site.

            Args:
                path (str): Path to subsubite on test website.
        """
        url: str = "http://127.0.0.1:5500" + path
        self.webdriver.get(url)

    def getTabTitle(self) -> str:
        """Get title of current tab."""
        return self.webdriver.title
