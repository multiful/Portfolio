from urllib.error import URLError
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="카카오 시가총액",
    page_icon="📊"
)

st.markdown("# 시가총액 비교")
st.sidebar.header("시가총액")
st.write(
    """카카오 시가총액 """
)

@st.cache_data
def get_market_cap_data():
    data = {
        "Company": ["카카오", "카카오 페이", "카카오뱅크","카카오 게임즈"],
        "Market Cap (Billion KRW)": [18.93, 3.8, 10.63 ,1.79]
    }
    df = pd.DataFrame(data)
    return df.set_index("Company")

try:
    df = get_market_cap_data()
    companies = st.multiselect(
        "Choose companies", list(df.index), ["카카오", "카카오 페이"]
    )
    if not companies:
        st.error("Please select at least one company.")
    else:
        data = df.loc[companies]
        st.write("### 시가총액(단위 : 조)", data.sort_index())

        data = data.reset_index()
        chart = (
            alt.Chart(data)
            .mark_bar(opacity=0.7)
            .encode(
                x="Company:N",
                y=alt.Y("Market Cap (Billion KRW):Q", stack=None),
                color="Company:N"
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """ % e.reason
    )
