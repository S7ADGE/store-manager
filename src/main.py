#=================================Validates user input for numbers within a specified range and type.=================================

def givenum(name = "Value", low = -9.9e100, high = 9.9e100, Type =float):

    while True:

        try:

            x = Type(input((f"{name} : ")))

            if Type != str:

                if x >= low and x <= high:
                    return x

                else:

                    print("Out of range ! ", low, "to", high)

            else:

                float(x)
                return x

        except:

            print(" Invalid number...")

#=================================Validates user input for yes or no responses.=================================

def yes_or_no(prompt):

    ans = input(prompt).lower()

    while ans not in ["y", "n"]:
        
        print("Please enter 'y' or 'n'")
        ans = input(prompt).lower()

    return ans

#=================================Validates customer information input and checks for duplicates ID=================================

ID_list = []

def getinfo():

    ID = givenum("Enter the customer's ID", Type = str)

    while ID in ID_list:
        
        print("ID already exist !")
        ID = givenum("Enter the customer's ID", Type = str)
        
    ID_list.append(ID)

    name = input("Enter the customer's name : ")
    family = input("Enter the customer's family : ")
    return {
            "ID":ID, 
            "Name":name, 
            "Family":family 
           }

#=================================Returns customer information=================================

def info():
    
    return list(getinfo().values())

#=================================Collect the items purchased by the customer, along with their quantities and prices=================================

items = ["cpu", "gpu", "mb", "ram", "ssd", "fan", "case"] #---Example of available items in store, you can change it as you want---

def getitem(items, materials):

    print ("\n_____________________________________________________\n")
    print ( "\t---   AVAILABLE ITEMS IN STORE   --- \n")

    for h in items :

        print ( h , end= "\t" )
   
    print ("\n\n_____________________________________________________\n")
    
    while True:
        
        item = input("Enter the item : ").lower()
        
        if item in materials:
            
            print("Item already exists in your cart!")
            continue
        
        elif item not in items:
            
            print("\tThis item is not available in store!")
            continue
        
        else:
            
            break 

    unit = givenum("Enter the unit of item", 1, Type = int)
    price = givenum("Enter the price of item ($)", 1)
    return {
        "Item":item, 
        "Unit":unit, 
        "Price":price
           }

#=================================Returns the list of items purchased by the customer=================================

def getitems():
    
    item_list = []
    materials = []
    ans = "y"

    while ans == "y":

        ITEM = getitem(items, materials)
        item_list.append(ITEM)
        materials.append(ITEM["Item"])
        ans = yes_or_no("\t\t Continue for item (y | n) : ")
        
    return item_list

#=================================Generate invoice for the customer=================================

def generate_invoice():
    
    customer_info = info()
    customer_cart = getitems()
    
    return {
        "customer": customer_info,
        "cart": customer_cart
           }

#=================================Manage customer registration and invoicing=================================

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
            print(i["Item"], "%9.0f"%i["Unit"], "%9.2f"%i["Price"], "%9.2f"%(i["Price"] * i["Unit"]), sep = "\t")
        
        print ("\n__________________________________________________________\n")
        print("items", "%9.0f"%total_units, "\tcost", "%9.2f"%total_cost, sep = "\t")
        print("\n\n")

    print("\n==========================================================")
    print("===========      TOTAL SALES BY ITEM      ================")
    print("==========================================================\n")

    for item, amount in item_sales.items():

        print(item,"\t:\t", "%9.2f"%amount)

#=================================Call customers()=================================

customers()
