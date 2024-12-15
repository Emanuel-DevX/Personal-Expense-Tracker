users = [
    {'uName': "emanuel", 'age': 25, 'Weekly income': 1000.00, 'Weekly Expense': 750.67, 'Initial Assets': 10000},
    {'uName': "abel", 'age': 30, 'Weekly income': 850.00, 'Weekly Expense': 670.67, 'Initial Assets': 4500},
    {'uName': "sami", 'age': 27, 'Weekly income': 900.00, 'Weekly Expense': 680.00, 'Initial Assets': 6000},
    {'uName': "kira", 'age': 22, 'Weekly income': 1100.00, 'Weekly Expense': 800.00, 'Initial Assets': 7000},
    {'uName': "john", 'age': 35, 'Weekly income': 1200.00, 'Weekly Expense': 950.00, 'Initial Assets': 8000},
    {'uName': "nati", 'age': 28, 'Weekly income': 1050.00, 'Weekly Expense': 720.00, 'Initial Assets': 5500},
]
userAcc =[{'uName': 'emanuel', 'password': '1234'},
          {'uName': 'sami', 'password': '0945'},
          {'uName': 'kira', 'password': '5432'},
          {'uName': 'john', 'password': '3456'},
          {'uName': 'nati', 'password': '7654'},
          {'uName': 'abel', 'password': '0908'}]

def main():
    uName = login()
    userInfo(uName)
def login():
    print ("Username: ")
    uName=input()
    print ('Password: ')
    password = input()
    for x in userAcc:
        if (uName == x['uName'] and password == x["password"]):
            print("Login successful!")
            return (uName)

def userInfo(uName):
    tempUserData= getInfo(uName)
    if tempUserData:  # Check if the user data is found
        for key, value in tempUserData.items():
            print(f"{key}: {value}")


def getInfo(uName):
    for x in users:
        if uName == x['uName']:
            # Calculate weekly savings and total assets
            calculateAssets(x)  # Call the function to calculate savings and assets
            return x
    return None  # Return None if user not found


def calculateAssets(user):
    # Calculate weekly savings
    weekly_savings = user['Weekly income'] - user['Weekly Expense']
    user['Weekly Savings'] = weekly_savings

    # Calculate total assets
    user['Total Assets'] = user['Initial Assets'] + weekly_savings

main()