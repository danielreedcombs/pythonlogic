nums = [1,2,3,4,5,6,7,8,9]
words = ["ruthy", "daniel", "drexel", "meira", "zach", "will", "nate"]
meats=["chicken", "cow", "pig", "duck"]
luna = ["luna", "not walked", "hungry"]
frogdog = ["frog dog", "not walked", "hungry"]
frogpuppy = ["frog puppy", "not walked", "hungry"]
foofie = ["Daniel hates that", "Daniel likes that", "I dosent mind that", "Foof doesnt concern herself with such pea brain things"]
daniel = ["The foof hates that", "Ruthanne likes that", "foofie dosent mind that", "Daniel doesnt think about that"]
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

def opinion_generator(person,thing):
    if thing == "traffic" and person == daniel:
     print(daniel[2])
    elif thing ==  "traffic" and person == foofie:
     print(foofie[0])
    elif thing == "luna" and person == foofie:
        print(foofie[1])
    elif thing == "luna" and person == daniel:
        print(daniel[1])
    elif thing == "work" and person == foofie:
        print(foofie[1])
    elif thing == "work" and person == daniel:
        print(danie[0])
    elif thing ==  "babies" and person == foofie:
        print(foofie[1])
    elif thing == "babies" and person == daniel:
        print(daniel[2])
    elif person == daniel:
        print(daniel[3])
    elif person == foofie:
        print(foofie[3])
    else:
        print("i dont know that person")
opinion_generator(daniel,"traffic")
opinion_generator(foofie, "trafic")
opinion_generator(foofie, "babies")
opinion_generator(daniel, "luna")
opinion_generator(foofie, "two chainz")