#Tristan Gebeaux
### Data ###
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}
"""could be turned into its own class but would increase overhead\n
[small] [cost]
        [ingredients]   {bread,ham,cheese}
[medium] [cost]
        [ingredients]   {bread,ham,cheese}
[large] [cost]
        [ingredients]   {bread,ham,cheese}
"""

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:
    #will create new dictionary to protect orginal input_resrouces values from changing
    def __init__(self, input_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = {
            #TODO loop for options in recipe dictionary/ or make it mandatory as input
            "bread": input_resources["bread"],  ## slice
            "ham": input_resources["ham"],  ## slice
            "cheese": input_resources["cheese"],  ## ounces
        }
    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients.keys():
            if(0 > self.machine_resources[item]-ingredients[item]):
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted in pennies. 1.25 is returned as 125
        this funciton also ask the user for the coins
        funciton does not check if valid input
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 100 * int(input("How many dollar coins:"))
        total = total + 50 * int(input("How many half dollars:"))
        total = total + 25 * int(input("How many quarters:"))
        total = total + 10 * int(input("How many nickels:"))
        total = total + 5 * int(input("How many dimes:"))
        total = total + int(input("How many pennies:"))
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if (coins < 100 * cost):  # if not enough coins
            print(f"Sorry that is not enough money. you will be refunded. cost is {cost}$"
                  f" and you inserted {coins} cents\n")
            return False
        if (coins == 100 * cost):
            print("exact amount inserted\n")
        else:
            print(f"here is {(coins - cost * 100) / 100} in change\n")
        return True
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
        WHY ARE SNADWICH_SIZE AND ORDER_INGREDIENTS BOTH PASSED    WHHHHHYYYYY WORLD  WHAT IS YOUR REASON
        I am should only need one not both. but which is better"""
        for item in order_ingredients.keys():#no need to make sure all items in order_ingredients are in present in the machine
            self.machine_resources[item] = self.machine_resources[item] - order_ingredients[item]
### Make an instance of SandwichMachine class and write the rest of the codes ###
mySandwichMachine = SandwichMachine(resources)
userWantsToExit = False
sandwichSize = "NA"

while(userWantsToExit == False):
    #get user input
    userInput = input("What would you like?(small/medium/ large/ off/ report:")#did a quick google search ot make sure i got the syntax right
    userRequest=0
    """
    if the below is changed then the possilbe values for sadnwich_size in SandwichMachine.make_sandwich must also be changed
    0=default value\n
    1=small\n
    2=medium\n
    3=large\n
    """
    #TODO loop through options in the recipes dictionary instead
    match userInput:
        case "small"|"Small"|"SMALL":
            print("you requested a small sandwich")
            userRequest = 1
            sandwichSize= "small"
        case "medium"|"Medium"|"MEDIUM":
            print("you requested a medium sandwich")
            userRequest = 2
            sandwichSize = "medium"
        case "large"|"Large"|"LARGE":
            print("you requested a large sandwich")
            userRequest = 3
            sandwichSize = "large"
        case "off"|"Off"|"OFF":
            print("you entered off")
            break
        case "report"|"Report"|"REPORT":
            print("you entered report")
            for item in mySandwichMachine.machine_resources.keys():
                print(f"{item}:{mySandwichMachine.machine_resources[item]}")
            continue
        case _:
            print(f"\"{userInput}\" is a invalid input")
            continue
    #only if input is large medium or small should the rest of this iteration of the loop run
    if not (    mySandwichMachine.check_resources(  recipes[sandwichSize]["ingredients"]  )    ):
        print("not enough resources")
        continue

    coinTotal = mySandwichMachine.process_coins()
    ans=mySandwichMachine.transaction_result(coinTotal,recipes[sandwichSize]["cost"])
    #1.25$  is given as 125
    if not (ans):#if not enough coins
        continue

    #make sandwich
    mySandwichMachine.make_sandwich(  sandwichSize  ,  recipes[sandwichSize]["ingredients"]  )
    print(f"Here is your {sandwichSize} sandwich. Bon appetit!")


    #end of loop