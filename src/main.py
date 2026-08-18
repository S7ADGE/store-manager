# ==================================================
# Validates user input for numbers or strings.
# For numeric types, the entered value must
# be within the specified minimum and maximum range.
# For string type, the input is validated by
# checking whether it can be converted to a float.
# ==================================================

def givenum(name = "Value", low = -9.9e100, high = 9.9e100, Type =float):

    while True:

        try:

            x = Type(input((f"{name} : ")))

            if Type != str:

                if x >= low and x <= high:
                    return x

                else:

                    print("\tOut of range ! ", low, "to", high)

            else:

                float(x)
                return x

        except ValueError:

            print("\tInvalid number...")

# ============================================
# Validates user input for Yes/No questions.
# Converts the input to lowercase and removes
# spaces, then keeps asking until the user
# enters either 'y' or 'n'.
# ============================================

def yes_or_no(prompt):

    ans = input(prompt).lower().replace(" ", "")

    while ans not in ["y", "n"]:
        
        print("Please enter 'y' or 'n'")
        ans = input(prompt).lower().replace(" ", "")

    return ans

# =======================================
# Stores all registered customer IDs.
# Used to prevent duplicate customer IDs
# during customer registration.
# =======================================

ID_list = []

# ===========================================
# Collects customer information.
# - Gets a unique customer ID.
# - Checks the ID against existing IDs.
# - Stores the new ID in ID_list.
# - Gets the customer's name and family name.
# - Returns the information as a dictionary.
# ===========================================

def getinfo():

    ID = givenum("Enter the customer's ID", Type = str)

    while ID in ID_list:
        
        print("ID already exist !")
        ID = givenum("Enter the customer's ID", Type = str)
        
    ID_list.append(ID)

    name = input("Enter the customer's name : ").replace(" ", "").title()
    family = input("Enter the customer's family : ").replace(" ", "").title()
    return {
            "number":str(len(ID_list)) + ".",
            "ID":ID, 
            "Name":name, 
            "Family":family 
           }


# ===================================
# Returns the customer's information
# as a list of dictionary values.
# ===================================
def info():
    
    return list(getinfo().values())

# ==========================================
# Stores the items available in the store.
# Each item is stored as a key and its price
# is stored as the corresponding value.
# ==========================================

items = {}

# ==========================================
# Collects available items and their prices.
# - Gets the item name from the user.
# - Prevents duplicate items.
# - Gets and validates the item price.
# - Continues until the user chooses 'n'.
# - Returns the store inventory dictionary.
# ==========================================

def getitem():

    ans = "y"

    while ans == "y":

        while True:

            item = input("Enter the item availbale in your store : ").title()

            if item in items:
                
                print("\tThis item has already been added!")
                continue

            else:

                break

        price = givenum("Enter the price of the item ($)", 1)
        items[item] = price
        ans = yes_or_no("\t\t\t Continue for item ? (y | n) : ")
        
    return items

# ====================================
# Gets the complete list of available
# items from the store inventory.
# ====================================

available_items = getitem()

# ==============================================
# Selects a single item for the customer's cart.
# - Displays all available items and prices.
# - Checks whether the selected item exists.
# - Prevents duplicate items in the cart.
# - Gets the quantity of the selected item.
# - Returns the item, quantity, and price.
# ==============================================

def selectitem(materials):

    print ("\n__________________________________________________________\n")
    print ( "\t  ---   AVAILABLE ITEMS IN STORE   --- \n")

    for item, price in available_items.items() :

        print ( f"{item}: ${price:.2f}" , end= "\t" )
   
    print ("\n\n__________________________________________________________\n")
    
    while True:
        
        item = input("Enter the item : ").title()
        
        if item in materials:
            
            print("\tItem already exists in your cart!")
            continue
        
        elif item not in available_items:
            
            print("\tThis item is not available in store!")
            continue

        else:
            
            break 

    unit = givenum("Enter the unit of item", 1, Type = int)
    
    return {
        "Item":item, 
        "Unit":unit, 
        "Price":price
           }

# ===============================================
# Collects all items purchased by a customer.
# - Creates an empty shopping cart.
# - Allows the customer to select multiple items.
# - Prevents duplicate items.
# - Stops if all available items are selected.
# - Returns the customer's complete item list.
# ===============================================

def selectitems():
    
    item_list = []
    materials = []
    ans = "y"

    while ans == "y":

        ITEM = selectitem(materials)
        item_list.append(ITEM)
        materials.append(ITEM["Item"])

        if sorted(materials) == sorted(available_items):
            
            print("\n\t~~~~~~~ All available items have been added to the cart! ~~~~~~~\n")
            break
        
        ans = yes_or_no("\t\t Continue for item (y | n) : ")
        
    return item_list

# ==========================================
# Generates an invoice for one customer.
#
# The invoice contains:
# - Customer information
# - Customer's purchased items
#
# Returns both sections inside a dictionary.
# ==========================================

def generate_invoice():
    
    customer_info = info()
    customer_cart = selectitems()
    
    return {
        "customer": customer_info,
        "cart": customer_cart
           }

# ============================================
# Manages customer registration and invoicing.
# - Registers multiple customers if requested.
# - Generates an invoice for each customer.
# - Stores all invoices.
# - Prints every customer's bill.
# - Calculates total units and total cost.
# - Calculates total sales for each item.
# ============================================

def customers():

    all_invoices = []

    while True:

        invoice = generate_invoice()
        all_invoices.append(invoice)
        next_user = yes_or_no("\nDo you want to register another customer? (y/n): ")
        if next_user == "n":
                
            break
    
    print("\n\n==========================================================")
    print("=========      PRINTING ALL CUSTOMER BILLS      ==========")
    print("==========================================================\n")

    item_sales = {}

    for h in all_invoices:
        
        for info in h["customer"]:

            print(info, end = "\t".expandtabs(15))

        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        total_units = 0
        total_cost = 0

        for i in h["cart"]:

            line_total = i["Unit"] * i["Price"]
            total_units += i["Unit"]
            total_cost += line_total
            item_sales[i["Item"]] = item_sales.get(i["Item"], 0) + line_total
            print(i["Item"], "%10.0f"%i["Unit"], "%10.2f"%i["Price"], "%10.2f"%(i["Price"] * i["Unit"]), sep = "\t")
        
        print ("\n__________________________________________________________\n")
        print("items", "%10.0f"%total_units, "\tcost", "%10.2f"%total_cost, sep = "\t")
        print("\n\n")

    print("\n==========================================================")
    print("===========      TOTAL SALES BY ITEM      ================")
    print("==========================================================\n")

    for item, amount in item_sales.items():

        print(item,"\t:\t", "%10.2f"%amount)

# =================================
# Starts the customer registration
# and invoice generation system.
# =================================

customers()
