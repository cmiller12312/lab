class Account():
    def __init__(self, name: str) -> None:
        '''
        Initializes account
        
        :param name: account name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Deposits amount into account
        
        :param amount: amount you wihs to deposit
        :return Will return True if successful and False if not
        '''
        if amount > 0:
            self.__account_balance + amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        '''
        withdraws amount from account
        
        :param amount: amount you wish to withdraw
        :return Will return True if successful and False if not
        '''
        if amount > 0　and amount <= self.__account_balance:
            self.__account_balance - amount
            return True
        return False

    def get_balance(self) -> float:
        '''
        returns the account balance
        
        :return account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        returns the account name
        
        :return Account name
        '''
        return self.__account_name
