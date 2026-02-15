age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ").lower()

if age >= 18:
    has_id = "yes"
    if has_id:
        print("Allowed")
    else:
        print("Need ID")
else:
    print("Too young")