from entity.Account import Account

class HMBankList:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def list_accounts(self):
        return sorted(self.accounts, key=lambda acc: acc.customer_name.lower())

class HMBankSet:
    def __init__(self):
        self.accounts = set()

    def add_account(self, account: Account):
        self.accounts.add(account)

    def list_accounts(self):
        return sorted(self.accounts, key=lambda acc: acc.customer_name.lower())

class HMBankMap:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number: int) -> Account:
        return self.accounts.get(account_number)

    def list_accounts(self):
        return sorted(self.accounts.values(), key=lambda acc: acc.customer_name.lower())

