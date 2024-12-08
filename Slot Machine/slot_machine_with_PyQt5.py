import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt

MAX_LINES = 3
MAX_BET = 100
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


class SlotMachineApp(QWidget):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Slot Machine Game 🎰")
        self.setGeometry(300, 200, 500, 600)
        self.setStyleSheet("background-color: #1c1c1c; color: white;")

        # Labels
        self.balance_label = QLabel("Balance: $0", self)
        self.balance_label.setAlignment(Qt.AlignCenter)
        self.balance_label.setStyleSheet("font-size: 20px; font-weight: bold; margin: 10px;")

        self.slot_labels = [[QLabel("-") for _ in range(COLS)] for _ in range(ROWS)]
        for row in self.slot_labels:
            for label in row:
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(
                    "font-size: 30px; font-weight: bold; border: 2px solid #FFD700; "
                    "background-color: #000000; color: #FFD700; padding: 10px; margin: 5px;"
                )

        # Inputs
        self.deposit_input = QLineEdit(self)
        self.deposit_input.setPlaceholderText("Enter deposit amount")
        self.deposit_input.setStyleSheet("font-size: 16px; padding: 5px;")

        self.lines_input = QLineEdit(self)
        self.lines_input.setPlaceholderText(f"Lines to bet (1-{MAX_LINES})")
        self.lines_input.setStyleSheet("font-size: 16px; padding: 5px;")

        self.bet_input = QLineEdit(self)
        self.bet_input.setPlaceholderText(f"Bet per line (${MIN_BET}-${MAX_BET})")
        self.bet_input.setStyleSheet("font-size: 16px; padding: 5px;")

        # Buttons
        self.deposit_button = QPushButton("Deposit", self)
        self.deposit_button.setStyleSheet(
            "background-color: #28a745; font-size: 18px; font-weight: bold; color: white; padding: 10px;"
        )

        self.spin_button = QPushButton("Spin 🎰", self)
        self.spin_button.setStyleSheet(
            "background-color: #dc3545; font-size: 18px; font-weight: bold; color: white; padding: 10px;"
        )
        self.spin_button.setEnabled(False)

        # Connect events
        self.deposit_button.clicked.connect(self.deposit)
        self.spin_button.clicked.connect(self.spin)

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(self.balance_label)
        layout.addWidget(self.deposit_input)
        layout.addWidget(self.deposit_button)

        layout.addWidget(self.lines_input)
        layout.addWidget(self.bet_input)

        slot_layout = QVBoxLayout()
        for row in self.slot_labels:
            row_layout = QHBoxLayout()
            for label in row:
                row_layout.addWidget(label)
            slot_layout.addLayout(row_layout)
        layout.addLayout(slot_layout)

        layout.addWidget(self.spin_button)

        self.setLayout(layout)

    def deposit(self):
        try:
            amount = int(self.deposit_input.text())
            if amount > 0:
                self.balance += amount
                self.update_balance()
                self.spin_button.setEnabled(True)
                QMessageBox.information(self, "Deposit Successful", f"Deposited ${amount}.")
            else:
                QMessageBox.warning(self, "Invalid Deposit", "Deposit must be greater than $0.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")

    def spin(self):
        try:
            lines = int(self.lines_input.text())
            bet = int(self.bet_input.text())
            total_bet = lines * bet

            if not (1 <= lines <= MAX_LINES):
                QMessageBox.warning(self, "Invalid Input", f"Lines must be between 1 and {MAX_LINES}.")
                return

            if not (MIN_BET <= bet <= MAX_BET):
                QMessageBox.warning(self, "Invalid Input", f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
                return

            if total_bet > self.balance:
                QMessageBox.warning(self, "Insufficient Balance", f"Total bet (${total_bet}) exceeds balance (${self.balance}).")
                return

            # Deduct bet and spin the slot machine
            self.balance -= total_bet
            slots = self.get_slot_machine_spin(ROWS, COLS, symbol_count)
            winnings, winning_lines = self.check_winnings(slots, lines, bet, symbol_value)
            self.balance += winnings

            # Update UI with results
            self.update_balance()
            self.display_slots(slots)
            QMessageBox.information(self, "Spin Result", f"You won ${winnings}. Winning lines: {', '.join(map(str, winning_lines)) if winning_lines else 'None'}")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numbers for lines and bet.")

    def update_balance(self):
        self.balance_label.setText(f"Balance: ${self.balance}")
        if self.balance == 0:
            self.spin_button.setEnabled(False)

    def display_slots(self, slots):
        for i in range(ROWS):
            for j in range(COLS):
                self.slot_labels[i][j].setText(slots[j][i])

    @staticmethod
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
                for _ in range(rows):
                    value = random.choice(all_symbols)
                    column.append(value)
            columns.append(column)

        return columns

    @staticmethod
    def check_winnings(columns, lines, bet, values):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            if all(column[line] == symbol for column in columns):
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
        return winnings, winning_lines


if __name__ == "__main__":
    app = QApplication(sys.argv)
    slot_machine = SlotMachineApp()
    slot_machine.show()
    sys.exit(app.exec_())
