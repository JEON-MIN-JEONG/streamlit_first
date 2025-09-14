import streamlit as st

# 타이틀
st.title("안녕하세요")
st.title('스마일 :sunglasses:')  # 이모지

# 헤더
st.header("헤더입니다.")

# sub헤더
st.subheader("sub헤더입니다.")

# 캡션
st.caption("캡션을 한 번 넣어보겠습니다.")

sample_code = ''' def function(): print("Hello world)'''

st.code(sample_code, language="python")

st.text("일반적인 텍스트를 입력하겠습니다.")

# 마크다운(markdown)
st.markdown("streamlit은 **마크다운 문법을 지원합니다**")

st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **blue(파란색)** 볼트체로 설정할 수 있습니다.")