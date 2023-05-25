import streamlit as st

# User Onboarding
def user_onboarding():
    st.title("Expense Management App")
    st.header("User Onboarding")
    # TODO: Implement sign up and login functionality

# Home Screen
def home_screen():
    st.title("Expense Management App")
    st.header("Home")
    # TODO: Display an overview of active groups/trips
    # TODO: Implement options to create a new group or join an existing one

# Group Management
def group_management():
    st.title("Expense Management App")
    st.header("Group Management")
    # TODO: Allow users to add/remove group members
    # TODO: Provide options to specify the purpose of the group

# Expense Entry
def expense_entry():
    st.title("Expense Management App")
    st.header("Expense Entry")
    # TODO: Allow users to enter individual expenses with details
    # TODO: Implement receipt upload functionality

# Expense Categorization
def expense_categorization():
    st.title("Expense Management App")
    st.header("Expense Categorization")
    # TODO: Implement tagging/untagging of group members for each expense
    # TODO: Allow users to categorize expenses for better tracking

# Payment and Reimbursement
def payment_reimbursement():
    st.title("Expense Management App")
    st.header("Payment and Reimbursement")
    # TODO: Display summary of expenses and payments made by each group member
    # TODO: Implement payback functionality to selected group members

# Group Closure
def group_closure():
    st.title("Expense Management App")
    st.header("Group Closure")
    # TODO: Display summary of financial transactions for the group

# Main App
def main():
    st.set_page_config(page_title="Expense Management App")
    user_onboarding()

    # Navigation
    page_options = {
        "Home": home_screen,
        "Group Management": group_management,
        "Expense Entry": expense_entry,
        "Expense Categorization": expense_categorization,
        "Payment and Reimbursement": payment_reimbursement,
        "Group Closure": group_closure
    }

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(page_options.keys()))
    page_options[page]()

if __name__ == "__main__":
    main()
