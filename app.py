import streamlit as st
import detection

def main():
    st.title('spam detection')

    

    # Create a text input field
    user_input = st.text_input('Enter Text:')
   

    # Create a button to refresh the text field
    if st.button('Refresh', key='refresh_button'):
        st.text_input('Enter Text:', value='', key='refresh_key')

    # Create a button to display the input value
    if st.button('Check'):
        result = detection.result(user_input)  # Use the predict_spam function from detection module
        if result == 0:
            output = "Not spam"
        else:
            output = "Spam"
        st.write(f'Prediction: {output}')

if __name__ == '__main__':
    main()
