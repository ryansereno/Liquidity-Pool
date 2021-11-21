#token_A_quantity = 50000
#token_B_quantity = 50000
#pegged_value = 1

#print("Token A quantity: ", token_A_quantity)
#print("Token B quantity: ", token_B_quantity)
#print(f'Pegged value: {pegged_value} USD')
def trade(A_trade_quantity, token_A_quantity, token_B_quantity):
    token_A_quantity += A_trade_quantity
    new_token_B_quantity_cache = 50000**2/ token_A_quantity
    B_trade_quantity = token_B_quantity - new_token_B_quantity_cache
    token_B_quantity = new_token_B_quantity_cache
    token_A_value = token_A_quantity / 50000
    token_B_value = token_B_quantity / 50000
    print("Quantity of B tokens returned: ", B_trade_quantity)
while True:
    token_A_quantity = 50000
    token_B_quantity = 50000
    pegged_value = 1
    print("Token A quantity: ", token_A_quantity)
    print("Token B quantity: ", token_B_quantity)
    print(f'Pegged value: {pegged_value} USD')
    A_trade_quantity = float(input("\n Enter quantity of A tokens to be traded: "))
    trade(A_trade_quantity, token_A_quantity, token_B_quantity)
