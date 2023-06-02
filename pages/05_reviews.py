import streamlit as st

def main():
    st.title("Review App")

    # User input for rating
    rating = st.slider("Rate the app (1-5)", min_value=1, max_value=5)

    # User input for review
    review = st.text_area("Leave a review")

    # Submit button
    if st.button("Submit"):
        save_review(rating, review)
        st.success("Review submitted successfully!")

def save_review(rating, review):
    # Write your logic here to save the rating and review
    # to a database or file
    # For this example, we'll just print them
    print(f"Rating: {rating}")
    print(f"Review: {review}")

if __name__ == "__main__":
    main()