
import streamlit as st

st.write('Hello, *World!* :sunglasses:')
st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader('Daily Orders')
 
col1, col2 = st.columns(2)
 
with col1:
    total_orders = day_df.instant_count.sum()
    st.metric("Total orders", value=total_orders)

with col2:
    total_cnt = format_currency(day_df.revenue.sum(), "AUD", locale='es_CO') 
    st.metric("Total Revenue", value=total_revenue)

    fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    day_df["dteday"],
    day_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)