token_A_quantity = 50000
token_B_quantity = 50000
pegged_value = 1

def trade(A_trade_quantity):
    global token_A_quantity
    global token_B_quantity
    token_A_quantity += A_trade_quantity
    new_token_B_quantity_cache = 50000**2/ token_A_quantity
    B_trade_quantity = token_B_quantity - new_token_B_quantity_cache
    token_B_quantity = new_token_B_quantity_cache
    token_A_value = 50000 / token_A_quantity
    token_B_value = 50000 / token_B_quantity
    print("Quantity of B tokens returned: ", B_trade_quantity)
    print("Token A value: ", token_A_value, "USD")
    print("Token B value: ", token_B_value, "USD")

while True:
    print("Token A quantity: ", token_A_quantity)
    print("Token B quantity: ", token_B_quantity)
    print(f'Pegged value: {pegged_value} USD')
    A_trade_quantity = float(input("\n Enter quantity of A tokens to be traded: "))
    trade(A_trade_quantity)
