class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        self._transactions = transactions

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self.transactions.append(amount)
            return
        raise ValueError('please use int for amount')

    @property
    def balance(self):
        return int(self.amount + sum(self.transactions))

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, index):
        return self.transactions[index]

    def __reversed__(self):
        return reversed(self.transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc_u = Account(owner=f'{self.owner}&{other.owner}', amount=self.amount + other.amount)
        acc_u._transactions.extend(self.transactions + other.transactions)
        return acc_u
        # self.owner += '&' + other.owner
        # self.amount += other.amount
        # self._transactions += other.transactions

    @staticmethod
    def validate_transaction(accout, amount_to_add):
        if not accout.balance + amount_to_add >= 0:
            raise ValueError('sorry cannot go in debt!')
        accout.add_transaction(amount_to_add)
        return f'New balance: {accout.balance}'
