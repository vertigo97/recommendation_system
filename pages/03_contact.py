import streamlit as st

def main():
    st.title("Contact Us")

    # Content section
    st.write("Your feedback and inquiries are valuable to us! If you have any questions, suggestions, or need assistance, please don't hesitate to reach out. Our team is here to help and provide you with the best possible support. Feel free to contact us via the following channels:")

    # Contact information
    st.subheader("Our Information")
    st.write("Email: restaurantrecommendation@gmail.com")
    st.write("Phone: +1 123-456-7890")
    st.write("Adress: Dzemala Bijedica 48")

    # Additional message
    st.write("If you can't find the information you're looking for, please reach out to us for further assistance.")

if __name__ == "__main__":
    main()
    import streamlit as st

def main():

    # Display an image from a file
    image_file = "pictures/teljefon.png"  # Replace with the path to your image file
    st.image(image_file, caption="")

if __name__ == "__main__":
    main()