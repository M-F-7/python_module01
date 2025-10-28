# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if isinstance(new_account, Account) == False:
            return False
        try:
            self.accounts.index(new_account)
            return False
        except ValueError:
            pass
        if len(dir(new_account)) % 2:
            return False
        
        is_zip_or_addr:bool = False
        is_info:int = 0
        for att in new_account:
            if str(att).startwith("b"):
                return False
            if str(att) == "zip" or str(att) == "addr":
                is_zip_or_addr = True
            if str(att) == "name" or "id" or "value":
                if str(att) == "name":
                    if isinstance(att, str) == False:
                        return False
                elif att == "id":
                    if isinstance(att, int) == False:
                        return False
                elif att == "value":
                    if isinstance(att, int) == False and isinstance(att, float) == False:
                        return False
                is_info += 1 
        if is_zip_or_addr == False:
            return False
        if is_info != 3:
            return False
        self.accounts.append(new_account)
        return True



    def transfer(self, origin:str, dest:str, amount:float):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if isinstance(origin, str) == False:
            return False
        if isinstance(dest, str) == False:
            return False
        if origin == dest:
            return True
        if (amount < 0):
            return False
        if amount > origin.value:
            return False


    def fix_account(self, name:str):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        try:
            if isinstance(name, str) == False:
                return False
            self.accounts.index(name)
        except ValueError:
            return False

    
    

    #print([name for name in dir(math) if not name.startswith("__")])
    
    # //The verification in add only checsk the type of the
# new_account and if there is no account among the ones already in Bank instance with
# the same name.
# A transaction is invalid if amount < 0 or if the amount is larger than the balance of
# the account
# A transfer between the same account
# (bank.transfer(’Wiliam John’, ’William John’)) is valid but there is no fund move-
# ment