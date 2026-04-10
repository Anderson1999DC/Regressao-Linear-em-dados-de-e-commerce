# Regressão Linear em Dados de E-Commerce

### EDA · Regressão Linear · Interpretação de Coeficientes · Decisão de Negócio

&nbsp;

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=for-the-badge)](https://github.com/Anderson1999DC/Regressao-Linear-em-dados-de-e-commerce)

&nbsp;
> Modelo de Regressão Linear para identificar quais canais e comportamentos mais influenciam
> o gasto anual dos clientes de uma empresa de moda online apoiando a decisão de investimento
> entre app mobile e website.

---

## Índice

- [Contexto](#contexto)
- [Objetivos](#objetivos)
- [Pipeline do Projeto](#pipeline-do-projeto)
- [Tecnologias](#tecnologias-utilizadas)
- [Dataset](#dataset)
- [Análise Exploratória](#análise-exploratória)
- [Resultados do Modelo](#resultados-do-modelo)
- [Decisão de Negócio](#decisão-de-negócio)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Autor](#autor)

---

## Contexto

Projeto de Regressão Linear aplicado ao e-commerce de moda. Uma empresa de Nova York vende roupas online e oferece sessões de consultoria presencial de estilo. A gestão precisa decidir onde concentrar os investimentos: no **aplicativo mobile** ou no **website**. O modelo identifica quais fatores mais impactam o gasto anual dos clientes.

| Etapa | Descrição |
|---|---|
| **EDA** | Análise de correlação entre canais de acesso e gasto anual |
| **Modelagem** | Regressão Linear com 4 features numéricas |
| **Avaliação** | MAE, MSE, RMSE, R² e análise de resíduos |
| **Decisão** | Interpretação dos coeficientes para apoio estratégico |

> **Base de dados fictícia** criada para fins educacionais.

---

## Objetivos

- Construir um modelo de regressão para prever o gasto anual dos clientes
- Identificar quais variáveis mais influenciam o volume de compras
- Interpretar os coeficientes do modelo para apoiar a decisão de negócio
- Exportar o modelo treinado para deploy via API

---

## Pipeline do Projeto

```mermaid
flowchart TD
    A([Dataset\nE-commerce\n500 clientes]) --> B[EDA\nCorrelações · Jointplots · Pairplot]
    B --> C[Seleção de Features\n4 variáveis numéricas]
    C --> D[Split Treino/Teste\n70% / 30%]
    D --> E[Regressão Linear]
    E --> F[Avaliação\nMAE · RMSE · R² · Resíduos]
    F --> G[Interpretação\nCoeficientes → Decisão]
    G --> H([Insight\nApp > Website\nFidelização é chave])

    style A fill:#4A90D9,color:#fff,stroke:none
    style H fill:#28a745,color:#fff,stroke:none
    style B fill:#6C757D,color:#fff,stroke:none
    style C fill:#6C757D,color:#fff,stroke:none
    style D fill:#6C757D,color:#fff,stroke:none
    style E fill:#6C757D,color:#fff,stroke:none
    style F fill:#6C757D,color:#fff,stroke:none
    style G fill:#6C757D,color:#fff,stroke:none
```

---

## Tecnologias Utilizadas

| Tecnologia | Uso no Projeto |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Linguagem principal |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Manipulação e análise dos dados |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Operações numéricas |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) | Modelo de Regressão Linear e métricas |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white) | Scatter plots e visualizações |
| ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square&logo=python&logoColor=white) | Jointplots, pairplot e lmplot |

---

## Dataset

**Fonte:** Dataset fictício de e-commerce criado para fins educacionais  
**Uso:** Exclusivamente educacional

| Característica | Detalhe |
|---|---|
| Volume | 500 clientes |
| Variável target | `Yearly Amount Spent` (USD) |

**Variáveis disponíveis:**

| Variável | Descrição |
|---|---|
| `Avg. Session Length` | Tempo médio de sessão de consultoria na loja (min) |
| `Time on App` | Tempo médio no aplicativo mobile (min) |
| `Time on Website` | Tempo médio no website (min) |
| `Length of Membership` | Tempo de associação como cliente (anos) |
| `Yearly Amount Spent` | **Target** — gasto anual do cliente (USD) |

---

## Análise Exploratória

A EDA revelou correlações importantes entre as variáveis e o gasto anual dos clientes:

- **Time on App** apresenta correlação visual mais forte com `Yearly Amount Spent` do que `Time on Website`
- **Length of Membership** é a variável com correlação mais clara clientes mais antigos gastam significativamente mais
- O **pairplot** confirma que o tempo no site tem impacto praticamente nulo no gasto

---

## Resultados do Modelo

### Valores Reais vs Previstos

![Real vs Previsto](assets/real_vs_previsto_ecommerce.png)

> Pontos próximos à linha diagonal indicam boa aderência do modelo a Regressão Linear capturou bem a relação entre as variáveis.

### Análise de Resíduos

![Resíduos](assets/residuos_ecommerce.png)

> Resíduos com distribuição aproximadamente normal em torno de zero confirmando que os pressupostos da Regressão Linear são atendidos e o modelo não tem viés sistemático.

### Coeficientes do Modelo

![Coeficientes](assets/coeficientes_ecommerce.png)

| Variável | Coeficiente | Interpretação |
|---|---|---|
| **Length of Membership** | **~$61** | **1 ano a mais de associação → +$61/ano** |
| **Time on App** | **~$39** | **1 min a mais no app → +$39/ano** |
| Avg. Session Length | ~$26 | 1 min a mais na sessão → +$26/ano |
| Time on Website | ~$0.19 | impacto praticamente nulo |

### Métricas de Avaliação

| Métrica | Valor |
|---|---|
| **R²** | **alto** |
| MAE | baixo |
| RMSE | baixo |

---

## Decisão de Negócio

A interpretação dos coeficientes revela dois insights estratégicos claros:

**1. Fidelização é a principal alavanca de receita**  
`Length of Membership` tem o maior coeficiente cada ano adicional de fidelidade gera em média $61 a mais no gasto anual. A empresa deve priorizar **programas de fidelização e retenção** antes de qualquer investimento em canal.

**2. App mobile supera o website**  
O coeficiente do `Time on App` ~$39 é muito superior ao do `Time on Website` ~$0.19. Investir em melhorias no aplicativo tem retorno claramente mensurável, enquanto o website apresenta impacto desprezível no gasto dos clientes.

---

## Estrutura do Repositório

```
Regressao-Linear-em-dados-de-e-commerce/
│
├──  assets/                                          # Gráficos gerados na análise
│   ├── coeficientes_ecommerce.png
│   ├── real_vs_previsto_ecommerce.png
│   └── residuos_ecommerce.png
│
├──  regressao_linear_em_dados_de_ecommerce_restrutured.ipynb  # Notebook completo
├──  ecommerce-customers.csv                          # Dataset original
├──  modelo_ecommerce.pkl                             # Modelo treinado
├──  colunas_ecommerce.pkl                            # Features esperadas pela API
├──  requirements.txt                                 # Dependências do projeto
└──  README.md                                        # Documentação do projeto
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
