import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(page_title="SIP Calculator", page_icon="📈", layout="centered")

st.title("📈 SIP Calculator")
st.markdown("Estimate your future wealth with monthly SIP investments.")

# Sidebar inputs
st.sidebar.header("SIP Parameters")
monthly_investment = st.sidebar.number_input("Monthly Investment Amount (₹)", min_value=500, value=5000, step=500)
annual_return = st.sidebar.number_input("Expected Annual Return Rate (%)", min_value=1.0, value=12.0, step=0.5)
years = st.sidebar.number_input("Investment Period (Years)", min_value=1, value=10, step=1)
# Show warnings if inputs are very low
if monthly_investment <= 500:
    st.warning("⚠️ Monthly investment amount seems very low. Consider investing more for better returns.")
if years < 3:
    st.warning("⚠️ Investment period is quite short. Longer periods benefit more from compounding.")
if annual_return < 5:
    st.warning("⚠️ Expected return rate is quite low. Typical equity SIPs assume around 10-12%.")

# Calculations
months = years * 12
monthly_rate = annual_return / 100 / 12

# SIP formula: FV = P * [((1+r)^n - 1) * (1+r)] / r
if monthly_rate > 0:
    future_value = monthly_investment * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate) / monthly_rate)
else:
    future_value = monthly_investment * months

total_invested = monthly_investment * months
gain = future_value - total_invested

# Display results
st.subheader("📊 Results")
st.write(f"**Total Invested:** ₹{total_invested:,.0f}")
st.write(f"**Estimated Final Amount:** ₹{future_value:,.0f}")
st.write(f"**Total Gain:** ₹{gain:,.0f}")

# Plot corpus growth over time
st.subheader("📈 Growth Over Time")
corpus = []
for m in range(1, months+1):
    if monthly_rate > 0:
        fv = monthly_investment * (((1 + monthly_rate) ** m - 1) * (1 + monthly_rate) / monthly_rate)
    else:
        fv = monthly_investment * m
    corpus.append(fv)

fig, ax = plt.subplots()
ax.plot(range(1, months+1), corpus, color='#4CAF50')
ax.set_xlabel('Months')
ax.set_ylabel('(₹)')
ax.set_title('Growth of Investment Over Time')
st.pyplot(fig)

st.markdown("---")
st.markdown("✅ *Built with Streamlit*")

