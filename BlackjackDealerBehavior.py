def next_move(hand):
    total = 0
    flag = False
    for char in hand:
        if char.isdigit():
            if char == "0":
                total += 10
            elif int(char) < 10:
                total += int(char)

            else:
                print("Invalid character detected. Please check input string.")  
        elif isinstance(char, str):
            if char in ("J", "Q", "K"):
                total += 10
            elif char == "A":
                flag = True
            else:
                print("Invalid character detected. Please check input string.")

    if flag:
        if (total + 11) > 16 and (total + 11) < 21:
            total += 11
        else:
            total += 1
    
    if total < 17:
        action = "Hit"
    elif total > 21:
        action = "Bust"
    else:
        action = "Stay"
    return action

print(next_move("2309"))