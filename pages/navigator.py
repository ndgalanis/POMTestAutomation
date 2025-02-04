from pages.starting_page import StartingPage


class Navigator:
    """
    A utility class for navigating to different pages in the application.
    Provides methods for navigating to specific pages and interacting with them.
    """

    @staticmethod
    def starting_page():
        """
        Navigates to the Starting Page (home page) and returns an instance of the page object.

        This method opens the starting page URL, checks if the title is correct,
        and returns an instance of the StartingPage class to allow further interactions.

        :return: An instance of the StartingPage.
        """
        page = StartingPage()
        page.open_page(page.get_page_url())
        page.check_title()
        return page
