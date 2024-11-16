# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

def home():
    st.write("Presentation Slide")

    

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    st.write("Please enter your password:")

    password = ""

    password = st.text_input("Password", type="password")
    if st.secrets["PASSWORD"] == password:
        st.success("Valid Credential")
        home()
    else:
        st.error("Invalid Password")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
