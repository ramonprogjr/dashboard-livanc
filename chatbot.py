import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard Livance", layout="wide")


st.markdown(
    """
    <style>
    .logo-container {
        display: flex;
        justify-content: center;
        margin-top: 50px; /* Aumente o valor para descer o logo */
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="logo-container"><img src="https://livance.com.br/livance-logo.svg" width="150"></div>', unsafe_allow_html=True)
st.title("Dashboard de Retenção - Livance")


st.markdown(
    """
    <style>
    .block-container {
        padding: 1rem 1rem 1rem 1rem;
    }
    h2, h3, .stMarkdown {
        margin-top: 1rem;
        margin-bottom: 1rem;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.header("Introdução")
st.markdown(
    """
    **Objetivo:** Identificar padrões e causas que impactam a taxa de retenção e propor soluções para atingir a meta de 30%.  
    **Contexto:**  
    - Taxa de retenção atual: **20%**  
    - Meta: **30%**  
    - Churn atual: **4%**  
    - Meta: **3,5%**
    """
)


st.header("Hipóteses Levantadas")
st.markdown(
    """
    1. **Motivo de Cancelamento:** Alguns motivos têm maior impacto na retenção.  
    2. **Categoria de Motivo:** Cancelamentos voluntários têm maior potencial de reversão.  
    3. **Tempo de Atividade:** Profissionais com menos de 6 meses de atividade têm maior churn.  
    4. **Pitch Comercial:** Argumentos comerciais específicos influenciam a retenção.  
    5. **SLA:** Pedidos com SLA maior que 5 dias têm menor taxa de retenção.
    """
)


st.header("Análises Realizadas")
st.markdown(
    """
    - **Análise 1:** Frequência dos motivos de cancelamento.  
    - **Análise 2:** Comparação entre categorias de motivo (voluntário vs. involuntário).  
    - **Análise 3:** Retenção por tempo de atividade (meses ativos).  
    - **Análise 4:** Eficácia dos pitches comerciais e membership.  
    - **Análise 5:** Impacto do SLA no sucesso de retenção.
    """
)


st.header("Principais Problemas Identificados")
st.markdown(
    """
    1. **Motivos Frequentes:** "Falta de pacientes" e "Preço (Mensalidade e Minutos)" são os mais recorrentes.  
    2. **Categoria de Motivo:** Cancelamentos voluntários representam 80% dos casos, mas têm maior potencial de reversão.  
    3. **Tempo de Atividade:** Profissionais com menos de 6 meses têm maior churn.  
    4. **Pitch Comercial:** Argumentos genéricos têm menor eficácia.  
    5. **SLA:** Pedidos tratados após 5 dias têm retenção significativamente menor.
    """
)


st.header("Proposta de Solução")
st.markdown(
    """
    **Automação e Processo:**  
    1. **Ferramenta de Análise de Dados:**  
       - Utilizar Python e Pandas para análise preditiva.  
       - Identificar padrões em tempo real.  
    2. **Automação de Comunicação:**  
       - Implementar um chatbot no WhatsApp para contato imediato após o pedido de cancelamento.  
       - Integração com ferramentas como Twilio ou Zapier.  
    3. **Segmentação de Clientes:**  
       - Criar clusters com base em motivos de cancelamento, tempo de atividade e categoria de motivo.  
    4. **Treinamento do Time:**  
       - Capacitar o time de retenção com scripts personalizados baseados nos insights.
    """
)


st.header("Detalhamento do Processo")
st.markdown(
    """
    1. **Passo 1:** Importar e processar os dados da planilha.  
    2. **Passo 2:** Identificar padrões com análise exploratória.  
    3. **Passo 3:** Desenvolver um modelo preditivo para priorizar contatos.  
    4. **Passo 4:** Automatizar mensagens personalizadas via WhatsApp.  
    5. **Passo 5:** Monitorar resultados e ajustar estratégias.
    """
)


st.header("Ferramentas Utilizadas")
st.markdown(
    """
    - **Análise de Dados:** Python (Pandas, Matplotlib, Scikit-learn).  
    - **Automação de Comunicação:** n8n para WhatsApp, Zapier para CRM e E-mails.  
    - **Dashboard de Monitoramento:** Google Data Studio ou Power BI.
    """
)


st.header("Recomendações")
st.markdown(
    """
    1. **Foco em Motivos Voluntários:** Priorizar "Falta de pacientes" e "Preço".  
    2. **Redução do SLA:** Garantir contato em até 2 dias.  
    3. **Personalização:** Utilizar argumentos específicos baseados no perfil do cliente.  
    4. **Monitoramento Contínuo:** Acompanhar métricas de retenção semanalmente.
    """
)


st.header("Resultados Esperados")
st.markdown(
    """
    - **Aumento da Retenção:** De 20% para 30%.  
    - **Redução do Churn:** De 4% para 3,5%.  
    - **Melhoria na Eficiência:** Redução do tempo médio de resposta.  
    - **Insights Contínuos:** Base de dados mais rica para decisões futuras.
    """
)


st.header("Conclusão")
st.markdown(
    """
    **Resumo:** A análise identificou padrões críticos e propôs soluções práticas e escaláveis.  
    **Próximos Passos:** Implementar a automação e monitorar os resultados.
    """
)


st.header("Comparação Antes e Depois")


retencao_antes = st.slider("Taxa de Retenção Antes (%)", min_value=0, max_value=100, value=20)
churn_antes = st.slider("Churn Antes (%)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)


retencao_depois = st.slider("Taxa de Retenção Depois (%)", min_value=0, max_value=100, value=30)
churn_depois = st.slider("Churn Depois (%)", min_value=0.0, max_value=10.0, value=3.5, step=0.1)


dados = {
    "Métrica": ["Taxa de Retenção", "Churn"],
    "Antes (%)": [retencao_antes, churn_antes],
    "Depois (%)": [retencao_depois, churn_depois],
}

df = pd.DataFrame(dados)


fig = go.Figure()


fig.add_trace(go.Bar(
    x=df["Métrica"],
    y=df["Antes (%)"],
    name="Antes",
    marker_color="#031B4E"  
))


fig.add_trace(go.Bar(
    x=df["Métrica"],
    y=df["Depois (%)"],
    name="Depois",
    marker_color="#00658A" 
))


fig.update_layout(
    title="Comparação de Taxa de Retenção e Churn (Antes vs. Depois)",
    xaxis_title="Métrica",
    yaxis_title="Percentual (%)",
    barmode="group",
    template="plotly_white"
)


st.plotly_chart(fig, use_container_width=True)


st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        background-color: #f1f1f1;
        text-align: left; /* Alinhar ao canto esquerdo */
        padding: 10px 20px; /* Espaçamento interno */
        font-size: 14px;
        color: #555;
        font-weight: bold; /* Deixar o texto em negrito */
    }
    </style>
    <div class="footer">
        Desenvolvido por Ramon Pereira
    </div>
    """,
    unsafe_allow_html=True,
)


