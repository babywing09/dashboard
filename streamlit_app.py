import streamlit as st
import pandas as pd
import plotly.express as px

# ��������� ������
@st.cache_data
def load_data():
    df = pd.read_csv("world-happiness-2024.csv")
    df.columns = [col.replace('Explained by: ', '').replace(' ', '_').lower() for col in df.columns]
    df = df.rename(columns={'country_name': 'Country', 'ladder_score': 'Happiness_Score'})
    return df

df = load_data()

# ������
st.title("���� 2024 World Happiness Dashboard")
st.markdown("**������ ������������ ������������ ��������� ������������ ������������ ���������������������.**")

# ��� ������
tab1, tab2, tab3 = st.tabs(["���� ������������ ���������", "���� ������ ������ ���������", "���� ������������ ������"])

# ���1: ������ ������ ������������
with tab1:
    st.subheader("��������� ������ ������ ������")
    fig_map = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Happiness_Score",
        hover_name="Country",
        color_continuous_scale="YlGnBu",
        title="2024 ������ ������ ������"
    )
    st.plotly_chart(fig_map, use_container_width=True)

# ���2: ������ ������ ������ 10������ ���������
with tab2:
    st.subheader("������ ������ ������ 10������")
    top10 = df.sort_values("Happiness_Score", ascending=False).head(10)
    fig_bar = px.bar(
        top10,
        x="Happiness_Score",
        y="Country",
        orientation="h",
        color="Happiness_Score",
        color_continuous_scale="Blues",
        title="������ ������ ������ 10������"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ���3: ������ ������ ��� ������������ ������
with tab3:
    st.subheader("������ ��������� ������ ��� ������ ������")
    numeric_cols = ["Happiness_Score", "log_gdp_per_capita", "social_support",
                    "healthy_life_expectancy", "freedom_to_make_life_choices",
                    "generosity", "perceptions_of_corruption"]

    selected_x = st.selectbox("X��� ������", numeric_cols, index=1)
    selected_y = st.selectbox("Y��� ������", numeric_cols, index=0)

    fig_scatter = px.scatter(
        df,
        x=selected_x,
        y=selected_y,
        text="Country",
        trendline="ols",
        title=f"{selected_x} vs {selected_y}"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("������ ������������ ������ ������ ��� ��������� ��������������� ��������� ��� ������������.")

    
