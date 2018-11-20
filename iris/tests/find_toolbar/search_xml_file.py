# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = 'Search on a XML page'
        self.test_case_id = '127272'
        self.test_suite_id = '2085'
        self.locales = ['en-US']

    def run(self):

        find_toolbar_pattern = Pattern('find_toolbar_text.png')
        xml_page_logo_pattern = Pattern('xml_page_logo.png')
        xml_page_logo_pattern.similarity = 0.6

        text_first_occurrence_pattern = Pattern('xml_text_first_occurrence_pattern.png')
        text_second_occurrence_pattern = Pattern('xml_text_second_occurrence_pattern.png')

        test_page_local = self.get_asset_path('cd_catalog.xml')
        navigate(test_page_local)

        xml_url_logo_exists = exists(xml_page_logo_pattern, 5)

        assert_true(self, xml_url_logo_exists, 'The page is successfully loaded.')

        open_find()

        # Remove all text from the Find Toolbar
        edit_select_all()
        edit_delete()

        find_toolbar_is_opened = exists(find_toolbar_pattern, 5)

        assert_true(self, find_toolbar_is_opened, 'The Find Toolbar is successfully displayed '
                                                  'by pressing CTRL + F / Cmd + F,.')

        type('for')

        selected_label_exists = exists(text_first_occurrence_pattern, 5)

        assert_true(self, selected_label_exists, 'All the matching words/characters are found.')

        text_first_occurrence_exists = exists(text_first_occurrence_pattern, 5)
        text_second_occurrence_exists = exists(text_second_occurrence_pattern, 5)

        assert_true(self, (text_first_occurrence_exists is True) and (text_second_occurrence_exists is False),
                    'First occurrence highlighted')

        # Go to next occurrence
        find_next()

        text_first_occurrence_exists = exists(text_first_occurrence_pattern, 5)
        text_second_occurrence_exists = exists(text_second_occurrence_pattern, 5)

        assert_true(self, (text_first_occurrence_exists is False) and (text_second_occurrence_exists is True),
                    'Second occurrence highlighted')

        # Go to first occurrence
        find_previous()

        text_first_occurrence_exists = exists(text_first_occurrence_pattern, 5)

        type(Key.DOWN)
        type(Key.UP)

        text_first_occurrence_exists_after_scroll = exists(text_first_occurrence_pattern, 5)

        assert_true(self, text_first_occurrence_exists == text_first_occurrence_exists_after_scroll,
                    'Occurrence exists after scroll up and down. No checkboarding is present.')
