import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações do layout do Streamlit
st.set_page_config(page_title="Simple Budget Tracker", layout="wide")

# CSS personalizado para deixar o estilo mais parecido com o Notion
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

# Função para estilizar as categorias no DataFrame
def color_category(category):
    color = color_map.get(category, "#CCCCCC")
    return f'<span class="category-label" style="background-color: {color};">{category}</span>'

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

# Exibir Tabela de Despesas
st.subheader("Expense Table")
df["Category"] = df["Category"].apply(color_category)
st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Gráfico de rosca de despesas por categoria
st.subheader("Expenses by Category")
category_summary = df.groupby("Category")["Amount"].sum().reset_index()
fig = px.pie(category_summary, values="Amount", names="Category", title="Expenses by Category", hole=0.4)
fig.update_traces(marker=dict(colors=[color_map[cat] for cat in category_summary["Category"]]))
st.plotly_chart(fig, use_container_width=True)

# Mostrar orçamento e gastos totais
total_expenses = df["Amount"].sum()
remaining_budget = monthly_budget - total_expenses
st.markdown(f"### Total Expenses: ${total_expenses:.2f}")
st.markdown(f"### Remaining Budget: ${remaining_budget:.2f}")
