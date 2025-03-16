from random import randint


animals = ["🐎","🦖","🐛","🦐"]
distance = [0,0,0,0]


# generate 4 random numbers (1-20)
while all(n < 50 for n in distance):
    
    for n in range(0,4):
        speed = randint(0,10)
        distance[n] += (speed)
        print(f"{distance[n] * '.'} {animals[n]} {(50-distance[n])*'.'} 🚩")

    print("")

    


    


    

# add 4 random numbers to 4 horses
# loop until >= 100



