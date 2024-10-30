import streamlit as st
import pandas as pd

# Supondo que você tenha um DataFrame 'df' com suas despesas
# Exemplo: df = pd.DataFrame({'Categoria': ['Alimentação', 'Transporte'], 'Valor': [100, 50]})

# Função para calcular o total de despesas
def calcular_despesas(dataframe):
    return dataframe['Valor'].sum()

# Inicializando o app
st.title("Controle Financeiro")

# Seção de Orçamento do mês
orçamento = st.number_input('Orçamento do mês:', min_value=0)

# Seção de Despesas
st.subheader("Despesas")

# Selecionar o tipo de visualização
opcao_visualizacao = st.radio("Escolha uma visualização:", ('Todas as Despesas', 'Por mês', 'Por categoria'))

# Mostrar as tabelas baseadas na opção escolhida
if opcao_visualizacao == 'Todas as Despesas':
    st.write("Tabela de todas as despesas")
    # Exibir tabela de todas as despesas
    st.dataframe(df)

elif opcao_visualizacao == 'Por mês':
    mes = st.selectbox("Selecione o mês:", ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
    # Filtrar o DataFrame para o mês selecionado
    df_mes = df[df['Mês'] == mes]  # Supondo que você tenha uma coluna 'Mês' no seu DataFrame
    st.write(f"Tabela de despesas para o mês de {mes}")
    st.dataframe(df_mes)

elif opcao_visualizacao == 'Por categoria':
    categoria_selecionada = st.selectbox("Escolha uma categoria:", df['Categoria'].unique())
    df_categoria = df[df['Categoria'] == categoria_selecionada]
    st.write(f"Tabela de despesas para a categoria: {categoria_selecionada}")
    st.dataframe(df_categoria)

# Calcular e exibir total de despesas
total_despesas = calcular_despesas(df)
st.write(f"Total de despesas: R$ {total_despesas:.2f}")

# Gráfico de despesas
st.subheader("Gráfico de Despesas")
# Aqui você pode usar uma biblioteca como matplotlib ou seaborn para gerar um gráfico.
import matplotlib.pyplot as plt

# Criando um gráfico simples de barras
fig, ax = plt.subplots()
ax.bar(df['Categoria'], df['Valor'])
ax.set_xlabel('Categoria')
ax.set_ylabel('Valor')
ax.set_title('Despesas por Categoria')

# Exibindo o gráfico no Streamlit
st.pyplot(fig)
