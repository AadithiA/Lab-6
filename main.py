def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main():
    print(menu())
    option = input("Please enter an option:")
    print(option)
    if option=='1':
        UserChoice1 = input("Please enter your password to encode:")
        print(UserChoice1)
        print("Your password has been encoded and stored!")
    elif option =='2':
        print("a")
    elif option =='3':
        break
if __name__ == "__main__":
    main()



