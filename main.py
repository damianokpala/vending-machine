
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

# Vend report

def vend_report():
    print("We have:")
    for i in vend_machine:
        print(f"This item: {i} with code {vend_machine[i]['code']} is avaliable, it costs ${vend_machine[i]['price']}, {vend_machine[i]['quantity']} quantity remaining ")
     

# product initialization

def vend_init():
    
    vend = input("Input code of what you want to purchase: ")
    vend_code = ""
    if vend == "report":
        vend_report()
    else:
        vend_code == int(vend)
    
    if product_from_code(vend_code) is False:
        vend_init()
    else:
        product = product_from_code(vend_code)
        money = payment_process(product)
        transact(money, product)

# Choosen product from code
def product_from_code(code):
    correct_code = False
    for product in vend_machine:
        if vend_machine[product]['code'] == code:
            correct_code = True
            return product
    if not correct_code:
        print("The code inserted is not correct!")
        return False


# Check Availability:

def check_availability(product):
  #  available = False
    if vend_machine[product]['quantity'] > 0:
        return True
    else:
        return False
  #  for i in vend_machine:
   #     if vend_machine[i]['code'] == code:
    #        available = True
     #       if vend_machine[i]['quantity'] > 0:
      #           return True
       #     else:
        #         print("This product is out of stock")
         #        return False
    #if not available:
     #    print("The code you input is invalid.")
      #   return False

# payment processing
def payment_process(code):
    if check_availability(code) == True:
       print("Please, insert coin:")
       coin = int(input("Insert cents: ")) * 0.01
       coin = coin + int(input("Insert nikkels: ")) * 0.05
       coin = coin + int(input("Insert dime: ")) * 0.10
       coin = coin + int(input("Insert quarter: ")) * 0.25
       return coin
    else:
       vend_init()

# transaction processing
def transact(money, product):
    vend_price = vend_machine[product]['price']
    if money >= vend_price:
        print("Transaction in process..")
        user_amount = money - vend_price
        if user_amount ==  0:
            print("Money completely used")
        else:
            print(f"You have a balance of {user_amount}")
        vend_machine[product]["price"] = new_amount
        vend_machine[product]["quantity"] = new_quantity

        vend_init()
    else:
        print("You don't have enough money")



# product dispensing


vend_init()
