import unittest


# from Testing.code_files.list_03 import IntegerList


class ListTests(unittest.TestCase):
    def test_listAdd_whenInt_shouldReturnList(self):
        il = IntegerList()
        il.add(15)
        self.assertEqual([15], il.get_data())

    def test_listAdd_whenNotInt_shouldRaiseError(self):
        il = IntegerList()
        with self.assertRaises(Exception) as context:
            il.add('test')
        self.assertIsNotNone(context.exception)

    def test_listRemoveIndex_whenValidIndex_shouldReturnElement(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        self.assertEqual(1, il.remove_index(0))

    def test_listRemoveIndex_whenInvalidIndex_shouldRaiseException(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        with self.assertRaises(Exception) as context:
            il.remove_index(10)
        self.assertIsNotNone(context.exception)

    def test_listInit_whenOnlyIntsArePassed_shouldCreateFullList(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        self.assertListEqual(nums, il.get_data())

    def test_listGet_whenValidIndex_shouldReturnElementAtIndex(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        self.assertEqual(1, il.get(0))

    def test_listGet_whenInvalidIndex_shouldRaiseException(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        with self.assertRaises(Exception) as context:
            il.get(10)
        self.assertIsNotNone(context.exception)

    def test_listInsert_whenAllValid_shouldInsert(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        il.insert(0, 15)
        self.assertListEqual([15, 1, 2, 3], il.get_data())

    def test_listInsert_whenInvalidIndex_shouldRaiseError(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        with self.assertRaises(Exception) as context:
            il.insert(10, 15)
        self.assertIsNotNone(context.exception)

    def test_listInsert_whenInvalidElement_shouldRaiseError(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        with self.assertRaises(Exception) as context:
            il.insert(0, 'test')
        self.assertIsNotNone(context.exception)

    def test_listGetBiggest_shouldReturnBiggestElement(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        self.assertEqual(3, il.get_biggest())

    def test_listGetIndex_shouldReturnIndexOfElement(self):
        nums = [1, 2, 3]
        il = IntegerList(*nums)
        self.assertEqual(1, il.get_index(2))


if __name__ == '__main__':
    unittest.main()
