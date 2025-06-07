import streamlit as st
import math

def calculate(operation, num1, num2=None):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "×":
        return num1 * num2
    elif operation == "÷":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif operation == "√":
        if num1 < 0:
            return "Error: Cannot calculate square root of negative number"
        return math.sqrt(num1)
    elif operation == "^":
        return num1 ** num2

def main():
    st.set_page_config(page_title="Calculator", page_icon="🧮")
    
    # Custom CSS for larger font sizes
    st.markdown("""
        <style>
        .stButton button {
            font-size: 24px !important;
            height: 60px !important;
        }
        .stTextInput input {
            font-size: 32px !important;
            height: 70px !important;
        }
        .stMarkdown {
            font-size: 20px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🧮 Calculator")
    
    # Initialize session state for calculator
    if 'current_number' not in st.session_state:
        st.session_state.current_number = "0"
    if 'first_number' not in st.session_state:
        st.session_state.first_number = None
    if 'operation' not in st.session_state:
        st.session_state.operation = None
    if 'new_number' not in st.session_state:
        st.session_state.new_number = True
    
    # Display with larger font
    st.text_input("", value=st.session_state.current_number, key="display", disabled=True)
    
    # Number buttons
    col1, col2, col3 = st.columns(3)
    
    # First row of numbers
    with col1:
        if st.button("7", use_container_width=True):
            update_display("7")
    with col2:
        if st.button("8", use_container_width=True):
            update_display("8")
    with col3:
        if st.button("9", use_container_width=True):
            update_display("9")
    
    # Second row of numbers
    with col1:
        if st.button("4", use_container_width=True):
            update_display("4")
    with col2:
        if st.button("5", use_container_width=True):
            update_display("5")
    with col3:
        if st.button("6", use_container_width=True):
            update_display("6")
    
    # Third row of numbers
    with col1:
        if st.button("1", use_container_width=True):
            update_display("1")
    with col2:
        if st.button("2", use_container_width=True):
            update_display("2")
    with col3:
        if st.button("3", use_container_width=True):
            update_display("3")
    
    # Fourth row (0 and decimal)
    with col1:
        if st.button("0", use_container_width=True):
            update_display("0")
    with col2:
        if st.button(".", use_container_width=True):
            update_display(".")
    with col3:
        if st.button("C", use_container_width=True):
            clear_calculator()
    
    # Operation buttons
    st.markdown("<h3>Operations:</h3>", unsafe_allow_html=True)
    op_col1, op_col2, op_col3, op_col4, op_col5 = st.columns(5)
    
    with op_col1:
        if st.button("➕", use_container_width=True):
            handle_operation("+")
    with op_col2:
        if st.button("➖", use_container_width=True):
            handle_operation("-")
    with op_col3:
        if st.button("✖️", use_container_width=True):
            handle_operation("×")
    with op_col4:
        if st.button("➗", use_container_width=True):
            handle_operation("÷")
    with op_col5:
        if st.button("🟰", use_container_width=True):
            calculate_result()

def update_display(digit):
    if st.session_state.new_number:
        st.session_state.current_number = digit
        st.session_state.new_number = False
    else:
        if digit == "." and "." in st.session_state.current_number:
            return
        st.session_state.current_number += digit
    st.rerun()

def handle_operation(op):
    if st.session_state.first_number is None:
        st.session_state.first_number = float(st.session_state.current_number)
    else:
        calculate_result()
    st.session_state.operation = op
    st.session_state.new_number = True
    st.rerun()

def calculate_result():
    if st.session_state.first_number is not None and st.session_state.operation is not None:
        second_number = float(st.session_state.current_number)
        result = calculate(st.session_state.operation, st.session_state.first_number, second_number)
        st.session_state.current_number = str(result)
        st.session_state.first_number = None
        st.session_state.operation = None
        st.session_state.new_number = True
        st.rerun()

def clear_calculator():
    st.session_state.current_number = "0"
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.new_number = True
    st.rerun()

if __name__ == "__main__":
    main() 