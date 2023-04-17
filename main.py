import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
#rare the value, higher the winning


def check_winnings(columns, lines, bet, values):
    winnings = 0
    #will return the amount they won
    winning_lines = []
    #returns what line they won on
    for line in range(lines):
        # it will go from 0 to number of lines user inputs, hence used lines. We could also use range(0, lines)
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            #we added +1 because the value starts from 0 and that's not gonna give us cirrect value

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #making an algorithm to select random value from symbols_count for slot machine
    for symbol, symbol_count in symbols.items():
        # .items() give both the key and value of the item in the list, similar to enumerate
        for _ in range(symbol_count):
            #unused variable is _, if we don't care about the count or iteration value
            all_symbols.append(symbol)

    columns = []
    
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        #here we are copying contents of all_symbols to avoid repetition of values such as A cannot be displayed thrice as it's maximum limit is 2
        #[:] is used to copy list. if we don't do this then changing either of the values will affect the other
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            #will find the first instance of the vaklue to be displayed in the slot machine and get rid of it
            column.append(value)
            #here we are adding value of picked random symbol to column

        columns.append(column)
    return columns
    #everything is generated in rows that we will be converting into columns formatin below function


def print_slot_machine(columns):
    #will be used to print values obtained from get_slot_machine_spin in a better way
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            #this is the logic to create a seperator in the matrix do that last element won't have "|"
            if i != len(columns) -1:
                print(column[row], end="|")
                #"|" is used to indicate python to print in a new line which is bydefault set as '\n'
            else:
                print(column[row], end="")

        print()
        #empty print statement gets us to a new line




def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount



def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

    

    
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
            #f converts/ formats everything into string here without mentioning or converting seperately
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        #logic to compare if entered amount is more than available balance
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough amount, your current balance is: ${balance}")
        else:
            break
        
    print(
        f"You're betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)
    # * will pass every line from winning_lines in print function
    return winnings- total_bet
    # will return how much they won or lost from this  spin
    


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        # This will update the balance 

    print(f"You're left with ${balance}")



main()