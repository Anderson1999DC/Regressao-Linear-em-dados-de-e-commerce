<div align="center">

# Regressão Linear em Dados de E-commerce
### EDA · Regressão Linear · Análise de Coeficientes · Decisão Estratégica

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=for-the-badge)]()

<br>

> Aplicação de Regressão Linear para prever o valor anual gasto por clientes em uma plataforma
> de e-commerce, com foco em responder uma pergunta estratégica de negócio: **app ou website?**

</div>

---

## Índice

- [Contexto](#contexto)
- [Objetivos](#objetivos)
- [Pipeline do Projeto](#pipeline-do-projeto)
- [Tecnologias](#tecnologias-utilizadas)
- [Dataset](#dataset)
- [Análise Exploratória](#análise-exploratória)
- [Modelagem e Resultados](#modelagem-e-resultados)
- [Conclusão Estratégica](#conclusão-estratégica)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Autor](#autor)

---

## Contexto

Uma empresa de e-commerce com sede em Nova York vende roupas online e também oferece sessões de consultoria de estilo presencialmente. Os clientes podem interagir com a empresa tanto pelo **aplicativo mobile** quanto pelo **website**.

A empresa precisa tomar uma decisão estratégica:

> **Vale mais a pena investir no aplicativo mobile ou no website para aumentar o faturamento?**

Atuei como Cientista de Dados para responder essa pergunta com base em dados reais de comportamento dos clientes.

| Canal | Situação Observada |
|---|---|
| **Aplicativo Mobile** | Forte correlação com o valor gasto |
| **Website** | Correlação praticamente nula com o valor gasto |

---

## Objetivos

- Explorar as relações entre comportamento dos clientes e valor gasto anualmente
- Identificar quais variáveis mais influenciam o faturamento
- Construir e avaliar um modelo de Regressão Linear para previsão do gasto anual
- Traduzir os coeficientes do modelo em recomendações de negócio

---

## Pipeline do Projeto

```mermaid
flowchart TD
    A([ecommerce-customers.csv\n500 clientes · 8 colunas]) --> B[EDA\nJointplots · Pairplot · LM Plot]
    B --> C[Preparação\nSeleção de features · Train/Test Split]
    C --> D[Regressão Linear\nScikit-learn]
    D --> E[Avaliação\nMAE · MSE · RMSE · Resíduos]
    E --> F([Decisão Estratégica\nApp vs Website])

    B --> B1[/"Length of Membership\nfeature mais correlacionada"/]
    D --> D1[/"70% treino · 30% teste\nRMSE: 8.93"/]

    style A fill:#4A90D9,color:#fff,stroke:none
    style F fill:#28a745,color:#fff,stroke:none
    style B fill:#6C757D,color:#fff,stroke:none
    style C fill:#6C757D,color:#fff,stroke:none
    style D fill:#6C757D,color:#fff,stroke:none
    style E fill:#6C757D,color:#fff,stroke:none
```

---

## Tecnologias Utilizadas

| Tecnologia | Uso no Projeto |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Linguagem principal |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Manipulação e análise dos dados |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Cálculos numéricos e métricas |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white) | Scatter plot de avaliação |
| ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square&logo=python&logoColor=white) | Jointplots, Pairplot e análise de resíduos |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) | Modelo de Regressão Linear e métricas |

---

## Dataset

**Fonte:** `ecommerce-customers.csv` — Dataset público de comportamento de clientes
**Uso:** Exclusivamente educacional

| Característica | Detalhe |
|---|---|
| Volume | 500 clientes |
| Colunas totais | 8 |
| Features usadas no modelo | 4 |
| Variável alvo | `Yearly Amount Spent` |

**Variáveis do modelo:**

| Feature | Descrição | Média |
|---|---|---|
| `Avg. Session Length` | Duração média das sessões de consultoria | 33,05 min |
| `Time on App` | Tempo médio no aplicativo mobile | 12,05 min |
| `Time on Website` | Tempo médio no website | 37,06 min |
| `Length of Membership` | Tempo de associação do cliente | 3,53 anos |
| `Yearly Amount Spent` | **Variável alvo** — valor gasto no ano | **US$ 499,31** |

---

## Análise Exploratória

### Visão Geral das Relações entre Variáveis

![Pairplot das Variáveis](assets/pairplot_variaveis.png)

> A análise do pairplot revela claramente que **`Length of Membership`** é a feature com maior correlação visual com o valor gasto anual, seguida por **`Time on App`**. `Time on Website` praticamente não apresenta padrão linear.

---

### Tempo no website × Valor Gasto Anual

![Time on Website x Gasto](assets/Time_on_Website_x_Gasto.png)

> Distribuição dispersa sem tendência linear — o tempo no website **não tem relação significativa** com o quanto o cliente gasta.

---

### Tempo no Aplicativo × Valor Gasto Anual

![Time on App x Gasto](assets/time_on_app_x_gasto.png)

> Correlação positiva moderada visível — clientes que passam mais tempo no app tendem a gastar mais.

---

### Tempo no Aplicativo × Tempo de Associação

![Time on App x Membership](assets/Time_on_App_×_Membership.png)

> Padrão hexagonal mostrando a concentração dos clientes — a maioria usa o app entre 11–13 min e tem entre 2–5 anos de associação.

---

### Relação Linear — Tempo de Associação × Valor Gasto

![LM Plot Membership x Gasto](assets/lmplot_membership_gasto.png)

> **Relação linear mais forte do dataset.** Clientes com mais tempo de associação gastam consistentemente mais — o que aponta para fidelização como principal alavanca de receita.

---

## Modelagem e Resultados

### Performance do Modelo — Dados de Teste

### Valores Reais vs. Preditos

![Scatter Real vs Predito](assets/scatter_real_vs_predito.png)

> Pontos concentrados próximos à diagonal, confirmando que o modelo captura bem a variação do gasto. Sem padrões sistemáticos de erro.

### Análise de Resíduos

![Histograma dos Resíduos](assets/histograma_residuos.png)

> Resíduos com distribuição aproximadamente normal e centrada em zero — sem viés sistemático, confirmando que a Regressão Linear é adequada para esse problema.

### Métricas de Avaliação

| Métrica | Valor |
|---|---|
| MAE | **US$ 7,23** |
| MSE | 79,81 |
| **RMSE** | **US$ 8,93** |

> Com RMSE de apenas **US$ 8,93** em um valor médio de **US$ 499**, o modelo apresenta erro relativo de menos de 2% — excelente desempenho para uma Regressão Linear simples.

### Coeficientes do Modelo

| Feature | Coeficiente | Interpretação |
|---|---|---|
| `Length of Membership` | **+61,28** | Cada ano a mais de associação → +US$ 61 gastos/ano |
| `Time on App` | **+38,59** | Cada minuto a mais no app → +US$ 38,59 gastos/ano |
| `Avg. Session Length` | +25,98 | Cada minuto a mais em consultoria → +US$ 25,98 gastos/ano |
| `Time on Website` | +0,19 | Impacto praticamente nulo no valor gasto |

---

## Conclusão Estratégica

A análise dos coeficientes responde diretamente a pergunta de negócio:

> **O aplicativo mobile tem impacto ~203x maior no faturamento do que o website** (coef. 38,59 vs. 0,19).

No entanto, a variável com maior influência é **`Length of Membership`** (coef. 61,28), o que revela que **fidelizar clientes é mais lucrativo do que qualquer canal digital**.

A empresa tem duas estratégias possíveis:

- **Investir no App** — capitalizar em algo que já funciona e aumentar o engajamento mobile
- **Investir no Website** — tentar desenvolver um canal que hoje está subutilizado e pode crescer

Em ambos os casos, **programas de fidelização** devem ser a prioridade, dado o peso do tempo de associação no modelo.

### Próximos Passos Sugeridos

- Testar modelos não-lineares (Random Forest, XGBoost) para verificar se capturam mais padrões
- Coletar dados de frequência de compra e ticket médio por sessão
- Implementar análise de segmentação (clustering) para personalizar estratégias por perfil de cliente

---

## Estrutura do Repositório

```
Regressao-Linear-em-dados-de-e-commerce/
│
├── 📁 assets/                              # Gráficos gerados na análise
│   ├── pairplot_variaveis.png
│   ├── Time_on_Website_x_Gasto.png
│   ├── time_on_app_x_gasto.png
│   ├── Time_on_App_x_Membership.png
│   ├── lmplot_membership_gasto.png
│   ├── scatter_real_vs_predito.png
│   └── histograma_residuos.png
│
├── 📓 regressao_linear_em_dados_de_ecommerce.ipynb  # Notebook completo
├── 📄 ecommerce-customers.csv                       # Dataset
├── 📄 requirements.txt                              # Dependências do projeto
└── 📄 README.md                                     # Documentação do projeto
```

---

## Autor

<div align="center">

<img src="https://github.com/Anderson1999DC.png" width="100px" style="border-radius:50%"/>

**Anderson Coelho**
*Cientista de Dados*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anderson-coelho-42671634a/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Anderson1999DC)

</div>

---

<div align="center">

</div>
