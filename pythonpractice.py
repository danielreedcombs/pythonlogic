nums = [1,2,3,4,5,6,7,8,9]
words = ["ruthy", "daniel", "drexel", "meira", "zach", "will", "nate"]
meats=["chicken", "cow", "pig", "duck"]
luna = ["luna", "not walked", "hungry"]
frogdog = ["frog dog", "not walked", "hungry"]
frogpuppy = ["frog puppy", "not walked", "hungry"]
dogs= [luna, frogdog, frogpuppy]
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

def dogwalker(puppy):
    if puppy[1] == "not walked":
        puppy[1] = "walked"
        print(f"{puppy[0]} has been walked")
    else:
        print(f"this dog has been walked")

dogwalker(luna)

def dogfeeder(puppy):
    if puppy[2] == "hungry":
        puppy[2] = "full puppy tummy!"
        print(f"{puppy[0]} has a {puppy[2]}")
    else:
        print (f"{puppy[0]} is not hungry")

def great_dog_caretaker(puppy):
    dogwalker(puppy)
    dogfeeder(puppy)

great_dog_caretaker(frogdog)

def okay_dog_caretaker(puppy):
    dogwalker(puppy)

okay_dog_caretaker(frogpuppy)
