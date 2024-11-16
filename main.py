# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

def home():
    st.write("Presentation Slide")

    image_path = 'https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Slide1.JPG'

    # Define the HTML hyperlink with the image
    html_string = f'<a href="{image_path}" target="_blank"><img src="{image_path}" caption="legend"></a>'

    # Display the image using `st.markdown`
    st.markdown(html_string, unsafe_allow_html=True)

    st.write("Script & Key Status")

    st.write("Page 1")

    image_path1 = 'https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Script%20for%20Ideafest%20as%20of%2015%20Nov%202024_Page_1.jpg'

    # Define the HTML hyperlink with the image
    html_string = f'<a href="{image_path1}" target="_blank"><img src="{image_path1}" caption="legend"></a>'

    # Display the image using `st.markdown`
    st.markdown(html_string, unsafe_allow_html=True)

    st.write("Page 2")

    image_path2 = 'https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Script%20for%20Ideafest%20as%20of%2015%20Nov%202024_Page_2.jpg'

    # Define the HTML hyperlink with the image
    html_string = f'<a href="{image_path2}" target="_blank"><img src="{image_path2}" caption="legend"></a>'

    # Display the image using `st.markdown`
    st.markdown(html_string, unsafe_allow_html=True)

    st.write("Page 3")

    image_path3 = 'https://raw.githubusercontent.com/hocknang/roaming/refs/heads/master/resource/Script%20for%20Ideafest%20as%20of%2015%20Nov%202024_Page_3.jpg'

    # Define the HTML hyperlink with the image
    html_string = f'<a href="{image_path3}" target="_blank"><img src="{image_path3}" caption="legend"></a>'

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
