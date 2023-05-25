import streamlit as st

# Define Expense and Group classes
class Expense:
    def __init__(self, description, amount, group):
        self.description = description
        self.amount = amount
        self.group = group


class Group:
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)


# Create an empty list to store groups
groups = []


# Streamlit app code
def main():
    st.title("Expense Management App")

    # Create a new group
    st.header("Create Group")
    group_name = st.text_input("Group Name")
    group_members = st.text_input("Group Members (comma-separated)")

    if st.button("Create"):
        members = [member.strip() for member in group_members.split(",")]
        group = Group(group_name, members)
        groups.append(group)
        st.success(f"Group '{group_name}' created successfully!")

    # Add expense to a group
    st.header("Add Expense")
    group_options = [group.name for group in groups]
    selected_group = st.selectbox("Select Group", group_options)

    expense_description = st.text_input("Expense Description")
    expense_amount = st.number_input("Expense Amount")

    if st.button("Add Expense"):
        group = get_group_by_name(selected_group)
        if group:
            expense = Expense(expense_description, expense_amount, group)
            group.add_expense(expense)
            st.success("Expense added successfully!")
        else:
            st.error("Group not found.")

    # Display group and expense details
    st.header("Group Details")
    selected_group = st.selectbox("Select Groups", group_options)

    group = get_group_by_name(selected_group)
    if group:
        st.subheader(f"Expenses for Group: {group.name}")
        for expense in group.expenses:
            st.write(f"Description: {expense.description}, Amount: {expense.amount}")
    else:
        st.error("Group not found.")


def get_group_by_name(name):
    for group in groups:
        if group.name == name:
            return group
    return None


if __name__ == "__main__":
    main()
