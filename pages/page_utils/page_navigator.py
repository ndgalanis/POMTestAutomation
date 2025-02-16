import importlib

class PageNavigator:
    """
    A utility class for navigating to different pages in the application.
    """

    @staticmethod
    def navigate_to(page_name):
        """
        Dynamically loads and returns an instance of the requested page.

        :param page_name: The name of the page (e.g., "starting_page").
        :return: An instance of the specified page class.
        """
        module_name = f"pages.{page_name}"
        class_name = "".join(word.capitalize() for word in page_name.split("_"))
        try:
            module = importlib.import_module(module_name)
            page_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ValueError(f"Failed to load page '{page_name}': {e}")

        page = page_class()
        page.open_page(page.get_page_url())
        page.check_title()
        return page


