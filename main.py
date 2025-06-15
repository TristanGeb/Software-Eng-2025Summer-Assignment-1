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
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
        WHY ARE SNADWICH_SIZE AND ORDER_INGREDIENTS BOTH PASSED    WHHHHHYYYYY WORLD
        I am should only need one not both. but which is better"""
        """match sandwich_size:
            case "small":
            case "medium":
            case "large":
            case _:
                print("this should never run")
                pause = input(f"error in make_sandwich\nsandwich_size=={sandwich_size}\n")
"""

### Make an instance of SandwichMachine class and write the rest of the codes ###
mySandwichMachine = SandwichMachine(resources)
userWantsToExit = False
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
            continue
        case _:
            print(f"\"{userInput}\" is a invalid input")
            continue
    #only if input is large medium or small should the rest of this iteration of the loop run
    if not (mySandwichMachine.check_resources(recipes[sandwichSize]["ingredients"])):
        print("not enough resources")
        continue
    #mySandwichMachine.check_resources()
    #end of loop