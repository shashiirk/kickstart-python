import re

def main():

    print(f"\n{7*'='} E-MAIL SLICER {7*'='}")

    while True:
        pattern = r"^([a-z0-9]{1}[a-z0-9-_.]+)@([a-z0-9]+[.][a-z0-9]+[.]?[a-z0-9]{2,6})$"
        string = input("\nEnter your email:> ")

        mail = re.findall(pattern,string)

        if mail:
            print(f"Username: {mail[0][0]}")
            print(f"Domain: {mail[0][1]}")
        else:
            print("Please provide a valid e-mail address!")
        
        check = input("\nTry again...?(Y/N) :").upper() == 'Y'
        if check:
            continue
        else:
            print("\nYou terminated...Bye!")
            break

if __name__ == "__main__":
    main()
