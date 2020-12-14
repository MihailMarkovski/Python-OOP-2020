import unittest


# from Testing.code_files.account_03E import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account(owner='Steve', amount=100)

    def test_add_transaction_valid(self):
        self.acc.add_transaction(50)
        self.assertEqual([50], self.acc.transactions)

    def test_add_transaction_invalid(self):
        with self.assertRaises(Exception) as context:
            self.acc.add_transaction('test')
        self.assertIsNotNone(context.exception)

    def test_balance(self):
        self.acc.add_transaction(25)
        self.assertEqual(125, self.acc.balance)

    def test_str(self):
        expected = 'Account of Steve with starting amount: 100'
        self.assertEqual(expected, str(self.acc))

    def test_repr(self):
        expected = 'Account(Steve, 100)'
        self.assertEqual(expected, repr(self.acc))

    def test_len(self):
        self.acc.add_transaction(25)
        self.acc.add_transaction(25)
        self.assertEqual(2, len(self.acc))

    def test_get_item(self):
        self.acc.add_transaction(25)
        self.acc.add_transaction(50)
        self.assertEqual(50, self.acc[1])

    def test_reversed(self):
        self.acc.add_transaction(25)
        self.acc.add_transaction(50)
        expected = [50, 25]
        self.assertListEqual(expected, list(reversed(self.acc)))

    def test_gt(self):
        acc2 = Account(owner='Walter', amount=50)
        self.assertGreater(self.acc, acc2)
        self.assertTrue(self.acc.balance > acc2.balance)

    def test_ge(self):
        acc2 = Account(owner='Walter', amount=100)  # тази тъпня държи последния тест, иска да са с равни суми
        self.assertGreaterEqual(self.acc, acc2)
        self.assertTrue(self.acc.balance >= acc2.balance)

    def test_lt(self):
        acc2 = Account(owner='Walter', amount=150)
        self.assertLess(self.acc, acc2)
        self.assertTrue(self.acc.balance < acc2.balance)

    def test_le(self):
        acc2 = Account(owner='Walter', amount=150)
        self.assertLessEqual(self.acc, acc2)
        self.assertTrue(self.acc.balance <= acc2.balance)

    def test_eq(self):
        acc2 = Account(owner='Walter', amount=100)
        self.assertEqual(self.acc, acc2)
        self.assertTrue(self.acc.balance == acc2.balance)

    def test_ne(self):
        acc2 = Account(owner='Walter', amount=50)
        self.assertNotEqual(self.acc, acc2)
        self.assertTrue(self.acc.balance != acc2.balance)

    def test_add(self):
        acc2 = Account(owner='Walter', amount=50)
        acc3 = self.acc + acc2
        expected = [f'{self.acc.owner}&{acc2.owner}', self.acc.amount + acc2.amount,
                    self.acc.transactions + acc2.transactions]
        self.assertListEqual(expected, [acc3.owner, acc3.amount, acc3.transactions])

    def test_validate_transaction_valid(self):
        result = Account.validate_transaction(self.acc, 50)
        expected = 'New balance: 150'
        self.assertEqual(expected, result)

    def test_validate_transaction_invalid(self):
        with self.assertRaises(Exception) as context:
            Account.validate_transaction(self.acc, -200)
        self.assertIsNotNone(context.exception)

    def test_validate_transaction_static(self):
        # import inspect
        # self.assertTrue(isinstance(inspect.getattr_static(self.acc, 'validate_transaction'), staticmethod))
        import types
        self.assertTrue(isinstance(self.acc.validate_transaction, types.FunctionType))


if __name__ == '__main__':
    unittest.main()
