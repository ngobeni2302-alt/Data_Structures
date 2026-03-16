import unittest
from data_structures import (
    split_coords, flatten_list, create_id_lookup, top_performer, sort_by_length,
    group_by_category, sort_dict_by_value, rotate_list, sort_emails_by_domain,
    is_subset, remove_dictionary_key, invert_dictionary, recursive_sum,
    fibonacci_generator,
)


class TestDataStructures(unittest.TestCase):

    def test_split_coords(self):
        self.assertEqual(
            split_coords([(12, 45), (15, 48), (18, 51)]),
            ([12, 15, 18], [45, 48, 51])
        )

    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([[['a']], ['b', 'c']]), ['a', 'b', 'c'])

    def test_create_id_lookup(self):
        self.assertEqual(
            create_id_lookup(["Sipho", "Lerato", "Thandi", "Kobane"]),
            {"Sipho": 0, "Lerato": 1, "Thandi": 2, "Kobane": 3}
        )

    def test_top_performer_1(self):
        self.assertEqual(
            top_performer({'A': 85, 'B': 90, 'C': 78, 'D': 92, 'E': 88}),
            'D'
        )

    def test_top_performer_2(self):
        self.assertEqual(
            top_performer({'Tom': 67, 'Jerry': 89, 'Mickey': 95, 'Donald': 80}),
            'Mickey'
        )

    def test_top_performer_3(self):
        result = top_performer({'Raj': 60, 'Simran': 60, 'Aman': 59})
        self.assertIn(result, ['Raj', 'Simran'])

    def test_sort_by_length(self):
        self.assertEqual(
            sort_by_length(["Christopher", "Ava", "Joe", "Bernadette"]),
            ["Ava", "Joe", "Bernadette", "Christopher"]
        )

    def test_group_by_category(self):
        input_data = [
            {"name": "Boerewors", "type": "Meat"},
            {"name": "Charcoal", "type": "Hardware"},
            {"name": "Lamb Chops", "type": "Meat"},
            {"name": "Chakalaka", "type": "Canned Goods"}
        ]

        expected = {
            "Meat": ["Boerewors", "Lamb Chops"],
            "Hardware": ["Charcoal"],
            "Canned Goods": ["Chakalaka"]
        }

        self.assertEqual(group_by_category(input_data), expected)

    def test_sort_dict_by_value_1(self):
        self.assertEqual(
            sort_dict_by_value({'a': 3, 'b': 1, 'c': 2}),
            {'b': 1, 'c': 2, 'a': 3}
        )

    def test_sort_dict_by_value_2(self):
        self.assertEqual(
            sort_dict_by_value({'x': 10, 'y': 5, 'z': 7}),
            {'y': 5, 'z': 7, 'x': 10}
        )

    def test_rotate_list_1(self):
        self.assertEqual(
            rotate_list([1, 2, 3, 4, 5], 2),
            [4, 5, 1, 2, 3]
        )

    def test_rotate_list_2(self):
        self.assertEqual(
            rotate_list([10, 20, 30], 1),
            [30, 10, 20]
        )

    def test_rotate_list_3(self):
        self.assertEqual(
            rotate_list([1, 2], 3),
            [2, 1]
        )

    def test_rotate_list_empty(self):
        self.assertEqual(rotate_list([], 5), [])

    def test_sort_emails_by_domain(self):
        input_emails = [
            "alice@yahoo.com",
            "bob@gmail.com",
            "charlie@outlook.com",
            "dave@gmail.com"
        ]

        expected = [
            "bob@gmail.com",
            "dave@gmail.com",
            "charlie@outlook.com",
            "alice@yahoo.com"
        ]

        self.assertEqual(sort_emails_by_domain(input_emails), expected)

    def test_is_subset_1(self):
        self.assertTrue(is_subset([1, 2], [1, 2, 3, 4]))

    def test_is_subset_2(self):
        self.assertFalse(is_subset([5, 6], [1, 2, 3]))

    def test_is_subset_3(self):
        self.assertTrue(is_subset(['a'], ['a', 'b', 'c']))

    def test_remove_dictionary_key_1(self):
        self.assertEqual(
            remove_dictionary_key({'a': 1, 'b': 2, 'c': 3}, 'b'),
            {'a': 1, 'c': 3}
        )

    def test_remove_dictionary_key_2(self):
        self.assertEqual(
            remove_dictionary_key({'x': 10}, 'x'),
            {}
        )

    def test_remove_dictionary_key_3(self):
        self.assertEqual(
            remove_dictionary_key({'p': 5, 'q': 6}, 'z'),
            "Key not found"
        )

    def test_invert_dictionary_1(self):
        self.assertEqual(
            invert_dictionary({'a': 1, 'b': 2}),
            {1: 'a', 2: 'b'}
        )

    def test_invert_dictionary_2(self):
        self.assertEqual(
            invert_dictionary({'x': 5, 'y': 5}),
            {5: 'y'}
        )

    def test_invert_dictionary_3(self):
        self.assertEqual(
            invert_dictionary({'p': True, 'q': False}),
            {True: 'p', False: 'q'}
        )

    def test_recursive_sum(self):
        self.assertEqual(recursive_sum(5), 15)

    def test_fibonacci_generator(self):
        self.assertEqual(
            fibonacci_generator(7),
            [0, 1, 1, 2, 3, 5, 8]
        )


if __name__ == "__main__":
    unittest.main()