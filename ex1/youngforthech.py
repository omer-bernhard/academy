
dacimal = int (input("enter a dacimal"))

bit_size = int(input("enter bit size"))


def dacimal_binary(num , length):
    binary = bin(num)
    binary = binary[2:]
    while len(binary) < length:
        binary = "0" + binary
    return binary


   
def complete_to_two(binary):
    revrese_bin = ""
    for i in range(len(binary)):
        if binary[i] == "1":
            revrese_bin += "0"
        else:
            revrese_bin += "1"
    revrese_bin = int(revrese_bin,2)+1
    return dacimal_binary(revrese_bin,bit_size)



res =dacimal_binary(dacimal, bit_size)
print(complete_to_two(res))

