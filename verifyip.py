def octet_verify(new_address):
    answer = True
    for octet in new_address:
        if octet_is_int(octet) == False:
            print("please enter only integers for the address")
            answer = False
        elif int(octet) < 0 or int(octet) > 255:
            print("Please enter addresses between 0 and 255")
            answer = False
            break
    return answer


def octet_is_int(octet):
    try:
        type(int(octet))
    except ValueError:
        return False
    else:
        return True

def verify_ip(address):
    # address = input("Enter IP Address (Type x to End):  ")
    # make the address a list with the four octets using the period as the splitter
    new_address = address.split(".")
    if address.upper() == "X":
        print("Thank you for trying the program")

    # Verify the length of the address is correct
    elif len(new_address) != 4:
        print("Sorry, this address is not the correct length or is not a proper address")

    elif octet_verify(new_address):
        print(f"{address} is a valid IP address")
    else:
        print(f"{address} is not a valid IP address")

address = 'y'

while address.upper() != 'X':
    address = input("Enter IP Address (Type x to End):  ")
    verify_ip(address)
