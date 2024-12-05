from enum import Enum, auto

from Agent import Agent

class TxnStatus(Enum):
    PENDING = "PENDING"
    FAILED = "FAILED"
    CANCELED = "CANCELED"
    RECEIVED = "RECEIVED"
    SETTLED = "SETTLED"


class Txn:
    def __init__(self, payer: 'Agent', recipient: 'Agent', amount: float, time_init: int, time_rec: int = None, time_set: int = None,  desc: str = ''):
        """
        Initializes a transaction.
        Args:
            payer (Agent): The agent initiating the payment.
            recipient (Agent): The agent receiving the payment.
            amt (float): The amount of the transaction.
            time_init (int): The time when the transaction was initiated.
            time_rec (int, optional): The time when the transaction is credited to the recipient. Defaults to None.
            time_set (int, optional): The time when the transaction is settled. Defaults to None.
            desc (str, optional): A description of the transaction. Defaults to ''.
        """
        self.payer = payer
        self.recipient = recipient
        self.amount = amount
        self.time_init = time_init
        self.time_rec = time_rec  # None indicates "not yet received"
        self.time_set = time_set  # None indicates "not yet settled"
        self.desc = desc

    @property
    def status(self) -> TxnStatus:
        """
        Dynamically calculates the transaction's status.
        Returns:
            TxnStatus: The transaction status (PENDING, RECEIVED, or SETTLED).
        """
        if self.time_set is not None:
            return TxnStatus.SETTLED
        elif self.time_rec is not None:
            return TxnStatus.RECEIVED
        else:
            return TxnStatus.PENDING

    def mark_received(self, current_time: int):
        """
        Marks the transaction as received by the recipient.
        Args:
            current_time (int): The time when the recipient receives provisional credit.
        """
        if self.time_rec is not None:  # Prevent overwriting if already received
            raise Exception("Transaction already received")
        self.time_rec = current_time

    def mark_settled(self, current_time: int):
        """
        Marks the transaction as settled.
        Args:
            current_time (int): The time when the transaction is fully settled.
        """
        if self.time_set is not None:  # Prevent overwriting if already settled
            raise Exception("Transaction already settled")
        self.time_set = current_time

    def __str__(self):
        """
        Returns a string representation of the transaction.
        """
        return (f"Txn(Payer: {self.payer}, Recipient: {self.recipient}, "
                f"Amount: {self.amount}, Status: {self.status.name}, "
                f"Time Init: {self.time_init}, Time Rec: {self.time_rec}, Time Set: {self.time_set})")
