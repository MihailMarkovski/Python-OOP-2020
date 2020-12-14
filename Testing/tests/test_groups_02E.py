import unittest

# from Testing.code_files.groups_02E import Person, Group


class TestPerson(unittest.TestCase):
    def setUp(self):
        Person.id_counter = 0
        self.person_1 = Person('Vince', 'Carter')
        self.person_2 = Person('Charles', 'Barkley')

    def test_personAutoincrementId_shouldIncrementProperly(self):
        self.assertEqual(0, self.person_1.id)
        self.assertEqual(1, self.person_2.id)

    def test_personAdd_shouldReturnNewInstance(self):
        expected = [self.person_1.name, self.person_2.surname]
        person_3 = self.person_1 + self.person_2
        self.assertListEqual(expected, [person_3.name, person_3.surname])

    def test_personRepr_shouldReturnProperString(self):
        expected = f"Person 0: Vince Carter"
        self.assertEqual(expected, repr(self.person_1))

    def test_personStr_shouldReturnProperString(self):
        expected = 'Vince Carter'
        self.assertEqual(expected, str(self.person_1))


class TestGroup(unittest.TestCase):
    def setUp(self):
        Person.id_counter = 0
        self.person_1 = Person('Vince', 'Carter')
        self.person_2 = Person('Charles', 'Barkley')
        people_1 = [self.person_1, self.person_2]
        self.group_1 = Group('Group1', people_1)

        self.person_3 = Person('Steve', 'Nash')
        self.person_4 = Person('Scottie', 'Pippen')
        people_2 = [self.person_3, self.person_4]
        self.group_2 = Group('Group2', people_2)

    def test_groupLen_shouldReturnTheLengthOfTheGroup(self):
        self.assertEqual(2, len(self.group_1))

    def test_groupRepr_shouldReturnProperString(self):
        expected = 'Group Group1 with members Vince Carter, Charles Barkley'
        self.assertEqual(expected, repr(self.group_1))

    def test_groupStr_shouldReturnProperString(self):
        expected = 'Group Group1 with members Vince Carter, Charles Barkley'
        self.assertEqual(expected, str(self.group_1))

    def test_groupGetItem_shouldReturnItemAtIndex(self):
        expected = f"Person 1: Charles Barkley"
        self.assertEqual(expected, self.group_1[1])

    def test_groupAdd_shouldCreateNewInstance(self):
        group_3 = self.group_1 + self.group_2
        expected = [self.group_1.name, self.group_1.people + self.group_2.people]
        self.assertListEqual(expected, [group_3.name, group_3.people])


if __name__ == '__main__':
    unittest.main()
# get item with invalid index
