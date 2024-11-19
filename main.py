# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

def home():
    st.title("Open Hidden Website")

    # Add a button to open a website
    if st.button("Click to Proceed"):
        # Redirect the user with a hidden URL
        st.markdown("""
            <script>
            window.location.href = "https://www.example.com";
            </script>
            """, unsafe_allow_html=True)




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
