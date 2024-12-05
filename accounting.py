from enum import Enum
from copy import deepcopy

class EntryType(Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

class AccountEntry:
    def __init__(self, entry_type: EntryType, amount: float, timestamp: int, description: str = ""):
        """
        Represents an entry (credit or debit) in an account.
        Args:
            entry_type (EntryType): The type of the entry (credit or debit).
            amount (float): The transaction amount (must be non-negative).
            timestamp (int): The time of the transaction.
            description (str): An optional description of the transaction.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.entry_type = entry_type
        self.amount = amount
        self.timestamp = timestamp
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the account entry.
        """
        return f"{self.entry_type}(Amount: {self.amount}, Time: {self.timestamp}, Desc: '{self.description}')"

    @property
    def value(self) -> float:
        """
        Returns the value of the entry (positive for credits, negative for debits).
        """
        return self.amount if self.entry_type == EntryType.CREDIT else -self.amount

class Account:
    def __init__(self, normal_balance: EntryType, name: str = None):
        """
        Initializes an account.
        Args:
            normal_balance (EntryType): The normal balance type (DEBIT or CREDIT).
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

    def add_entry(self, entry: AccountEntry):
        """
        Adds an entry to the account.
        Args:
            entry (AccountEntry): The entry to add.
        """
        self.entries.append(entry)

    def generate_negative(self) -> 'Account':
        """
        Generates an equivalent to the corresponding account of a counterpart by inverting the normal balance type and entry types, leaving the balance unchanged.
        Returns:
            Account: A new Account instance with the opposite normal balance type.
        """
        # Create a new account with the opposite normal balance type
        counterparty_account = Account(
            EntryType.DEBIT if self.normal_balance == EntryType.CREDIT else EntryType.CREDIT,
            name = f"{self.name} (NEGATIVE)" if self.name else None
        )
        # Copy the entries to the new account (deep copy to prevent shared references)
        counterparty_account.entries = deepcopy(self.entries)
        # Invert the entry types for the copied entries in the new account
        for entry in counterparty_account.entries:
            entry.entry_type = EntryType.DEBIT if entry.entry_type == EntryType.CREDIT else EntryType.CREDIT
        return counterparty_account

    def __str__(self):
        """
        Returns a string representation of the account.
        """
        return f"Account(Name: {self.name}, Balance: {self.balance}, Normally: {self.normal_balance})"