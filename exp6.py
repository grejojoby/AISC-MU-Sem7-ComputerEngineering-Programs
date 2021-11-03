print("Types of clothes:")
print("1. woolen")
print("2. silk")
print("3. jeans")
n = input("Enter type of cloth: ")

print("\nLevel of dirt:")
print("1. very dirty")
print("2. medium dirty")
print("3. not dirty")
m = input("Enter level of dirt: ")

def result(n,m):
    if(n=='woolen' and m=='very dirty'): #1
        print("\nFor Woolen clothes and level of dirt very dirty ")
        print("Wash duration: Long")
    elif(n=='woolen' and m=='medium dirty'): #2
        print("\nFor Woolen clothes and level of dirt medium dirty ")
        print("Wash duration: Medium")
    elif(n=='woolen' and m=='not dirty'): #3
        print("\nFor Woolen clothes and level of dirt not dirty ")
        print("Wash duration: Average")
    elif(n=='silk' and m=='very dirty'): #4
        print("\nFor Silk clothes and level of dirt very dirty ")
        print("Wash duration: Long")
    elif(n=='silk' and m=='medium dirty'): #5
        print("\nFor Silk clothes and level of dirt medium dirty ")
        print("Wash duration: Medium")
    elif(n=='silk' and m=='not dirty'): #6
        print("\nFor Silk clothes and level of dirt not dirty ")
        print("Wash duration: Average")
    elif(n=='jeans' and m=='very dirty'): #7
        print("\nFor Jeans clothes and level of dirt very dirty ")
        print("Wash duration: Long")
    elif(n=='jeans' and m=='medium dirty'): #8
        print("\nFor Jeans clothes and level of dirt medium dirty ")
        print("Wash duration: Medium")
    elif(n=='jeans' and m=='not dirty'): #9
        print("\nFor Jeans clothes and level of dirt not dirty ")
        print("Wash duration: Average")

result(n,m)