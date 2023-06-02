import streamlit as st

def main():
    st.title("Recommend to a Friend")

    # User input for friend's email
    friend_email = st.text_input("Friend's Email", key="friend_email")

    # User input for message
    message = st.text_area("Message", key="message")

    # Send recommendation button
    if st.button("Send Recommendation"):
        send_recommendation(friend_email, message)
        st.success("Recommendation sent successfully!")

    # Social media sharing
    st.subheader("Share on Social Media")
    st.write("Share our app on your favorite social media platform:")

    # Facebook share button
    facebook_share_url = "https://www.facebook.com/"
    st.markdown(f"[Share on Facebook]({facebook_share_url})", unsafe_allow_html=True)

    # Instagram share button
    instagram_share_url = "https://www.instagram.com/"
    st.markdown(f"[Share on Instagram]({instagram_share_url})", unsafe_allow_html=True)

def send_recommendation(friend_email, message):
    # Write your logic here to send the recommendation email to the friend
    # For this example, we'll just print the friend's email and message
    print(f"Friend's Email: {friend_email}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main()
    import streamlit as st

def main():

    # Display an image from a file
    image_file = "pictures/hanuma.png"  # Replace with the path to your image file
    st.image(image_file, caption="Restaurant")

if __name__ == "__main__":
    main()