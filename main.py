
# product invectory

vend_machine = {
   "snacks":  {
        "code": 2345,
        "price": 100,
        "quantity": 5
    },

    "eggs": {
        "code": 4422,
        "price": 221,
        "quantity": 4
    },

    "candy": {
        "code": 2875,
        "price": 920,
        "quantity": 3
    },

    "chips": {
        "code": 3442,
        "price": 350,
        "quantity": 6
    },

    "beverages": {
        "code": 3222,
        "price": 260,
        "quantity": 4
    },

    "cakes": {
        "code": 5012,
        "price": 300,
        "quantity": 2
    },

    "sausages": {
        "code": 4521,
        "price": 280,
        "quantity": 5
    }
}

def vend_off():
    pass

def vend_report():
    print("We have:")
    for product, details in vend_machine.items():
        print(f"This item: {product} with code {details['code']} is available, it costs ${details['price']}, {details['quantity']} quantity remaining")
    vend_init()

def product_from_code(code):
    for product, details in vend_machine.items():
        if details['code'] == code:
            return product
    print("The code inserted is not correct!")
    vend_init()
    return False

def check_availability(product):
    return vend_machine[product]['quantity'] > 0

def payment_process(product):
    if check_availability(product):
        print("Please, insert coins:")
        coin = int(input("Insert cents: ")) * 0.01
        coin += int(input("Insert nickels: ")) * 0.05
        coin += int(input("Insert dimes: ")) * 0.10
        coin += int(input("Insert quarters: ")) * 0.25
        return coin
    else:
        vend_init()

def transact(money, product):
    vend_price = vend_machine[product]['price']
    if money >= vend_price:
        print("Transaction in process...")
        user_amount = money - vend_price
        if user_amount == 0:
            print("Money completely used")
        else:
            print(f"You have a balance of {user_amount}")
        vend_machine[product]["quantity"] -= 1

        vend_init()
    else:
        print("You don't have enough money")
        vend_init()

def vend_init():
    vend = input("Input code of what you want to purchase: ")

    if vend == "report":
        vend_report()
    elif vend == "off":
        vend_off()
    else:
        vend_code = int(vend)
    
        product = product_from_code(vend_code)
        if product:
            money = payment_process(product)
            transact(money, product)

vend_init()
