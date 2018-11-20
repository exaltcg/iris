# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = 'Remove part of the searched item'
        self.test_case_id = '127246'
        self.test_suite_id = '2085'
        self.locales = ['en-US']

    def run(self):

        find_in_page_icon_pattern = Pattern('find_in_page_icon.png')
        soap_label_pattern = Pattern('soap_label.png')
        soap_large_title_selected_pattern = Pattern('soap_large_title_selected.png')
        soap_large_title_unselected_pattern = Pattern('soap_large_title_unselected.png')
        soap_s_large_title_selected_pattern = Pattern('soap_s_large_title_selected.png')
        soap_so_large_title_selected_pattern = Pattern('soap_so_large_title_selected.png')
        soap_soa_large_title_selected_pattern = Pattern('soap_soa_large_title_selected.png')

        test_page_local = self.get_asset_path('wiki_soap.html')
        navigate(test_page_local)

        soap_label_exists = exists(soap_label_pattern, 20)

        assert_true(self, soap_label_exists, 'The page is successfully loaded.')

        open_find()
        edit_select_all()
        edit_delete()

        find_toolbar_opened = exists(find_in_page_icon_pattern, 10)

        assert_true(self, find_toolbar_opened, 'Find Toolbar is opened.')

        type('soap', interval=1)

        selected_label_exists = exists(soap_large_title_selected_pattern, 5)
        unselected_label_exists = exists(soap_label_pattern, 5)

        assert_true(self, selected_label_exists, 'The first one has a green background highlighted.')
        assert_true(self, unselected_label_exists, 'The others are not highlighted.')

        type(Key.BACKSPACE)

        soa_selected_exists = exists(soap_soa_large_title_selected_pattern, 5)
        type(Key.BACKSPACE)

        so_selected_exists = exists(soap_so_large_title_selected_pattern)
        type(Key.BACKSPACE)

        s_selected_exists = exists(soap_s_large_title_selected_pattern)
        type(Key.BACKSPACE)

        soap_clean_exists = exists(soap_large_title_unselected_pattern, 5)

        assert_true(self,
                    soa_selected_exists &
                    so_selected_exists &
                    s_selected_exists &
                    soap_clean_exists,
                    'The matching characters are changing accordingly.')
