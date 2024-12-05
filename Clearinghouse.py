from Agent import Agent

class Clearinghouse(Agent):
    def __init__(self):
        """Initialize the Clearinghouse with an empty ledger."""
        # Call the superclass constructor
        super().__init__("Clearinghouse")
        # Initialize the ledger as an empty list of transactions
        self.txns = []

    def record_txn(self, payer: 'Agent', recipient: 'Agent', amount: float):
        """
        Records a transaction between a payer and recipient.
        Args:
            payer (Agent): The agent initiating the payment.
            recipient (Agent): The agent receiving the payment.
            amount (float): The amount being transferred.
        """
        pass

    def advance_txn(self, txn: 'Txn'):
        """
        Advances provisional credits to the recipient.
        Args:
            txn (Txn): The transaction to advance.
        """
        pass
        

    def settle_txn(self, txn: 'Txn'):
        """
        Enforces settlement of callable debts when conditions allow.
        Ensures no default occurs and balances are updated accordingly.
        Args:
            txn (Txn): The transaction to settle
        """
        pass