# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

def home():
    st.write("QR Code")

    st.write(
        f'<iframe src="https://plumber.gov.sg/tiles/9c5aeb0f-1db2-4a3a-a615-a2ea829ebfee/54f8b9b9-0bf1-4fe1-96e9-53091aab8eb4"></iframe>',
        unsafe_allow_html=True,
    )




def print(image_path):
    # Define the HTML hyperlink with the image
    html_string = f'<a href="{image_path}" target="_blank"><img src="{image_path}" caption="legend"></a>'

    # Display the image using `st.markdown`
    st.markdown(html_string, unsafe_allow_html=True)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    home()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
