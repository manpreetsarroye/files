withdraw,balance=map(str,input().split())
withdraw=int(withdraw)
balance=float                                                                   (balance)
if withdraw%5==0 and withdraw+0.50<=balance:
    print(balance-withdraw-0.50)
else:
    print(balance)
