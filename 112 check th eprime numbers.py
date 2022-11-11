from unicodedata import digit


def is_prime(number):
    if number>1:
        for num in range(2,number):
            if (number%num==0):
                return "not prime"
        return "prime"
    return "false"

print(is_prime(11))
