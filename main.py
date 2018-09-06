con = True
while con:
    s = input("Type your simple equation: ")
    ans = 0
    for i in range(0, len(s)):
        if s[i] == "+":
            ans = int(s[0:i]) + int(s[i+1:])
            break
        elif s[i] == "-":
            ans = int(s[0:i]) - int(s[i + 1:])
            break

        # The and is used so that the exponent is not mistaken
        elif s[i] == "*" and s[i:i+2] != "**":
            ans = int(s[0:i]) * int(s[i + 1:])
            break

        # The and is used so that the floor division is not mistaken
        elif s[i] == "/" and s[i:i+2] != "//":
            sec = int(s[i + 1:])

            # Checking if its divided by zero
            if sec == 0:
                print("Can't divide by 0")
                break

            ans = int(s[0:i]) / sec
            break
        elif s[i] == "%":
            ans = int(s[0:i]) % int(s[i + 1:])
            break
        elif s[i:i+2] == "//":
            sec = int(s[i + 2:])

            if sec == 0:
                print("Can't divide by 0")
                break

            ans = int(s[0:i]) // sec
            break
        elif s[i:i+2] == "**":
            ans = int(s[0:i]) ** int(s[i + 2:])
            break
    print(s + "=" + str(ans))
    newS = input("Would you like to perform another calculation? Y or N: ")
    if newS == "Y":
        con = True
    else:
        con = False
