# Previsão de Valor Gasto por Clientes em E-commerce com Regressão Linear

Este projeto aplica técnicas de **Machine Learning** para analisar e prever o **valor anual gasto por clientes em uma plataforma de e-commerce**, utilizando um modelo de **Regressão Linear**.

O objetivo é demonstrar na prática um fluxo completo de **análise de dados e modelagem preditiva**, explorando como diferentes variáveis relacionadas ao comportamento do usuário influenciam o faturamento da empresa.

---

# Problema

Uma empresa de e-commerce deseja entender **quais fatores mais influenciam o valor que os clientes gastam na plataforma ao longo do ano**.

A partir dessa análise, a empresa busca responder uma pergunta estratégica:

**Vale mais a pena investir no aplicativo mobile ou no website para aumentar o faturamento?**

---

# Dataset

O conjunto de dados **Ecommerce Customers** contém informações sobre comportamento de clientes e seu consumo na plataforma.

Principais variáveis utilizadas:

- **Avg. Session Length** – Tempo médio das sessões de consultoria
- **Time on App** – Tempo médio gasto no aplicativo
- **Time on Website** – Tempo médio gasto no site
- **Length of Membership** – Tempo de associação do cliente (anos)
- **Yearly Amount Spent** – Valor anual gasto pelo cliente (variável alvo)

Algumas variáveis como **Email**, **Address** e **Avatar** foram removidas da modelagem por não contribuírem diretamente para a análise preditiva.

---

# Etapas do Projeto

## 1. Análise Exploratória de Dados (EDA)

Foi realizada uma análise inicial para entender a distribuição das variáveis e identificar possíveis relações entre o comportamento dos usuários e o valor gasto.

Foram analisados aspectos como:

- Relação entre tempo no aplicativo e valor gasto
- Relação entre tempo no website e valor gasto
- Influência do tempo de associação do cliente

---

## 2. Pré-processamento

As principais etapas de preparação dos dados incluíram:

- Seleção das variáveis relevantes para a modelagem
- Separação entre **variáveis independentes (features)** e **variável alvo**
- Divisão do dataset em **treino e teste**

---

## 3. Modelagem

Foi utilizado o algoritmo de **Regressão Linear**, amplamente aplicado em problemas de previsão de valores numéricos.

O modelo foi treinado para estimar o **valor anual gasto pelos clientes** com base em suas características comportamentais.

---

## 4. Avaliação do Modelo

O desempenho do modelo foi avaliado utilizando métricas comuns de regressão:

- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**

Também foi realizada uma **análise de resíduos**, permitindo verificar a distribuição dos erros do modelo e avaliar sua adequação aos dados.

---

# Insights de Negócio

A partir dos resultados obtidos, é possível extrair alguns insights relevantes para estratégias de negócio:

- Clientes com **maior tempo de associação tendem a gastar mais na plataforma**.
- O **tempo gasto no aplicativo possui impacto maior no valor gasto do que o tempo gasto no website**.
- Estratégias focadas em **retenção de clientes e fidelização** podem aumentar significativamente o faturamento ao longo do tempo.

---

# Limitações do Modelo

Apesar dos resultados positivos, algumas limitações devem ser consideradas:

- O modelo assume uma **relação linear entre as variáveis**, o que pode não capturar padrões mais complexos.
- O desempenho foi avaliado apenas neste conjunto de dados específico.
- Em aplicações reais, seria recomendável testar outros modelos de regressão e utilizar bases de dados maiores.

---

# Tecnologias Utilizadas

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Jupyter Notebook**

---

# Estrutura do Projeto
Regressão-Linear-em-dados-de-e-commerce
/
│
├── regressao_linear_em_dados_de_ecommerce.ipynb
├── Ecommerce-Customers.csv
├── requirements.txt
└── README.md

---

# Resultados do Modelo

MAE: 7.2281486534308295
MSE: 79.81305165097444
RMSE: 8.933815066978633

Avg. Session Length	25.981550
Time on App	38.590159
Time on Website	0.190405
Length of Membership	61.279097

---

# Conclusão

Este projeto demonstra como técnicas de **análise de dados e regressão linear** podem ser utilizadas para identificar fatores que impactam o comportamento de consumo dos clientes.

A análise evidencia que **retenção de clientes e engajamento no aplicativo** são fatores estratégicos para o crescimento do faturamento, reforçando o papel da **ciência de dados na tomada de decisões orientadas por dados**.

---

## Como Executar o Projeto

1. Clone este repositório

git clone [[[https://github.com/Anderson1999DC/Regressao-Linear-em-dados-de-e-commerce.git](https://github.com/Anderson1999DC/Regressao-Linear-em-dados-de-e-commerce)

2. Instale as dependências

pip install pandas numpy matplotlib seaborn scikit-learn jupyter

3. Abra o notebook


