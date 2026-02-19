

#ItemInCart = 0

#if ItemInCart != 2:

  #  raise Exception("Cart items count is not matching")


#if ItemInCart != 2:
 #  pass
#assert (ItemInCart == 2)




try:
    with open("test.txt", "r") as reader:
        reader.read()
except:
    print("try block failed")

try:
    with open("test.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")

