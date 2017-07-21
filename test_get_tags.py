from unittest import TestCase
from RegexTest import get_tags

# def get_tags(string, start, end):
#     return start, end


class TestGet_tags(TestCase):
    def test_get_tags_all_empty(self):

        string = ''
        start = 0
        end = 0

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('0.0', start_tag)
        self.assertEqual('0.0', end_tag)

    def test_get_tags_string_index_0_0(self):

        string = 'ddsalfkjhdfsdfhlgahuhglkfjhdlfkj'
        start = 0
        end = 0

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.0', end_tag)

    def test_get_tags_string_index_0_5(self):

        string = 'ddsalfkjhdfsdfhlgahuhglkfjhdlfkj'
        start = 0
        end = 5

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.5', end_tag)

    def test_get_tags_string_index_1_5(self):

        string = 'ddsalfkjhdfsdfhlgahuhglkfjhdlfkj'
        start = 1
        end = 5

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.1', start_tag)
        self.assertEqual('1.5', end_tag)

    def test_get_tags_string_index_5_0(self):

        string = 'ddsalfkjhdfsdfhlgahuhglkfjhdlfkj'
        start = 5
        end = 0

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.0', end_tag)

    def test_get_tags_string_index_5_1(self):

        string = 'ddsalfkjhdfsdfhlgahuhglkfjhdlfkj'
        start = 5
        end = 1

        start_tag, end_tag = get_tags(string, start, end)

        self.assertEqual('1.0', start_tag)
        self.assertEqual('1.0', end_tag)

