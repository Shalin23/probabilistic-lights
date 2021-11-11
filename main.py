import additionTM
import subtractionTM
import multiplicationTM


def main():
    print("Welcome to the Math Tutor!")
    print()

    print("Applying 3 + 4 using a Turing Machine")
    additionTM.turing_machine("111+1111")
    print("Applying 4 + 4 using a Turing Machine")
    additionTM.turing_machine("1111+1111")
    print("Applying 4 + 5 using a Turing Machine")
    additionTM.turing_machine("1111+1011")
    print()

    print("Applying 2 - 9 using a Turing Machine")
    subtractionTM.turing_machine("00a000000000")
    print("Applying 4 - 4 using a Turing Machine")
    subtractionTM.turing_machine("0000a0000")
    print("Applying 2 - 4 using a Turing Machine")
    subtractionTM.turing_machine("00a0000")
    print("Applying 5 - 4 using a Turing Machine")
    subtractionTM.turing_machine("00000a0000")
    print()

    print("Applying 5 × 9 using a Turing Machine")
    multiplicationTM.turing_machine("##11111*111111111#")
    print("Applying 2 × 3 using a Turing Machine")
    multiplicationTM.turing_machine("##11*111#")
    print("Applying 11 × 7 using a Turing Machine")
    multiplicationTM.turing_machine("##11111111111*1111111#")
    print("Applying 5 × 16 using a Turing Machine")
    multiplicationTM.turing_machine("##11111*1111111111111111#")
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
