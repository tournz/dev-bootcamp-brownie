from brownie import MyFirstContract, config, accounts, network

def main():
    account = accounts.add(config["wallets"]["from_key"]) or accounts(0)
    my_first_contract = MyFirstContract[-1]
    tx = my_first_contract.setNumber(123456,{'from': account})
    tx.wait(1)
    print("Number is", my_first_contract.getNumber({'from': account}))
    print("Number is", my_first_contract.sumFunction(876544,{'from': account}))
