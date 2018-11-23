# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = 'Search Links only [NOTE: Fails on step 3 because pink background does not appear]'
        self.test_case_id = '127252'
        self.test_suite_id = '2085'
        self.locales = ['en-US']

    def run(self):

        soap_label_pattern = Pattern('soap_label.png')
        find_in_page_links_only_icon_pattern = Pattern('find_in_page_links_only_icon.png')
        find_in_page_links_only_soap_pattern = Pattern('find_links_only_part.png')

        soap_link_highlighted_green_pattern = Pattern('soap_link_highlighted.png')
        soap_link_highlighted_green_pattern.similarity = 0.6

        soap_other_link_highlighted_pink_pattern = Pattern('soap_link_disambiguation_highlighted.png')

        test_page_local = self.get_asset_path('wiki_soap.html')
        navigate(test_page_local)

        soap_label_exists = exists(soap_label_pattern, 20)
        assert_true(self, soap_label_exists, 'The page is successfully loaded.')

        type("'")

        # Remove all text from the toolbar
        edit_select_all()
        edit_delete()

        find_toolbar_opened = exists(find_in_page_links_only_icon_pattern, 10)

        assert_true(self, find_toolbar_opened, 'Find Toolbar (links only) is opened.')

        type('soap', interval=1)

        found_link_highlighted_green = exists(soap_link_highlighted_green_pattern, 5)

        assert_true(self, found_link_highlighted_green, 'Matching link is found.')

        # Other link doesn't have pink background, so raise an Exception
        # raise AssertionError

        # other_link_highlighted_pink = exists(soap_another_link_pattern, 10)
        assert_true(self, False, 'Other links are pink. [Known issue other links do not have pink background]')

        try:
            search_links_only_toolbar_disappeared = wait_vanish(find_in_page_links_only_soap_pattern, 30)
            assert_true(self, search_links_only_toolbar_disappeared, "The Findbar is disappeared")
        except FindError:
            raise FindError("The Findbar is NOT disappeared")