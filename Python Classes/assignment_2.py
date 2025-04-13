#Loan Agreement between a bank and a customer
# The bank will provide a loan to the customer
# The customer will pay back the loan with interest
# The loan agreement will include the following information:
# 1. Loan amount
# 2. Interest rate
# 3. Loan term
# 4. Monthly payment
# 5. Total payment
# 6. Total interest paid
# 7. Loan agreement details

import tkinter as tk
from tkinter import messagebox
import math

def calculate_loan():
    try:
        # Get input values
        customer_name = entry_customer_name.get()  # Get customer's name
        loan_amount = float(entry_loan_amount.get())
        annual_interest_rate = float(entry_interest_rate.get())
        loan_term_years = int(entry_loan_term.get())

        # Calculate monthly interest rate and number of payments
        monthly_interest_rate = annual_interest_rate / 100 / 12
        number_of_payments = loan_term_years * 12

        # Calculate monthly payment using the formula
        monthly_payment = loan_amount * monthly_interest_rate / (1 - math.pow(1 + monthly_interest_rate, -number_of_payments))
        total_payment = monthly_payment * number_of_payments
        total_interest = total_payment - loan_amount

        # Display results
        label_monthly_payment_value.config(text=f"₦{monthly_payment:,.2f}")
        label_total_payment_value.config(text=f"₦{total_payment:,.2f}")
        label_total_interest_value.config(text=f"₦{total_interest:,.2f}")

        # Generate loan agreement details
        loan_agreement_details = (
            f"Loan Agreement Details:\n"
            f"Customer Name: {customer_name}\n"
            f"Loan Amount: ₦{loan_amount:,.2f}\n"
            f"Annual Interest Rate: {annual_interest_rate}%\n"
            f"Loan Term: {loan_term_years} years\n"
            f"Monthly Payment: ₦{monthly_payment:,.2f}\n"
            f"Total Payment: ₦{total_payment:,.2f}\n"
            f"Total Interest Paid: ₦{total_interest:,.2f}\n"
        )

        # Display loan agreement details in the text area
        text_loan_agreement.delete(1.0, tk.END)
        text_loan_agreement.insert(tk.END, loan_agreement_details)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Loan Calculator")

# Customer name input
label_customer_name = tk.Label(root, text="Customer Name:")
label_customer_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_customer_name = tk.Entry(root)
entry_customer_name.grid(row=0, column=1, padx=10, pady=5)

# Loan amount input
label_loan_amount = tk.Label(root, text="Loan Amount (₦):")
label_loan_amount.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_loan_amount = tk.Entry(root)
entry_loan_amount.grid(row=1, column=1, padx=10, pady=5)

# Interest rate input
label_interest_rate = tk.Label(root, text="Annual Interest Rate (%):")
label_interest_rate.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_interest_rate = tk.Entry(root)
entry_interest_rate.grid(row=2, column=1, padx=10, pady=5)

# Loan term input
label_loan_term = tk.Label(root, text="Loan Term (years):")
label_loan_term.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_loan_term = tk.Entry(root)
entry_loan_term.grid(row=3, column=1, padx=10, pady=5)

# Monthly payment output
label_monthly_payment = tk.Label(root, text="Monthly Payment:")
label_monthly_payment.grid(row=4, column=0, padx=10, pady=5, sticky="e")
label_monthly_payment_value = tk.Label(root, text="₦0.00")
label_monthly_payment_value.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Total payment output
label_total_payment = tk.Label(root, text="Total Payment:")
label_total_payment.grid(row=5, column=0, padx=10, pady=5, sticky="e")
label_total_payment_value = tk.Label(root, text="₦0.00")
label_total_payment_value.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Total interest output
label_total_interest = tk.Label(root, text="Total Interest Paid:")
label_total_interest.grid(row=6, column=0, padx=10, pady=5, sticky="e")
label_total_interest_value = tk.Label(root, text="₦0.00")
label_total_interest_value.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_loan)
button_calculate.grid(row=7, column=0, columnspan=2, pady=10)

# Loan agreement details section
label_loan_agreement = tk.Label(root, text="Loan Agreement Details:")
label_loan_agreement.grid(row=8, column=0, columnspan=2, pady=5)
text_loan_agreement = tk.Text(root, height=10, width=50)
text_loan_agreement.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()