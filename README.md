# Regressão Linear em Dados de E-Commerce

### EDA · Regressão Linear · Interpretação de Coeficientes · FastAPI · Docker · Deploy

&nbsp;

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-deployed-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/API-online-28a745?style=for-the-badge)](https://api-ecommerce-ml.onrender.com)

&nbsp;
> Modelo de Regressão Linear para identificar quais canais e comportamentos mais influenciam
> o gasto anual dos clientes de uma empresa de moda online apoiando a decisão de investimento
> entre app mobile e website. Deploy em produção com API REST containerizada.

&nbsp;

### Interface Interativa

**[Acessar interface interativa](https://api-ecommerce-ml.onrender.com/app)** &nbsp;|&nbsp; **[Documentação da API](https://api-ecommerce-ml.onrender.com/docs)**

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
- [API em Produção](#api-em-produção)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Autor](#autor)

---

## Contexto

Projeto de Regressão Linear aplicado ao e-commerce de moda. Uma empresa de Nova York vende roupas online e oferece sessões de consultoria presencial de estilo. A gestão precisa decidir onde concentrar os investimentos: no **aplicativo mobile** ou no **website**. O modelo identifica quais fatores mais impactam o gasto anual dos clientes e apoia essa decisão estratégica.

| Etapa | Descrição |
|---|---|
| **EDA** | Análise de correlação entre canais de acesso e gasto anual |
| **Modelagem** | Regressão Linear com 4 features numéricas |
| **Avaliação** | MAE, MSE, RMSE, R² e análise de resíduos |
| **Decisão** | Interpretação dos coeficientes para apoio estratégico |
| **Deploy** | API REST com FastAPI + Docker + Render |

> **Base de dados fictícia** criada para fins educacionais.

---

## Objetivos

- Construir um modelo de regressão para prever o gasto anual dos clientes
- Identificar quais variáveis mais influenciam o volume de compras
- Interpretar os coeficientes do modelo para apoiar a decisão de negócio
- Criar uma API REST com FastAPI e containerizar com Docker
- Fazer deploy em produção com link público acessível

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
    G --> H[API REST\nFastAPI · Docker]
    H --> I([Deploy\nRender · Link público])

    style A fill:#4A90D9,color:#fff,stroke:none
    style I fill:#28a745,color:#fff,stroke:none
    style B fill:#6C757D,color:#fff,stroke:none
    style C fill:#6C757D,color:#fff,stroke:none
    style D fill:#6C757D,color:#fff,stroke:none
    style E fill:#6C757D,color:#fff,stroke:none
    style F fill:#6C757D,color:#fff,stroke:none
    style G fill:#6C757D,color:#fff,stroke:none
    style H fill:#6C757D,color:#fff,stroke:none
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
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | API REST para servir o modelo em produção |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) | Containerização da aplicação |
| ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white) | Hospedagem do deploy em produção |

---

## Dataset

**Fonte:** Dataset fictício de e-commerce criado para fins educacionais
**Uso:** Exclusivamente educacional

| Característica | Detalhe |
|---|---|
| Volume | 500 clientes |
| Variável target | `Yearly Amount Spent` (USD) |

**Variáveis utilizadas:**

| Variável | Descrição |
|---|---|
| `Avg. Session Length` | Tempo médio de sessão de consultoria na loja (min) |
| `Time on App` | Tempo médio no aplicativo mobile (min) |
| `Time on Website` | Tempo médio no website (min) |
| `Length of Membership` | Tempo de associação como cliente (anos) |
| `Yearly Amount Spent` | **Target** gasto anual do cliente (USD) |

---

## Análise Exploratória

### Valores Reais vs Previstos

![Real vs Previsto](assets/real_vs_previsto_ecommerce.png)

> Pontos próximos à linha diagonal indicam boa aderência do modelo a Regressão Linear capturou bem a relação entre as variáveis comportamentais e o gasto anual.

### Análise de Resíduos

![Resíduos](assets/residuos_ecommerce.png)

> Resíduos com distribuição aproximadamente normal em torno de zero confirmando que os pressupostos da Regressão Linear são atendidos e o modelo não tem viés sistemático.

### Impacto de Cada Variável no Gasto Anual

![Coeficientes](assets/coeficientes_ecommerce.png)

> Cada barra representa o impacto de 1 unidade adicional da variável no gasto anual em USD. `Length of Membership` e `Time on App` são os fatores de maior peso, enquanto `Time on Website` tem impacto praticamente nulo.

---

## Resultados do Modelo

### Coeficientes do Modelo

| Variável | Coeficiente | Interpretação |
|---|---|---|
| **Length of Membership** | **~$61** | **1 ano a mais de associação → +$61/ano** |
| **Time on App** | **~$39** | **1 min a mais no app → +$39/ano** |
| Avg. Session Length | ~$26 | 1 min a mais na sessão → +$26/ano |
| Time on Website | ~$0.19 | impacto praticamente nulo |

### Métricas de Avaliação

| Métrica | Valor |
|---|---|
| MAE | ~$7.23 |
| MSE | ~$79.81 |
| RMSE | ~$8.93 |

---

## Decisão de Negócio

A interpretação dos coeficientes revela dois insights estratégicos claros:

**1. Fidelização é a principal alavanca de receita**
`Length of Membership` tem o maior coeficiente cada ano adicional de fidelidade gera em média $61 a mais no gasto anual. A empresa deve priorizar **programas de fidelização e retenção** antes de qualquer investimento em canal.

**2. App mobile supera o website**
O coeficiente do `Time on App` (~$39) é muito superior ao do `Time on Website` (~$0.19). Investir em melhorias no aplicativo tem retorno claramente mensurável, enquanto o website apresenta impacto desprezível no gasto dos clientes.

---

## API em Produção

### Interface Interativa

[![Interface do Modelo](assets/modelo_em_funcinamento.png)](https://api-ecommerce-ml.onrender.com/app)

> Acesse a interface em: **[api-ecommerce-ml.onrender.com/app](https://api-ecommerce-ml.onrender.com/app)**

### Documentação Swagger

[![Swagger UI](assets/Swagger_UI.png)](https://api-ecommerce-ml.onrender.com/docs)

> Documentação completa da API em: **[api-ecommerce-ml.onrender.com/docs](https://api-ecommerce-ml.onrender.com/docs)**

### Exemplo de Requisição

```bash
curl -X POST https://api-ecommerce-ml.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "avg_session_length": 33.0,
    "time_on_app": 12.0,
    "time_on_website": 37.0,
    "length_of_membership": 4.0
  }'
```

### Resposta

```json
{
  "gasto_anual_previsto": 498.32,
  "unidade": "USD",
  "modelo": "LinearRegression"
}
```

### Endpoints disponíveis

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/` | Status da API |
| `GET` | `/app` | Interface interativa |
| `GET` | `/docs` | Documentação Swagger |
| `POST` | `/predict` | Previsão de gasto anual |

---

## Estrutura do Repositório

```
Regressao-Linear-em-dados-de-e-commerce/
│
├──  assets/                                          # Gráficos e imagens
│   ├── real_vs_previsto_ecommerce.png
│   ├── residuos_ecommerce.png
│   ├── coeficientes_ecommerce.png
│   ├── modelo_em_funcionamento.png
│   └── Swagger_UI.png
│
├──  regressao_linear_em_dados_de_ecommerce.ipynb    # Notebook completo
├──  main.py                                          # API FastAPI
├──  index.html                                       # Interface interativa
├──  Dockerfile                                       # Containerização
├──  modelo_ecommerce.pkl                             # Modelo treinado
├──  colunas_ecommerce.pkl                            # Features esperadas pela API
├──  ecommerce-customers.csv                          # Dataset original
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
