from unittest import TestCase
from RegexTest import get_tags

# def get_tags(string, start, end):
#     return start, end

string = '012345678\n012345678\n012345678\n012345678\n0123456789'

class TestGet_tags(TestCase):
    def test_get_tags_all_empty(self):

        string = ''
        start = 0
        end = 0

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('0.0', start_tag)
        self.assertEqual('0.0', end_tag)

    def test_get_tags_string_index_0_0(self):

        start = 0
        end = 0

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.0', end_tag)

    def test_get_tags_string_index_0_5(self):

        start = 0
        end = 5

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.5', end_tag)

    def test_get_tags_no_string_index_0_5(self):

        string = ''
        start = 0
        end = 5

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('0.0', start_tag)
        self.assertEqual('0.0', end_tag)

    def test_get_tags_string_index_1_5(self):

        start = 1
        end = 5

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.1', start_tag)
        self.assertEqual('1.5', end_tag)

    def test_get_tags_string_index_5_0(self):

        start = 5
        end = 0

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.0', end_tag)

    def test_get_tags_string_index_5_1(self):

        start = 5
        end = 1

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.0', end_tag)

    def test_get_tags_string_index_11_16(self):

        start = 11
        end = 16

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('2.1', start_tag)
        self.assertEqual('2.6', end_tag)

    def test_get_tags_string_index_25_45(self):

        start = 25
        end = 45

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('3.5', start_tag)
        self.assertEqual('5.5', end_tag)

