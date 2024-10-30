import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações do layout do Streamlit
st.set_page_config(page_title="Simple Budget Tracker", layout="wide")

# CSS para estilizar as categorias e outros elementos
st.markdown("""
    <style>
        .main .block-container {
            padding: 2rem;
        }
        .title {
            font-size: 36px;
            font-weight: 600;
            text-align: center;
            margin-bottom: 2rem;
        }
        .subheader {
            font-size: 20px;
            font-weight: 500;
            color: #555;
            text-align: center;
        }
        .category-label {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 4px;
            color: white;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho do site
st.markdown("<div class='title'>Simple Budget Tracker</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Organize and track your expenses effortlessly</div>", unsafe_allow_html=True)

# Entrada do orçamento mensal
st.subheader("Enter Monthly Budget")
monthly_budget = st.number_input("Monthly Budget:", min_value=0.0, value=1000.0, step=100.0)

# Dados de despesas iniciais
data = {
    "Expense Name": ["Groceries", "Gym Membership", "Netflix Subscription", "Dining Out"],
    "Date": ["2024-10-05", "2024-10-10", "2024-10-12", "2024-10-15"],
    "Category": ["Food", "Health", "Entertainment", "Food"],
    "Payment Method": ["Debit", "Credit", "Debit", "Credit"],
    "Amount": [150.0, 50.0, 15.0, 40.0]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Paleta de cores para as categorias
color_map = {
    "Food": "#FFCC00",
    "Health": "#66FF66",
    "Entertainment": "#6699FF",
    "Transport": "#FF9966",
    "Education": "#9966FF",
    "Other": "#CCCCCC"
}

# Adicionar Despesa
st.subheader("Add New Expense")
with st.form("expense_form"):
    expense_name = st.text_input("Expense Name")
    expense_date = st.date_input("Date")
    expense_category = st.selectbox("Category", list(color_map.keys()))
    payment_method = st.selectbox("Payment Method", ["Debit", "Credit", "Cash", "Pix"])
    expense_amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_expense = {
            "Expense Name": expense_name,
            "Date": expense_date,
            "Category": expense_category,
            "Payment Method": payment_method,
            "Amount": expense_amount
        }
        df = df.append(new_expense, ignore_index=True)
        st.success("Expense added!")

# Sessão de visualização de despesas com abas
st.subheader("Expense Analysis")

# Criação das abas
tabs = st.tabs(["All Expenses", "By Month", "By Category"])

# Abas de visualização e filtros
with tabs[0]:
    st.write("### All Expenses")
    st.write(df)

with tabs[1]:
    st.write("### Expenses By Month")
    # Extrair o mês e o ano de cada data
    df['Month'] = df['Date'].dt.to_period("M")
    month_selected = st.selectbox("Select Month:", df['Month'].unique())
    
    # Filtrar o DataFrame pelo mês selecionado
    df_month = df[df['Month'] == month_selected]
    if not df_month.empty:
        fig_month = px.pie(df_month, names="Category", values="Amount", title=f"Expenses in {month_selected}", hole=0.4)
        fig_month.update_traces(marker=dict(colors=[color_map[cat] for cat in df_month["Category"]]))
        st.plotly_chart(fig_month, use_container_width=True)
    else:
        st.write("No expenses found for the selected month.")

with tabs[2]:
    st.write("### Expenses By Category")
    category_selected = st.selectbox("Select Category:", df['Category'].unique())
    
    # Filtrar o DataFrame pela categoria selecionada
    df_category = df[df['Category'] == category_selected]
    if not df_category.empty:
        fig_category = px.pie(df_category, names="Date", values="Amount", title=f"Expenses in {category_selected} category", hole=0.4)
        fig_category.update_traces(marker=dict(colors=[color_map[category_selected]]))
        st.plotly_chart(fig_category, use_container_width=True)
    else:
        st.write("No expenses found for the selected category.")
        
# Exibir total de despesas e orçamento restante
total_expenses = df["Amount"].sum()
remaining_budget = monthly_budget - total_expenses
st.markdown(f"### Total Expenses: ${total_expenses:.2f}")
st.markdown(f"### Remaining Budget: ${remaining_budget:.2f}")

# Mostrar orçamento e gastos totais
total_expenses = df["Amount"].sum()
remaining_budget = monthly_budget - total_expenses
st.markdown(f"### Total Expenses: ${total_expenses:.2f}")
st.markdown(f"### Remaining Budget: ${remaining_budget:.2f}")
