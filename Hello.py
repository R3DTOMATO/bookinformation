import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)



def run():
    st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    )
    
    st.title("메인 페이지")  
    st.write("# 안녕하세요? 이곳에 오신것을 환영합니다. 👋")
    st.sidebar.success("위에서 선택해주세요")

    st.markdown(
    '안녕하세요 여기서 책이름 혹은 작가명으로 검색을 해주세요^^'
    )
    
if __name__ == "__main__":       
    run()