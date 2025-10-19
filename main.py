from save_to_notion import save_to_notion
from post_generator import code_based_generate_post,query_based_generate_post
import streamlit as st

def query_app():
	st.title("LLM post to Notion")
	query = st.text_input("Topic")
	if "work_done" not in st.session_state:
		st.session_state.work_done = False

	if st.button("Generate Content"):
		if query:
			st.session_state.result = query_based_generate_post(query)
			st.session_state.work_done = True
		else:
			st.error("Please Provide Query...")

	if st.session_state.work_done:
		st.write(st.session_state.result)
		st.success("Post Generated !")
		st.info("Click Save to Notion,for saving it to Notion Database")
		if st.button("Save to Notion"):
			save_to_notion(st.session_state.result,query)
			st.success("Sucessfully Saved !")


def code_analysis():
	st.title("Code Analysis")
	code_path = st.text_input("Enter The Path Of The Program")
	if "work_done" not in st.session_state:
		st.session_state.work_done = False
	if st.button("Click to Analyze for a Post"):
		if code_path:
			st.session_state.result = code_based_generate_post(code_path)
			st.session_state.work_done = True
		else:
			st.error("Please Provide Code Path")
	if st.session_state.work_done:
		st.write(st.session_state.result)
		st.success("Code Analysized !")
		st.info("Click Save to Notion,for saving it to Notion Database")
		if st.button("Save to Notion"):
			save_to_notion(st.session_state.result,f"Github-{code_path}")
			st.success("Sucessfully Saved !")


if __name__ == "__main__":
	side = st.sidebar.selectbox("Select",["Home","LLM To Post","Code To Post"])
	if side == "Home":
		st.title("Welcome To Post Generator and Saver.")
	elif side == "LLM To Post":
		query_app()
	elif side == "Code To Post":
		code_analysis()