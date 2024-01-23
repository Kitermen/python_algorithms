quote = str(input("Kąty czy Boki?"))
if quote == "Boki":
    x = int(input("Podaj długość boku a"))
    y = int(input("Podaj długość boku b"))
    z = int(input("Podaj długość boku c"))

    sticks = [x, y, z]

    if sticks[0] < sticks[1] + sticks[2]:
        if sticks[1] < sticks[0] + sticks[2]:
            if sticks[2] < sticks[0] + sticks[1]:
                print("Z podanych boków można zbudować trójkąt")
            print("3ci bok nie spełnia założeń!")
        print("2gi bok nie spełnia założeń!")
    print("1szy bok nie spełnia założeń!")

elif quote == "Kąty":
    a = int(input("Podaj kąt alfa "))
    b = int(input("Podaj kąt beta "))
    g = int(input("Podaj kąt gamma "))

    angles = [a, b, g]
    sumOfAngles = 0

    for angle in angles:
        sumOfAngles += angle
        if angle > 178:
            print("Kąt nie może być większy niż 180 stopni!")
            exit()

    if(sumOfAngles != 180):
        print("Wprowadzono niepoprawne wartości kątów!")
        exit()
    print("Wprowadzono poprawne kąty")