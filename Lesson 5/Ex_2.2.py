while True:
    num = input("Enter a number please: ")
    if num.lower() == "stop":
        confirm = input("Are you sure you want to stop? Write stop again: ")
        if confirm.lower() == "stop":
            print("Thank you!")
            break
        else:
            continue

    num = int(num)
    try:
        prev_num
    except NameError:
        prev_num = num -1
    
    if num > prev_num:
        prev_num = num
    else:
        print(f"The number {num} is smaller than {prev_num}. Better luck next time <3")
        break

