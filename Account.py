import copy

from EntryType import EntryType
from AccountEntry import AccountEntry 

class Account:
    def __init__(self, normal_balance: EntryType, name: str = None):
        """
        Initializes an account.
        Args:
            normal_balance (NormalBalance): The normal balance type (DEBIT or CREDIT).
            name (str, optional): An optional name for the account.
        """
        self.normal_balance = normal_balance
        self.name = name
        self.entries = []  # List of AccountEntry objects

    @property
    def balance(self) -> float:
        """
        Calculates the account's balance based on its entries.
        Returns:
            float: The current balance of the account.
        """
        net_credits = sum(entry.value for entry in self.entries)
        return net_credits if self.normal_balance == EntryType.CREDIT else -net_credits

    def add_entry(self):
        pass

    def generate_negative(self) -> 'Account':
        """
        Generates the negative account equivalent to the cooresponding account of a counterpart.
        Returns:
            Account: A new Account instance with the opposite normal balance.
        """
        counterparty_account = Account(
            EntryType.DEBIT if self.normal_balance == EntryType.CREDIT else EntryType.CREDIT,
            name = f"{self.name} (NEGATIVE)" if self.name else None
        )
        counterparty_account.entries = copy.deepcopy(self.entries)
        return counterparty_account

    def __str__(self):
        """
        Returns a string representation of the account.
        """
        return f"Account(Name: {self.name}, Balance: {self.balance}, Normally: {self.normal_balance})"