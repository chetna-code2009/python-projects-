def temp():
    while True:
        print("\nTEMPERATURE CONVERTER")
        print("C → Celsius to Fahrenheit")
        print("F → Fahrenheit to Celsius")
        print("K → Celsius to Kelvin")
        print("E → Exit")

        try:
            A = input("Enter choice: ").lower()

            if A == "e":
                print("Program ended.")
                break

            B = float(input("Enter temperature: "))

            if A == "c":
                print("Fahrenheit =", round((9/5 * B) + 32, 2), "°F")

            elif A == "f":
                print("Celsius =", round((5/9) * (B - 32), 2), "°C")

            elif A == "k":
                print("Kelvin =", round(B + 273.15, 2), "K")

            else:
                print("Invalid choice!")

        except:
            print("Please enter a valid number!")

temp()