import streamlit as st
from Query_Database import handle_user_input



def main():

	messages = st.container(height=500)
	if "messages" not in st.session_state:
		st.session_state.messages = []

	for message in st.session_state.messages:
		messages.chat_message(message["role"]).write(message["content"])

	if query_text := st.chat_input("Say something"):
		messages.chat_message("user").write(query_text)

		formatted_response = handle_user_input(query_text, st.session_state.messages)

		st.session_state.messages.append({"role": "user", "content": query_text}) 
		st.session_state.messages.append({"role": "assistant", "content": formatted_response})
		messages.chat_message("assistant").write(formatted_response)

		expander = messages.expander("See Sources")
		

if __name__ == '__main__':
	main()