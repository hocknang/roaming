# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

def home():
    st.write("QR Code")

    print(st.secrets["QR_CODE"])

    st.write("Presentation Slide")

    print("https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Slide1.JPG")

    st.write("Script & Key Status")

    st.write("Page 1")

    print("https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Script%20for%20Ideafest%20as%20of%2015%20Nov%202024_Page_1.jpg")

    st.write("Page 2")

    print("https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Script%20for%20Ideafest%20as%20of%2015%20Nov%202024_Page_2.jpg")

    st.write("Page 3")

    print("https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Script%20for%20Ideafest%20as%20of%2015%20Nov%202024_Page_3.jpg")



def print(image_path):
    # Define the HTML hyperlink with the image
    html_string = f'<a href="{image_path}" target="_blank"><img src="{image_path}" caption="legend"></a>'

    # Display the image using `st.markdown`
    st.markdown(html_string, unsafe_allow_html=True)

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
