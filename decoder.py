#Varvara Folimonova
def decoder(encoded_pass):
    decoded = ""
    for digit in encoded_pass:
        de_digit = int(digit)-3
        if de_digit <= 0:
            de_digit += 10
        decoded += str(de_digit)[-1]
    print(f"The encoded password is {encoded_pass}, and the original password is {decoded}.")


    