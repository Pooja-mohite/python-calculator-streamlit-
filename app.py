
import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Python Calculator",
    page_icon="🧮",
    layout="centered"
)

# History file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "history.txt")


# Save calculation
def save_history(equation):
    with open(HISTORY_FILE, "a") as file:
        file.write(equation + "\n")


# Read history
def show_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as file:
        return file.readlines()


# Clear history
def clear_history():
    with open(HISTORY_FILE, "w") as file:
        file.write("")


# Calculator UI
st.title("🧮 Python Calculator")
st.write("Perform basic mathematical operations.")

st.divider()

# Input fields
num1 = st.number_input("Enter first number", value=0.0)

operator = st.selectbox(
    "Select operator",
    ["+", "-", "*", "/"]
)

num2 = st.number_input("Enter second number", value=0.0)


# Calculate button
if st.button("Calculate", use_container_width=True):

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            st.error("Division by zero is not possible.")
            result = None
        else:
            result = num1 / num2

    if result is not None:

        if result.is_integer():
            result = int(result)

        equation = f"{num1} {operator} {num2} = {result}"

        st.success(f"Result: {result}")

        save_history(equation)


# History section
st.divider()

st.subheader("📜 Calculation History")

history = show_history()

if history:
    for item in reversed(history):
        st.write(item.strip())
else:
    st.info("No history found.")


# Clear history button
if st.button("Clear History", use_container_width=True):
    clear_history()
    st.success("History cleared!")
    st.rerun()
