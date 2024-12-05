from Agent import Agent
from accounting import Account, EntryType
from Txn import Txn, TxnStatus
from Clearinghouse import Clearinghouse

def main():
    # Create Clearinghouse
    clearinghouse = Clearinghouse()

    # Create agents
    alice = Agent("Alice")
    bob = Agent("Bob")

    # Create accounts
    alice_account = Account(EntryType.CREDIT, name="Alice's Account")
    bob_account = Account(EntryType.CREDIT, name="Bob's Account")

    # Create a transaction
    txn = Txn(alice, bob, 100, 0, desc="Example payment from Alice to Bob")

    # Print the transaction status
    print(f"Transaction status: {txn.status}")
    assert txn.status == TxnStatus.PENDING

    # Mark the transaction as received
    print("Marking transaction as received...")
    txn.mark_received(1)
    assert txn.status == TxnStatus.RECEIVED



if __name__ == "__main__":
    main()