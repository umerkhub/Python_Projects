# PYTHON SLOT MACHINE

import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 6,
    'B': 8,
    'C': 10,
    'D': 12
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        match = True
        for column in columns:
            if column[line] != symbol:
                match = False
                break
        if match:
                winnings += values[symbol] *bet
                winnings_lines.append(line + 1)
        return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for col in range(cols):
        column = []
        if col == 0:
            first_symbol = random.choice(all_symbols)
            column = [first_symbol] * rows
        else:
            for row in range(rows):
                value = random.choice(all_symbols)
                column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()


def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Please enter a number')

    return amount


def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1 -' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number')

    return lines



def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number')

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'Insufficient Balance. Your current balance is: ${balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    if winning_lines:
        print(f'You won on lines:', *winning_lines)
    else:
        print("You didn't win on any lines.")
    return balance + winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f'Current Balance is ${balance}')
        answer = input('Press enter to play (q to quit).')
        if answer == 'q':
            break
        balance += spin(balance)
    print(f'You left with ${balance}.')



main()