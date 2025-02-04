from pages.starting_page import StartingPage

class Navigator:

    @staticmethod
    def starting_page():
        """Navigate to the Starting Page and returns an instance of it"""
        page= StartingPage()
        page.open_page(page.get_page_url())
        page.check_title()
        return page
