def main():
    greeting = input("Привествие")
    res = value(greeting)
    print(f"$(res)")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("здравствуйте"):
        return 0
    if greeting.startswith("3"):
       return 20
    else:
        return 100

if __name__ == "__main__":
    main()

