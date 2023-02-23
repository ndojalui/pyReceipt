
class User:
    def __init__(self,name,cost = 0) -> None:
        self.name = name
        self.cost = cost
    def addCost(self,cost):
        self.cost += cost
    def subtractCost(self,cost):
        self.cost -= cost
    def __str__(self) -> str:
        return self.name

class Item:
    def __init__(self,name,cost,users = []) -> None:
        self.name = name
        self.cost = cost
        self.users = users
    
    def addUser(self,user):
        self.users.append(user)

    def getCost(self) -> float:
        return self.cost

    def getUsers(self):
        return self.users

    def __str__(self) -> str:
        return self.name

class Receipt:    
    def __init__(self,total,tax,users,items = []) -> None:
        self.total = total
        self.tax = tax
        self.users = users
        self.items = items
        self.tempTotal = total     

    def addNewItem(self,user):
        itemName = input("\nWhat is the name of the item? ")
        itemCost = float(input("What is the cost of the item? "))
        newItem = Item(itemName,itemCost)
        newItem.addUser(user)
        self.items.append(newItem)
        
        
    
    def claimItem(self,user):
        totalCost = float(input("\nWhat was the total cost of the items this person is claiming?" ))
        user.addCost(totalCost)
        self.tempTotal -= totalCost

    def removeItem(self,user,item):
        item.addUser(user)
        print(f"\nItem cost is {item.getCost()}\n")

    def assignCosts(self):
        numUsers = len(self.users)

        for item in self.items:
            self.tempTotal -= item.getCost()
            notPaying = item.getUsers()
            usersPaying = [x for x in self.users if x not in notPaying]
            for user in usersPaying:
                user.addCost(item.getCost()/len(usersPaying))
        
        for user in self.users:
            user.addCost(self.tempTotal/numUsers)
            user.addCost(self.tax/numUsers)

    
    def printReceipt(self):
        print(f"\nThe receipt came to a total of {self.total+self.tax} after tax")      
        
        print('Here is what everyone pays...')
        totalCheck = 0
        for user in self.users:
            print(f'{user.name} pays {user.cost:.2f}')
            totalCheck+=user.cost
        
        print(f'The summation of everyones costs is {totalCheck}')

names = ["luigj","august","kyle","christian","josh"]
users = []

for name in names:
    user = User(name)
    users.append(user)


total = float(input("What is the total before tax? "))
tax = float(input("whats the total tax? "))
currentReceipt = Receipt(total,tax,users)

run = True
while run:
    print(f'\nhere is a list of users:\n{", ".join(map(str,users))}')
    
    choice = input(f"Select 0 to {len(users)-1} to claim or remove items from users, or enter 'Q' to quit ")

    if choice == "Q":
        run = False

    else:
        choice = int(choice)
        tempUser = users[choice]
        print(f"\nYou have selected {tempUser.name}")

        choice = int(input("Enter 0 to claim items, 1 to remove items "))
        match choice:
            case 0:
                currentReceipt.claimItem(tempUser)

            case 1:
                print(", ".join(map(str,currentReceipt.items))) if len(currentReceipt) > 0 else print("No Items Added!")
                choice = input(f"Select 0 to {len(currentReceipt.items)-1} to select the item\n if desired item doesnt exist, enter 'A' ")
                if choice == "A":
                    currentReceipt.addNewItem(tempUser)
                    tempItem = currentReceipt.items[-1]
                else:
                    choice = int(choice)
                    tempItem = currentReceipt.items[choice]
                currentReceipt.removeItem(tempUser,tempItem)

currentReceipt.assignCosts()
currentReceipt.printReceipt()
