nums = [1,2,3,4,5,6,7,8,9]
words = ["ruthy", "daniel", "drexel", "meira", "zach", "will", "nate"]
meats=["chicken", "cow", "pig", "duck"]

def primefunction(nums):
    for num in nums:
        if num < 5:
            print("this number is under 5, ",num)
        else:
            print(f"this number is over 5, ", num)


primefunction(nums)

def stringtemp(nums):
    for num in nums:
        if num % 2 == 0 :
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

stringtemp(nums)

def friendsbackwards(words):
    container=[]
    for word in words:
        container.append(f"persons name is {word}")
        print(container)

friendsbackwards(words)

def grill(meat):
    grilledmeat = ["chicken", "burger", "bacon", "duck"]
    if meat == "chicken":
        print(f"order up! you ordered {grilledmeat[0]}")
    elif meat == "cow":
        print(f"order up! you ordered {grilledmeat[1]}")
    elif meat == "pig":
        print(f"order up! you ordered {grilledmeat[2]}")
    elif meat == "duck":
        print(f"order up! you ordered {grilledmeat[3]}")

def bbq(meats):
    for meat in meats:
        grill(meat)

bbq(meats)