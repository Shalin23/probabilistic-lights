import additionTM
import subtractionTM
import multiplicationTM


def main():
    print("Welcome to the Math Tutor!")
    print()

    print("Applying 3 + 4 using a Turing Machine")
    additionTM.turing_machine("000a0000")
    print()

    print("Applying 2 - 9 using a Turing Machine")
    subtractionTM.turing_machine("00a000000000")
    print()

    print("Applying 5 × 9 using a Turing Machine")
    multiplicationTM.turing_machine("##11111*111111111#")
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
