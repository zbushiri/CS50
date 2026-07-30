def main():
    number = get_number()
    meow(3)


def get_number():
    while True:
        n = int(input("What's n? "))


def meow(n):
    for _ in range(n):
        print("meow")


main()
