import tkinter as tk
from tkinter import messagebox
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")
        
        self.balance = 0
        self.lines = 1
        self.bet = 1
        
        # Deposit Frame
        self.deposit_frame = tk.Frame(root)
        self.deposit_frame.pack(pady=10)
        
        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount: $")
        self.deposit_label.pack(side=tk.LEFT)
        
        self.deposit_entry = tk.Entry(self.deposit_frame)
        self.deposit_entry.pack(side=tk.LEFT)
        
        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(side=tk.LEFT)
        
        # Info Frame
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(pady=10)
        
        self.balance_label = tk.Label(self.info_frame, text="Current Balance: $0")
        self.balance_label.pack()
        
        self.lines_label = tk.Label(self.info_frame, text="Number of Lines to Bet On (1-3):")
        self.lines_label.pack()
        
        self.lines_entry = tk.Entry(self.info_frame)
        self.lines_entry.pack()
        
        self.bet_label = tk.Label(self.info_frame, text="Bet Amount per Line ($1-$100):")
        self.bet_label.pack()
        
        self.bet_entry = tk.Entry(self.info_frame)
        self.bet_entry.pack()
        
        # Play Button
        self.play_button = tk.Button(root, text="Spin", command=self.spin)
        self.play_button.pack(pady=10)
        
        # Result Frame
        self.result_frame = tk.Frame(root)
        self.result_frame.pack(pady=10)
        
        self.result_label = tk.Label(self.result_frame, text="Good Luck!")
        self.result_label.pack()

    def deposit(self):
        try:
            amount = int(self.deposit_entry.get())
            if amount > 0:
                self.balance += amount
                self.update_balance_label()
            else:
                messagebox.showerror("Error", "Amount must be greater than 0.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def update_balance_label(self):
        self.balance_label.config(text=f"Current Balance: ${self.balance}")

    def spin(self):
        try:
            self.lines = int(self.lines_entry.get())
            self.bet = int(self.bet_entry.get())
            
            if not (1 <= self.lines <= MAX_LINES):
                messagebox.showerror("Error", "Enter a valid number of lines (1-3).")
                return
            
            if not (MIN_BET <= self.bet <= MAX_BET):
                messagebox.showerror("Error", f"Bet amount must be between ${MIN_BET} and ${MAX_BET}.")
                return
            
            total_bet = self.bet * self.lines
            if total_bet > self.balance:
                messagebox.showerror("Error", "You do not have enough balance.")
                return
            
            self.balance -= total_bet
            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            winnings, winning_lines = check_winnings(slots, self.lines, self.bet, symbol_value)
            self.balance += winnings
            
            result_text = f"Slots:\n{slots[0]}\n{slots[1]}\n{slots[2]}\n"
            result_text += f"You won ${winnings}.\n"
            result_text += f"You won on lines: {', '.join(map(str, winning_lines)) if winning_lines else 'None'}"
            
            self.result_label.config(text=result_text)
            self.update_balance_label()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for lines and bet.")

def main():
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()

main()
