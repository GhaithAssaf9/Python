import random
def randInt(min = 0,max = 100):
    if max<0:
        print('sorry we need a max number greater than 0')
    elif min > max:
        print('sorry please give a max greater than the min')
    else: 
        if max != 100 and min != 0:
            return round(random.random()*(max-min)+min)
        if min != 0:
            return round(random.random()*(100-min)+min)
        if max != 100:
            return round(random.random()*max)
    return round(random.random()*100)
print(f"This function call should always return a random number between 0 and 100 randInt() = {randInt()}")
print(f"This function call should always return a random number between 0 and 10 randInt(max = 10) = {randInt(max = 10)}")
print(f"This function call should always return a random number between 98 and 100, randInt(min = 98) = {randInt(min = 98)}")
print(f"This function call should always return a random number between 22 and 25 randInt(min = 22, max = 25) = {randInt(min = 22, max = 25)}")
print(f"This function call takes into account the edge case of min>max, randInt(min = 7, max = 2) {randInt(min = 7, max = 2)}")
print(f"This function call takes into account the edge case of 0<max, randInt(max = -5) {randInt(max = -5)}")