from EntryType import EntryType

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
