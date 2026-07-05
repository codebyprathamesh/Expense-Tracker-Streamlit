import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Tracker",page_icon="💵")
st.title("Expense Tracker 🫰🏻💸")
st.sidebar.title("Expense Tracker")

with st.expander("Monthly Income", icon="💰"):
    income = st.number_input("Please enter Your Income", min_value=0)

with st.expander("Living Essentials", icon="🛒"):
    rent = st.number_input("Enter Monthly Rent amount", min_value=0)
    electricity_bill = st.number_input("Enter Monthly Electricy bill amount", min_value=0)
    internet = st.number_input("Enter monthly internet expense", min_value=0)
    Vegetables = st.number_input("Enter monthly Vegetable expense", min_value=0)
    Fruits = st.number_input("Enter monthly Fruits expense", min_value=0)
    Dairy = st.number_input("Enter monthly Dairy expense", min_value=0)
    Oil = st.number_input("Enter monthly Oil expense", min_value=0)
    Spices = st.number_input("Enter monthly Spice expense", min_value=0)
    Gas = st.number_input("Enter monthly Gas Cylinder expense", min_value=0)
    Living_Essentials = rent + electricity_bill + internet + Vegetables + Fruits + Dairy + Oil + Spices + Gas

with st.expander("Health", icon="❤️"):
    hosp = st.number_input("Enter Monthly Hospital Expense", min_value=0)
    meds = st.number_input("Enter Monthly Medical Expense", min_value=0)
    health = hosp + meds

with st.expander("Home Care", icon="🏠"):
    maintainence = st.number_input("Enter Montly Maintainence Expense", min_value=0)
    hygiene = st.number_input("Enter Monthly Hygiene Expense", min_value=0)
    Home_care = maintainence + hygiene

with st.expander("Education", icon="🎓"):
    fees = st.number_input("Enter Monthly School/College Fee Amount", min_value=0)
    books = st.number_input("Enter Monthly Books Expense", min_value=0)
    courses = st.number_input("Enter Monthly Expense on Courses/Online Courses", min_value=0)
    stationary = st.number_input("Enter Monthly Expense on Stationary", min_value=0)
    exam_fees = st.number_input("Enter Monthly Expense on Exam_Fees", min_value=0)
    Education = fees + books + courses + stationary + exam_fees

with st.expander("Entertainment", icon="🎬"):
    movies = st.number_input("Enter Montly  Movies Expense", min_value=0)
    games = st.number_input("Enter Montly Games Expense", min_value=0)
    subs = st.number_input("Enter Montly Subscription Expense", min_value=0)
    Entertainment = movies + games + subs

with st.expander("Travel", icon="✈️"):
    bus = st.number_input("Enter Montly Rikshaw/Bus Expense", min_value=0)
    train = st.number_input("Enter Monthly Train Expense", min_value=0)
    fuel = st.number_input("Enter Monthly Fuel Expense", min_value=0)
    cab = st.number_input("Enter Monthly Cab Expense", min_value=0)
    Travel = bus + train + fuel + cab

with st.expander("Clothing", icon="👕"):
    clothes = st.number_input("Enter Montly Clothing Expense", min_value=0)
    footwear = st.number_input("Enter Montly Footwear Expense", min_value=0)
    Accesories = st.number_input("Enter Montly Accessories Expense", min_value=0)
    Clothing = clothes + footwear + Accesories


Total_Expense = Living_Essentials + Home_care + Entertainment + Travel + Clothing + Education + health

if st.button("Calculate"):

    if income == 0:
        st.warning("Please enter your Income to proceed!")
        st.stop()

    if Total_Expense == 0:
        st.warning("Expenses Cannot be Zero!")
        st.stop()

    values = [
        Living_Essentials,
        Home_care,
        Education,
        Entertainment,
        Travel,
        Clothing,
        health
    ]

    labels = [
        "Living Essentials",
        "Home Care",
        "Education",
        "Entertainment",
        "Travel",
        "Clothing",
        "Health"
    ]

    values_filtered = []
    labels_filtered = []

    for i in range(len(values)):
        if values[i] != 0:
            values_filtered.append(values[i])
            labels_filtered.append(labels[i])

    # Savings
    Savings = income - Total_Expense
    Savings_percentage = (Savings / income) * 100
    exp_perc = (Total_Expense / income) * 100

    tab1, tab2, tab3 = st.tabs(["📊Dashboard", "📈 Analytics", "🧠Insights"])

    with tab1:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("💰 Income", f"₹{income:.2f}")

        with col2:
            st.metric("💸 Total Expense", f"₹{Total_Expense:.2f}")

        with col3:
            st.metric("💵 Savings", f"₹{Savings:.2f}")

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("📈 Savings %", f"{Savings_percentage:.2f}%")

        with col5:
            st.metric("📉 Expense %", f"{exp_perc:.2f}%")

        with col6:
            score = 0
            if Savings_percentage >= 30:
                score += 40
            if Total_Expense <= 0.7 * income:
                score += 30
            if max(values_filtered) < 0.5 * Total_Expense:
                score += 20
            if Total_Expense <= income:
                score += 10

            if score >= 90:
                st.metric(label="🏥Financial Health", value="🟢Excellent", delta=f"{score}/100")
            elif score >= 75:
                st.metric(label="🏥Financial Health", value="🔵Good", delta=f"{score}/100")
            elif score >= 60:
                st.metric(label="🏥Financial Health", value="🟡Fair", delta=f"{score}/100")
            elif score >= 40:
                st.metric(label="🏥Financial Health", value="🟠Needs attention", delta=f"{score}/100")
            else:
                st.metric(label="🏥Financial Health", value="🔴Poor", delta=f"{score}/100")

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            fig1, ax = plt.subplots()
            ax.set_title("Visual Representation Of Your Monthly Expenses.")
            ax.pie(values_filtered, labels=labels_filtered, autopct="%.2f%%")
            st.pyplot(fig1)

        with col2:
            fig2, ax2 = plt.subplots()
            ax2.bar(x=labels_filtered, height=values_filtered)
            ax2.set_title("Category-wise Expenses")
            ax2.set_ylabel("Expense (₹)")
            ax2.tick_params(axis="x", rotation=25)
            st.pyplot(fig2)

    with tab3:
        max_val = max(values_filtered)
        max_idx = values_filtered.index(max_val)
        min_val = min(values_filtered)
        min_idx = values_filtered.index(min_val)

        st.markdown(f"""
### Insights
*  You have high monthly expense in {labels_filtered[max_idx]} of about ₹{max_val:.2f} which is about {(max_val/Total_Expense)*100:.2f}% of your Total Expense.
*  You have least monthly expense in {labels_filtered[min_idx]} which is about {(min_val/Total_Expense)*100:.2f}% of your Total Expense.
*  You have saved Rs.{Savings:.2f} in this month.""")

        if Savings_percentage > 30:
            st.markdown("* Excellent Saving this month!")

        if Total_Expense > income:
            st.markdown("⚠️ Your Expenses exceeded your income.")
        elif Total_Expense > income * 0.9:
            st.markdown("* Your Expenses are very close to your income")

        for i in range(len(values_filtered)):
            cat_per = (values_filtered[i] / Total_Expense) * 100
            if cat_per > 50:
                st.markdown(f"* A significant portion of your expenses went to {labels_filtered[i]} and is Rs. {values_filtered[i]:.2f}, which is about {cat_per:.2f}% of your total expenses.")