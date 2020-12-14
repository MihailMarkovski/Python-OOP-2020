import unittest

# from Testing.code_files.cat_02 import Cat


class CatTests(unittest.TestCase):
    def test_catEat_shouldIncreaseWeight(self):
        name = 'test name'
        c = Cat(name)
        c.eat()
        self.assertEqual(1, c.size)

    def test_catEat_shouldFedBeTrue(self):
        name = 'test name'
        c = Cat(name)
        c.eat()
        self.assertTrue(c.fed)

    def test_catEatWhenFed_shouldRaiseException(self):
        name = 'test name'
        c = Cat(name)
        c.eat()
        with self.assertRaises(Exception) as context:
            c.eat()
        self.assertIsNotNone(context.exception)

    def test_catSleepWhenNotFed_shouldRaiseException(self):
        name = 'test name'
        c = Cat(name)
        with self.assertRaises(Exception) as context:
            c.sleep()
        self.assertIsNotNone(context.exception)

    def test_catSleep_shouldNotBeSleepy(self):
        name = 'test name'
        c = Cat(name)
        c.eat()
        c.sleep()
        self.assertFalse(c.sleepy)


if __name__ == '__main__':
    unittest.main()
