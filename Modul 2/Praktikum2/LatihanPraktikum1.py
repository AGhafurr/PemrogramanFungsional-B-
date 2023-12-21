expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

def add_expense(expenses, tanggal, deskripsi, jumlah):
    expenses.append({
        'tanggal': tanggal,
        'deskripsi': deskripsi,
        'jumlah': jumlah
    })
    return expenses

calculate_total_expenses = lambda expenses: sum(expense['jumlah'] for expense in expenses)

def get_expenses_by_date(expenses, date):
    return [expense for expense in expenses if expense['tanggal'] == date]

def generate_expenses_report(expenses):
    for self in expenses:
        yield f"{self['tanggal']} - {self['deskripsi']}: {self['jumlah']}"

def main():
    add_expense(expenses, '2023-07-08', 'Ultah aku', 100000)

    total_expenses = calculate_total_expenses( expenses)
    print(f"total pengeluaran anda : {total_expenses}")

    expenses_by_date = get_expenses_by_date(expenses, '2023-07-07')
    for expense in expenses_by_date:
        print(f"{expense['deskripsi']}: {expense['jumlah']}")

    report = generate_expenses_report(expenses)
    print("Laporan Pengeluaran Harian: ")
    for line in report:  # Anda perlu menggulirkan generator
        print(line)

if __name__ == '__main__':
    main()
