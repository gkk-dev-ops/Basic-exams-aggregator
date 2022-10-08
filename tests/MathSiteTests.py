import unittest
from Tools import Utils
from selenium.webdriver.common.by import By

SUBPAGES: list[str] = ["index.html", "math-tests.html"]
SUBPAGES_MATH: list[str] = ["Addition.html", "Division.html",
                            "Fractions.html", "Multiplication.html", "Substraction.html"]


class TabTitleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.util: Utils = Utils()
        self.util.navigateToSite()

    def tearDown(self) -> None:
        self.util.closeBrowser()

    def _subpages_title_text(self, page, expectedText, path="") -> None:
        """
            Tests if all defined subpages are available.
            args:
                pages (str): page address.
                expectedText (str): text expeceted to be on tab title.
                path (str): path to tested endpoint (whole endpoint path is path + pages).
        """
        self.util.navigateToSite(f"{path}/{page}")
        self.assertEqual(self.util.getTabTitle(), expectedText)

    def test_root_subpages(self) -> None:
        for page in SUBPAGES:
            self._subpages_title_text(page, 'School tests in one place!📃🏢🥳')

    def test_math_subpages(self) -> None:
        for page in SUBPAGES_MATH:
            self._subpages_title_text(
                page, f'{page.removesuffix(".html")} test ⌚', "/math-tests")

    def test_navigation_rootpages_navbar(self) -> None:
        for site in SUBPAGES:
            self.util.navigateToSite(f"/{site}")
            navbarItemsCount: int = len(self.util.webdriver.find_elements(
                By.CLASS_NAME, 'header-item'))
            for i in range(navbarItemsCount):
                navBtns = self.util.webdriver.find_elements(
                    By.CLASS_NAME, 'header-item')
                navBtnTxt: str = navBtns[i].text
                if navBtnTxt == "Home":
                    navBtnTxt = "index"
                elif navBtnTxt == "Math":
                    navBtnTxt = "math-tests"
                elif navBtnTxt == "German":
                    navBtnTxt = "german"
                navBtns[i].click()
                self.assertEqual(navBtnTxt, self.util.webdriver.current_url.removesuffix(
                    ".html").removeprefix("http://127.0.0.1:5500/"))
                self.util.webdriver.back()

    def test_navigation_mathpages_navbar(self) -> None:
        for site in SUBPAGES_MATH:
            self.util.navigateToSite(f"/math-tests/{site}")
            navbarItemsCount: int = len(self.util.webdriver.find_elements(
                By.CLASS_NAME, 'header-item'))
            for i in range(navbarItemsCount):
                navBtns = self.util.webdriver.find_elements(
                    By.CLASS_NAME, 'header-item')
                navBtnTxt: str = navBtns[i].text
                if navBtnTxt == "Home":
                    navBtnTxt = "index"
                elif navBtnTxt == "Math":
                    navBtnTxt = "math-tests"
                elif navBtnTxt == "German":
                    navBtnTxt = "german"
                navBtns[i].click()
                self.assertEqual(navBtnTxt, self.util.webdriver.current_url.removesuffix(
                    ".html").removeprefix("http://127.0.0.1:5500/"))
                self.util.webdriver.back()

    def test_navigation_home_tiles(self) -> None:
        self.util.navigateToSite()
        navTiles = self.util.webdriver.find_elements(
            By.CLASS_NAME, 'test-type-tile')
        for i in range(len(navTiles)):
            navTiles = self.util.webdriver.find_elements(
                By.CLASS_NAME, 'test-type-tile')
            navTileTxt: str = navTiles[i].text
            navTiles[i].click()
            self.assertEqual(navTileTxt, self.util.webdriver.current_url.removesuffix(
                ".html").removeprefix("http://127.0.0.1:5500/math-tests/"))
            self.util.webdriver.back()

    def test_navigation_math_tiles(self) -> None:
        self.util.navigateToSite("/math-tests.html")
        navTiles = self.util.webdriver.find_elements(
            By.CLASS_NAME, 'test-type-tile')
        for i in range(len(navTiles)):
            navTiles = self.util.webdriver.find_elements(
                By.CLASS_NAME, 'test-type-tile')
            navTileTxt: str = navTiles[i].text
            navTiles[i].click()
            self.assertEqual(navTileTxt, self.util.webdriver.current_url.removesuffix(
                ".html").removeprefix("http://127.0.0.1:5500/math-tests/"))
            self.util.webdriver.back()


if __name__ == '__main__':
    unittest.main()
