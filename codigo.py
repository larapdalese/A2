# Exibir menu de opções à direita com opções lado a lado
with col2:
    st.write("**Opções**")
    col_a, col_b, col_c = st.columns(3)  # Criar três colunas para as opções

    with col_a:
        if st.button("Todas as Despesas"):
            escolha = "Todas as Despesas"
    with col_b:
        if st.button("Por Categoria"):
            escolha = "Por Categoria"
    with col_c:
        if st.button("Mais 3"):
            escolha = "Mais 3"

    # Exibir DataFrames de acordo com a opção escolhida
    if escolha == "Todas as Despesas":
        st.write(df)
    elif escolha == "Por Categoria":
        categoria_selecionada = st.selectbox("Escolha uma categoria:", df["Categoria"].unique())
        despesas_categoria = df[df["Categoria"] == categoria_selecionada]
        st.write(despesas_categoria)
    elif escolha == "Mais 3":
        escolha_mais_3 = st.radio("Opções adicionais", ["Por mês", "Gastos totais ao longo do tempo", "Gastos ao longo dos meses"])
        
        if escolha_mais_3 == "Por mês":
            mes_selecionado = st.selectbox("Selecione o mês:", ["Tudo"] + list(df["Data"].dt.to_period("M").astype(str).unique()))
            if mes_selecionado == "Tudo":
                st.write(df)
            else:
                despesas_mes = df[df["Data"].dt.to_period("M").astype(str) == mes_selecionado]
                st.write(despesas_mes)
                
        elif escolha_mais_3 == "Gastos totais ao longo do tempo":
            df["AnoMes"] = df["Data"].dt.to_period("M").astype(str)
            despesas_por_mes = df.groupby("AnoMes")["Valor"].sum().reset_index()
            fig_gastos_totais = px.line(despesas_por_mes, x="AnoMes", y="Valor", title="Gastos Totais ao Longo do Tempo")
            st.plotly_chart(fig_gastos_totais, use_container_width=True)
        
        elif escolha_mais_3 == "Gastos ao longo dos meses":
            df["Mes"] = df["Data"].dt.month
            despesas_por_mes = df.groupby("Mes")["Valor"].sum().reset_index()
            fig_gastos_mensais = px.line(despesas_por_mes, x="Mes", y="Valor", title="Gastos ao Longo dos Meses")
            st.plotly_chart(fig_gastos_mensais, use_container_width=True)

        elif escolha_mais_3 == "Gastos ao longo dos meses":
            df["Mes"] = df["Data"].dt.month
            despesas_por_mes = df.groupby("Mes")["Valor"].sum().reset_index()
            fig_gastos_mensais = px.line(despesas_por_mes, x="Mes", y="Valor", title="Gastos ao Longo dos Meses")
            st.plotly_chart(fig_gastos_mensais, use_container_width=True)
