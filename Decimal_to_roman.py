def Decimal_to_roman(num):
  
    if not 0 < num < 4000:
        raise ValueError("The number must be within the range of 1 to 3999")

    decimal_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    result = ''
    for value, numeral in sorted(decimal_numerals.items(), reverse=True):
        while num >= value:
            result += numeral
            num -= value

    return result

def main():
    while True:
        try:
            num = int(input("Enter a number (between 1 and 3999): "))
            if not 0 < num < 4000:
                print("The number must be within the range of 1 to 3999.")
                continue
            break
        except ValueError:
            print("Please enter only integer numbers.")

    roman_numeral = Decimal_to_roman(num)
    print(f"The corresponding Roman numeral is: {roman_numeral}")

if __name__ == "__main__":
    main()
