import random
# Amt is the change amount that will be added to a purchase for donation
amt = 0
accounts = {}
# The loss amount is calculated for external losses to determine what may be
# the gross income from donations
# The b_accounts var stores donation receipts and sums along
# with inital fees for joining the service
b_accounts = {
    "Milk and Honey": {"amt": 200000, "donated": {}, "sum": 0, "fee": 800},
    "A Baked Joint":  {"amt": 30000, "donated": {}, "sum": 0, "fee": 225},
    "Cane": {"amt": 40000, "donated": {}, "sum": 0, "fee": 267},
    "Brooklyn on U": {"amt": 100000, "donated": {}, "sum": 0, "fee": 550}
}


# Chooses a random decimal amount to donate to a company
# Simulates the calculation of spare change needed to round out a purchase
def RandomRange():
    x = [0.01, 0.12, 0.10, 0.50, 0.60, 0.75, 0.25, 0.9, 0.88]
    r = random.randint(0, len(x)-1)
    rate = x[r]
    return rate


# Function used to create a user and track spending and funds.
# Tracked donations would allow for giving back to users who donate often
def AddUser(string):
    accounts.update({string: {"acn": 123456789, "name": "N/A", "amt": 20000}})
    accounts[string]["name"] = input("Enter your Name:\n")


def main():
    # yearamt = 1400 - The amount of purchases a certain demographic may make
    # in a year
    accounts.update({"user": {"acn": 123456789, "name": "user", "amt": 20000}})
    amt = RandomRange()
    # Number of times to calculate when automatically simulating donations
    num = 0
    # Name of current company to donate to
    company = "rand"
    # Dict object storing values associated with company's account
    cval = {}
    # Boolean value that determines whether to randomize current company
    rand = False
    print("Press enter to manually choose a business to invest in.")
    print("Type doAuto to simulate multiple purchases and")
    print("donations a given number of times. If you would like")
    print("to check your balance then type balance")
    # c stores the current input for most of the main function
    c = input(">>")
    while True:
        amt = RandomRange()
        if c == "":
            print("You can donate an extra "+str(amt)+" to round out the")
            print("purchase you just made. Please type in the name of an")
            print("applicable company to donate this amount to them")
            company = input(">>")
            if company in b_accounts:
                print(company)
                cval = b_accounts[company]
                print(cval["sum"]+cval["amt"])
                namt = amt
                # rnd is a random value that determines if the current
                # purchase comes after a company loss, to help
                # simulate the unexpected expenses that a company may
                # have from external sources
                rnd = random.randint(0, 110)
                if rnd == 0:
                    lossamt = random.randint(35, 45)
                    print("-"+str(lossamt))
                print(str(namt))
                b_accounts[company]["sum"] += namt
                b_accounts[company]["sum"] = round(cval["sum"], 2)
                b_accounts[company]["donated"].update(
                    {len(cval["donated"]): namt})
                print(str(cval["sum"]+cval["amt"])+"\n")
                amt = RandomRange()
            else:
                pass
        elif c == "doAuto":
            print("doAuto- Type in a number of times to simulate a")
            print("purchase and donation")
            num = input(">>")
            num = int(num)
            print("Type in the name of the company you want to")
            print("continuously donate to "+str(num)+" times, or")
            print("press enter to randomly choose each time")
            c = input(">>")
            if c == "":
                rand = True
            else:
                company = c
            for i in range(num):
                if rand is True:
                    company, cval = random.choice(list(b_accounts.items()))
                if company in b_accounts:
                    cval = b_accounts[company]
                    print(company)
                    print(cval["sum"]+cval["amt"])
                    namt = amt
                    rnd = random.randint(0, 110)
                    if rnd == 0:
                        lossamt = random.randint(35, 45)
                        print("-"+str(lossamt))
                    print(str(namt))
                    b_accounts[company]["sum"] += namt
                    b_accounts[company]["sum"] = round(
                        b_accounts[company]["sum"], 2)
                    b_accounts[company]["donated"].update(
                        {len(b_accounts[company]["donated"]): namt})
                    print(str(cval["sum"]+cval["amt"])+"\n")
                    amt = RandomRange()
                else:
                    pass
        print("Press enter to manually choose a business to invest in.")
        print("Type doAuto to simulate multiple purchases and donations")
        print("a given number of times.")
        print("If you would like to check your balance then type balance")
        c = input(">>")
if __name__ == "__main__":
    main()
