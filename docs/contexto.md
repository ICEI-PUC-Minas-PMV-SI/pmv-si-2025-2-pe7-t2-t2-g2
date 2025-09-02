# Introdução

O futebol contemporâneo deixou de ser um domínio exclusivo da intuição para se tornar uma arena amplamente orientada por dados. A cada partida, um volume massivo de informações estatísticas é gerado, criando um "oceano" de dados que contém padrões valiosos sobre desempenho tático e técnico. O principal desafio, no entanto, é transformar esse grande volume de informação bruta em conhecimento estratégico. Atualmente, a capacidade de realizar análises preditivas avançadas é um diferencial competitivo, muitas vezes limitado a clubes com grandes orçamentos. Este projeto se propõe a explorar esse cenário, aplicando a ciência de dados para demonstrar como é possível modelar, prever e classificar resultados e comportamentos em campo a partir de dados abertos.

Para materializar esse objetivo, o projeto foca na aplicação prática de três técnicas de Machine Learning, cada uma abordando uma questão fundamental da análise esportiva. A execução será conduzida utilizando Python e bibliotecas consolidadas como Pandas e Scikit-Learn, com o objetivo de construir modelos robustos para:

Regressão: Estimar o número total de gols em uma partida, oferecendo uma medida quantitativa do potencial ofensivo do confronto.

Classificação: Prever o resultado mais provável de um jogo (vitória do time da casa, empate ou derrota), aplicando uma abordagem estatística a um dos maiores desafios do esporte.

Clusterização: Identificar perfis de equipes com estilos de jogo similares, agrupando-as com base em suas métricas de desempenho para revelar semelhanças táticas.

O resultado final deste trabalho é uma ferramenta de análise preditiva funcional, projetada para ser útil a um público diversificado. O projeto oferece valor estratégico para equipes técnicas e analistas na preparação para partidas, enriquece o trabalho da mídia esportiva com insights baseados em dados, e serve como um estudo de caso prático para estudantes e pesquisadores. Ao final, o objetivo é demonstrar de forma clara e objetiva o impacto da ciência de dados na geração de inteligência competitiva e no aprofundamento da compreensão estratégica do esporte.

## Problema

Nesta seção, você deve apresentar o problema que a sua investigação/experimentação busca resolver. Por exemplo, caso o _dataset_ selecionado, seja um _dataset_ que contenha uma série temporal com o preço de diversas ações da bolsa de valores, o problema pode estar relacionado a dificuldade em saber a melhor hora (hora certa??) de comprar ou então, de executar a venda de uma determinada ação.

Descreva ainda o contexto em que essa aplicação será usada, se houver: empresa parceira, tecnologias etc. Novamente, descreva apenas o que de fato existir, pois ainda não é a hora de apresentar requisitos  detalhados ou projetos.

**Atenção:** Nesta etapa, apresente apenas informações reais e já confirmadas. Não antecipe requisitos técnicos detalhados, funcionalidades específicas ou desenhos de projeto — essa parte será desenvolvida posteriormente.

> **Links Úteis**:
> - [Objetivos, Problema de pesquisa e Justificativa](https://medium.com/@versioparole/objetivos-problema-de-pesquisa-e-justificativa-c98c8233b9c3)
> - [Matriz Certezas, Suposições e Dúvidas](https://medium.com/educa%C3%A7%C3%A3o-fora-da-caixa/matriz-certezas-suposi%C3%A7%C3%B5es-e-d%C3%BAvidas-fa2263633655)
> - [Brainstorming](https://www.euax.com.br/2018/09/brainstorming/)

## Questão de pesquisa

A questão de pesquisa é o ponto de partida e a base orientadora de todo o trabalho a ser desenvolvido. Ela deve estar diretamente alinhada ao problema identificado e expressar, de forma clara, o que se deseja investigar ou comprovar.

O papel da questão de pesquisa é guiar todas as etapas do projeto — desde a definição da metodologia até a análise e interpretação dos resultados. Ao término da investigação ou experimentação, o objetivo é que seja possível responder a essa questão de forma fundamentada, utilizando evidências obtidas ao longo do processo.

**Dica:** Formule a questão de pesquisa de forma específica e objetiva, evitando perguntas muito amplas ou genéricas. Pergunte-se: "Ao final do trabalho, minha pesquisa terá condições de responder claramente a essa pergunta?"

> **Links Úteis**:
> - [Questão de pesquisa](https://www.enago.com.br/academy/how-to-develop-good-research-question-types-examples/)
> - [Problema de pesquisa](https://blog.even3.com.br/problema-de-pesquisa/)

## Objetivos preliminares

Objetivo Geral

Experimentar e avaliar modelos de aprendizado de máquina para previsão e análise de partidas de futebol, visando identificar as abordagens mais eficazes para:

* estimar o número de gols por jogo,

* classificar o resultado da partida (vitória, empate ou derrota) e

* agrupar os clubes em perfis táticos de desempenho.

Objetivos Específicos

* Aplicar modelos de regressão (Regressão Linear, Random Forest Regressor e XGBoost) para estimar o número esperado de gols em cada partida, utilizando métricas como RMSE e R² para avaliar o desempenho.

* Comparar diferentes modelos de classificação supervisionada (Regressão Logística, Random Forest Classifier e XGBoost) para prever o desfecho de cada jogo, analisando métricas como acurácia, precisão, recall e F1-score.

* Explorar algoritmos de clusterização (K-Means, DBSCAN, HDBSCAN) para identificar padrões e agrupar os clubes em perfis táticos (ofensivo, defensivo, equilibrado), avaliando a qualidade dos agrupamentos por meio de métricas como Silhouette Score.

Otimizar os hiperparâmetros dos modelos selecionados a fim de melhorar as métricas de desempenho e maximizar a capacidade preditiva e explicativa das análises.

## Justificativa

O futebol é um dos esportes mais populares do mundo e movimenta uma das maiores indústrias globais de entretenimento e apostas. Segundo a FIFA (2023), mais de 5 bilhões de pessoas acompanharam a Copa do Mundo do Catar, evidenciando o alcance social e econômico desse esporte. No Brasil, país considerado o maior mercado de futebol da América Latina, a CBF reportou que o Campeonato Brasileiro gerou mais de R$ 1,3 bilhão em receitas apenas em 2022, entre direitos de transmissão, patrocínios e bilheterias. Esse volume de recursos mostra como pequenas melhorias em desempenho, análise de dados ou previsão de resultados podem gerar impactos significativos para clubes, investidores, casas de apostas e torcedores.

A escolha do conjunto de dados de partidas, clubes e jogadores de diferentes temporadas é estratégica, pois reúne informações ricas e multidimensionais (estatísticas de jogo, indicadores de desempenho coletivo, métricas individuais). Isso possibilita a aplicação de técnicas de aprendizado de máquina tanto em problemas de regressão (estimativa de gols), quanto de classificação (resultado da partida) e clusterização (perfis táticos de clubes). Dessa forma, cobre três áreas centrais da ciência de dados aplicada ao esporte: previsão de eventos, categorização de desfechos e descoberta de padrões ocultos.

A decisão de aprofundar nos objetivos específicos está ligada ao potencial de solução de problemas reais enfrentados por analistas esportivos e gestores de clubes. A previsão do número de gols pode auxiliar em estratégias de jogo, avaliação de desempenho ofensivo/defensivo e até em modelos de precificação para apostas esportivas, setor que movimentou mais de R$ 7 bilhões no Brasil em 2023 (IBGE/Agência Brasil). Já a classificação do resultado de uma partida tem aplicações diretas em simulações de campeonatos, previsão de pontos e probabilidade de títulos. Por sua vez, a clusterização de clubes em perfis táticos permite identificar tendências estratégicas, auxiliar treinadores na análise de adversários e melhorar processos de scouting de atletas compatíveis com cada estilo de jogo.

Do ponto de vista acadêmico, este estudo contribui para demonstrar a aplicabilidade de algoritmos de aprendizado de máquina em contextos reais, com bases volumosas e variáveis complexas. A utilização de métricas robustas (RMSE, R², F1-score, Silhouette) garante rigor na avaliação dos modelos, fortalecendo a validade científica do trabalho. Além disso, a otimização de hiperparâmetros acrescenta valor ao experimento, pois busca maximizar a capacidade preditiva e explicativa das análises.

No âmbito social e econômico, o impacto é igualmente relevante. A análise de dados esportivos pode ajudar clubes com menor orçamento a otimizar decisões táticas, reduzindo desigualdades competitivas. Também fornece subsídios para narrativas jornalísticas mais embasadas e para maior engajamento do torcedor. Assim, o projeto não apenas avança em termos técnicos e metodológicos, mas também gera benefícios concretos em setores-chave da sociedade que orbitam o futebol.

## Público-Alvo

O projeto destina-se a atender um público variado, que atua no ecossistema do futebol e tem interesse em utilizar dados e inteligência artificial para melhorar processos de análise, tomada de decisão e engajamento.

1. Estudantes e Pesquisadores de Ciência de Dados e Esporte

* Conhecimento prévio: Noções de estatística, aprendizado de máquina e/ou análise esportiva.

* Necessidades: Conjunto de dados robusto e estruturado para aplicação de técnicas de regressão, classificação e clusterização.

* Expectativa: Poder utilizar o projeto como estudo de caso para validar hipóteses, desenvolver artigos científicos e aplicar metodologias de previsão em cenários reais.

2. Analistas de Desempenho e Profissionais de Clubes

* Conhecimento prévio: Entendem métricas de futebol, táticas e indicadores de performance.

* Necessidades: Ferramentas que auxiliem na previsão de resultados, identificação de padrões táticos e avaliação de desempenho de equipes.

* Expectativa: Obter insights que possam embasar estratégias de treinamento, contratações e ajustes táticos.

3. Gestores e Tomadores de Decisão no Esporte

* Conhecimento prévio: Visão estratégica do negócio, mas nem sempre profundidade técnica em estatística ou IA.

* Necessidades: Relatórios claros e objetivos que facilitem decisões sobre investimento, contratações ou marketing esportivo.

* Expectativa: Ter acesso a indicadores consolidados que reduzam o risco em negociações e investimentos no clube.

4. Empresas de Mídia e Casas de Apostas

* Conhecimento prévio: Uso avançado de estatísticas para gerar conteúdo e odds.

* Necessidades: Modelos preditivos que aumentem o engajamento do público e melhorem a precificação de apostas.

* Expectativa: Obter previsões com maior acurácia para gerar narrativas interessantes e atrair apostadores.

5. Torcedores e Entusiastas de Futebol

* Conhecimento prévio: Baixo a médio, mais interessados no aspecto lúdico do esporte.

* Necessidades: Informação de fácil interpretação, gráficos e estatísticas que aumentem a experiência de acompanhar o campeonato.

* Expectativa: Acessar previsões de resultados e análises de desempenho para acompanhar o campeonato de forma mais interativa.

## Estado da Arte

Nesta seção, descrevemos abordagens da literatura que tratam de problemas semelhantes à previsão de resultados e análise de estilos táticos no futebol. O objetivo é documentar os métodos, dados, métricas e resultados de 2 trabalhos relevantes, publicados nos últimos anos, para contextualizar e fundamentar nosso projeto.

### Levantamento de Trabalhos

---

#### Trabalho 1: Previsão de Resultados com Foco em Classificação e Rentabilidade

*   **Referência Completa:** Choi, B. S., Foo, L. K., & Chua, S. L. (2023). *Predicting Football Match Outcomes with Machine Learning Approaches*. MENDEL, 29(1), 93-99.
*   **DOI/URL:** [`https://doi.org/10.13164/mendel.2023.1.093`](https://doi.org/10.13164/mendel.2023.1.093 )

*   **Problema e Contexto:** O trabalho buscou prever o resultado de partidas (vitória, empate ou derrota) da English Premier League (EPL), um dos campeonatos mais competitivos e ricos em dados do mundo. O diferencial foi avaliar não apenas a acurácia dos modelos, mas também sua performance em um cenário de simulação de apostas, testando o impacto de diferentes técnicas de balanceamento de dados.
*   **Dados (Dataset):**
    *   **Origem:** Dados da temporada 2022-2023 da English Premier League (EPL).
    *   **Variáveis/Atributos:** O estudo não detalha todas as features, mas foca em estatísticas históricas de desempenho das equipes.
    *   **Pré-processamentos:** O ponto central do estudo foi o teste de diferentes técnicas de amostragem para lidar com o desbalanceamento de classes (menos empates que vitórias/derrotas), como SMOTE (*Synthetic Minority Over-sampling Technique*).
*   **Abordagem/Algoritmos:**
    *   **Classificação (Resultado do Jogo):** Foram comparados quatro algoritmos: Random Forest, Regressão Logística, Linear Support Vector Classifier (SVC) e XGBoost.
*   **Métricas de Avaliação:**
    *   **Acurácia:** Para medir o percentual de previsões corretas.
    *   **Lucro Simulado:** Uma métrica prática para avaliar o retorno financeiro das previsões em um cenário de apostas.
*   **Resultados:**
    *   O **Random Forest** (em classificação binária) alcançou a maior acurácia.
    *   A **Regressão Logística** (também binária) gerou o maior lucro na simulação de apostas, indicando que a melhor acurácia nem sempre se traduz em maior rentabilidade.
    *   A principal conclusão foi que o uso de técnicas de amostragem para balancear o dataset melhorou significativamente o desempenho dos modelos.

---

#### Trabalho 2: Clusterização para Identificar Estilos de Jogo de Times

*   **Referência Completa:** Plakias, S., et al. (2024). *Cluster Analysis on Football Teams Performance Data*. DiVA portal.
*   **DOI/URL:** [`http://urn.kb.se/resolve?urn=urn:nbn:se:liu:diva-202299`](http://urn.kb.se/resolve?urn=urn:nbn:se:liu:diva-202299 )

*   **Problema e Contexto:** O trabalho utilizou aprendizado não supervisionado para resolver um problema de análise tática: agrupar times de futebol em clusters que representem "estilos de jogo" distintos. O estudo foi aplicado às cinco principais ligas europeias na temporada 2022-23.
*   **Dados (Dataset):**
    *   **Origem:** Dados de desempenho de times das ligas da Itália, Alemanha, França, Espanha e Inglaterra na temporada 2022-23.
    *   **Variáveis/Atributos:** Métricas de desempenho que refletem táticas, como posse de bola, tipos de passe, pressão defensiva, xG (*Gols Esperados*), etc.
    *   **Pré-processamentos:** Normalização dos dados para que as diferentes escalas das variáveis não distorcessem o cálculo de distância.
*   **Abordagem/Algoritmos:**
    *   **Clusterização:** O método principal foi a **Clusterização Hierárquica Aglomerativa**, usando a distância Euclidiana e o algoritmo de Ward para calcular a junção dos clusters.
    *   **Visualização:** Análise de Componentes Principais (PCA) foi usada para reduzir a dimensionalidade e visualizar os clusters em um gráfico 2D.
*   **Métricas de Avaliação:**
    *   **Métricas Internas:** Métricas como o coeficiente de silhueta (*Silhouette Score*) foram usadas para ajudar a determinar o número ideal de clusters.
*   **Resultados:**
    *   A análise apontou para a existência de **dois clusters principais** nos dados.
    *   O primeiro cluster era mais coeso e continha quase que exclusivamente os times de elite (ex: Manchester City, Real Madrid), caracterizados por alta posse de bola e domínio ofensivo.
    *   O segundo cluster era maior e mais difuso, agrupando os demais times com estilos mais variados e menos dominantes.

---

### Texto-Síntese Crítico

As pesquisas que examinamos, mesmo que abordem diferentes objetivos de aprendizado de máquina, convergem em relação à utilidade de usar modelos computacionais para obter informações relevantes sobre futebol. Ambos os estudos são unânimes em afirmar que a qualidade dos dados e a forma como são preparados são etapas essenciais. O estudo de Choi et al. (2023) ressalta como é importante equilibrar as classes para tarefas de classificação, enquanto Plakias et al. (2024) realça a importância de normalizar as características para algoritmos de agrupamento que se baseiam na distância. Isso demonstra que, independentemente da tarefa (seja supervisionada ou não), o preparo dos dados é crucial para um bom resultado.

É natural que as abordagens tomem rumos diferentes, considerando seus objetivos: uma se concentra em previsão (classificação), e a outra, em identificar padrões (agrupamento). A primeira busca um resultado direto e que pode ser medido (prever quem vai vencer), enquanto a segunda almeja um entendimento mais amplo e estratégico (identificar diferentes estilos de jogo). Uma questão ainda pendente é a junção dessas duas áreas. Os perfis táticos descobertos pelo agrupamento poderiam ser aproveitados como um dado valioso nos modelos de previsão, mas as pesquisas geralmente tratam essas análises de maneira separada. Além disso, ambos os estudos utilizam dados reunidos por temporada ou partida, negligenciando informações contextuais relevantes, como lesões, o estado emocional da equipe ou táticas específicas para cada adversário.

Nosso projeto está alinhado a essa situação atual, ao sugerir uma abordagem que une diferentes aspectos. Pretendemos executar as três tarefas (regressão, classificação e agrupamento) de maneira integrada, utilizando a mesma base de dados. Isso nos coloca em uma posição vantajosa para solucionar a lacuna identificada: poderemos, por exemplo, empregar os agrupamentos de estilos táticos como um novo dado para os modelos de previsão de gols e resultados, verificando se essa informação estratégica aprimora a capacidade de previsão. Assim, nosso trabalho não só reproduz as técnicas já existentes, mas também as conecta, resultando em uma análise mais abrangente e que gera mais valor sobre o desempenho no futebol.


# Descrição do _dataset_ selecionado

## Dataset — FootyStats CSV (Liga, Partidas, Times, Jogadores)

### 1) Identificação e Origem

- Nome oficial: FootyStats — Download Soccer/Football Stats CSV.
- Link de acesso: [footystats.org](https://footystats.org/download-stats-csv) (necessita conta paga/credits). 
- Fonte: FootyStats (plataforma proprietária com dados para 1.500+ ligas; também oferece API JSON).
- Licença/uso: Proprietária sob Termos & Condições da FootyStats; downloads são controlados por créditos (ex.: limite típico de 100 CSV/mês por usuário, sujeito ao plano).

### 2) Visão Geral

- **Arquivos principais disponíveis**:
  - `League.csv` → estatísticas agregadas por liga/temporada (~49 colunas).  
  - `Match.csv` → resultados e estatísticas por partida (~64 colunas).  
  - `Team.csv` → estatísticas agregadas por time (~186 colunas).  
  - `Team_Part2.csv` → continuação de métricas de time (~442 colunas).  
  - `Player.csv` → estatísticas individuais de jogadores (45+ colunas).  

- **Total de registros**: depende do número de ligas e temporadas baixadas.  
- **Cobertura temporal**: histórico e partidas futuras (dados em tempo real).  
- **Contexto**: dataset robusto para análises de desempenho esportivo, previsão de resultados, modelagem de métricas avançadas (xG, odds, posse, cartões, escanteios etc.).

### 3) Atributos (resumo)

### League CSV (≈49 colunas)
| Campo | Descrição | Tipo | Unidade | Exemplo |
|-------|-----------|------|---------|---------|
| name | Nome da liga | string | – | "Premier League" |
| season | Temporada | string | – | "2017/2018" |
| status | Status da temporada | string | – | "In Progress" |
| number_of_clubs | Nº de clubes | int | qtd | 20 |
| total_matches | Partidas agendadas | int | qtd | 380 |
| matches_completed | Partidas concluídas | int | qtd | 250 |
| progress | Progresso da temporada | float | % | 85.0 |
| average_goals_per_match | Gols médios/jogo | float | gols/jogo | 2.72 |
| average_corners_per_match | Escanteios médios/jogo | float | esc./jogo | 9.2 |
| average_cards_per_match | Cartões médios/jogo | float | cart./jogo | 4.1 |
| over_05_percentage ~ over_55_percentage | % de resultados Over (0.5 a 5.5) | float | % | 63.0 |
| goals_min_0_to_10 ~ goals_min_81_to_90 | Gols por intervalo de 10 min | float | gols | 0.28 |
| xg_avg | xG médio por jogo | float | xG | 2.75 |

### Match CSV (≈64 colunas)
| Campo | Descrição | Tipo | Unidade | Exemplo |
|-------|-----------|------|---------|---------|
| timestamp | Kick-off (Unix) | timestamp | epoch | 1487419800 |
| date_GMT | Kick-off GMT | string | data/hora | "Feb 18 2017 - 9:30am" |
| status | Estado da partida | string | – | "complete" |
| team_a_name / team_b_name | Times (casa/fora) | string | – | "Arsenal" / "Chelsea" |
| home_team_goal_count / away_team_goal_count | Gols | int | gols | 2 / 1 |
| home_team_corner_count / away_team_corner_count | Escanteios | int | esc. | 7 / 5 |
| home_team_shots / away_team_shots | Finalizações | int | – | 15 / 10 |
| home_team_possession / away_team_possession | Posse | float | % | 56.0 / 44.0 |
| odds_ft_home_team_win / draw / away_team_win | Odds FT | float | odds decimais | 1.85 / 3.50 / 4.20 |
| stadium_name | Estádio | string | – | "Emirates Stadium" |

### Team CSV (≈186 colunas) + Team CSV Pt.2 (≈442 colunas)
| Campo | Descrição | Tipo | Unidade | Exemplo |
|-------|-----------|------|---------|---------|
| team_name / common_name | Nome do time | string | – | "Manchester City" / "Man City" |
| season | Temporada | string | – | "2019/2020" |
| matches_played | Partidas jogadas | int | qtd | 38 |
| wins / draws / losses | Resultados | int | qtd | 26 / 7 / 5 |
| goals_scored / conceded | Gols marcados/sofridos | int | gols | 102 / 35 |
| league_position | Posição final | int | ranking | 2 |
| average_possession | Posse média | float | % | 60.5 |
| shots / shots_on_target | Finalizações | int | – | 580 / 240 |
| clean_sheets | Jogos sem sofrer gol | int | qtd | 16 |
| win_percentage | % de vitórias | float | % | 68.4 |
| xg_for_avg / xg_against_avg | xG For/Against | float | xG | 2.1 / 0.9 |

### Player CSV (45+ colunas)
| Campo | Descrição | Tipo | Unidade | Exemplo |
|-------|-----------|------|---------|---------|
| full_name | Nome do jogador | string | – | "Erling Haaland" |
| age | Idade | int | anos | 23 |
| nationality | Nacionalidade | string | – | "Norway" |
| current_club | Clube atual | string | – | "Man City" |
| appearances | Jogos disputados | int | qtd | 35 |
| goals / assists | Gols / assistências | int | – | 27 / 6 |
| minutes_played | Minutos jogados | int | min | 2850 |
| goals_per_90 | Gols por 90 min | float | gols/90 | 0.85 |
| yellow_cards_overall / red_cards_overall | Cartões | int | qtd | 3 / 0 |
| rank_in_league_top_attackers | Ranking (ataque) | int | posição | 1 |

### 4) Qualidade dos Dados

- **Valores faltantes**: estatísticas como *attendance*, árbitro, escanteios, cartões, posse de bola e *goal timings* podem não estar disponíveis em todas as ligas.  
- **Temporalidade**: jogos futuros aparecem com status `incomplete` e estatísticas nulas.  
- **Consistências internas**: checar que `matches_completed ≤ total_matches`; gols casa+fora = total; `shots_on_target ≤ shots`.  
- **Duplicatas**: baixa probabilidade; usar chaves compostas (ex.: `league+season`, `match_id/date`, `team+season`, `player+club+season`).  
- **Outliers**: valores extremos em escanteios/cartões são comuns em ligas menores; tratar estatisticamente.  
- **Odds**: armazenadas em formato decimal; converter para probabilidade quando necessário.  
- **Cobertura**: embora ampla (1.500+ ligas), a granularidade varia bastante por competição.  

### 5) Chaves Técnicas Recomendadas
- **League**: `league_name + season`  
- **Match**: `timestamp + team_a_name + team_b_name`  
- **Team**: `team_name + season`  
- **Player**: `full_name + current_club + season`  

# Canvas analítico

1. Question (Pergunta Central)

- Como prever o desempenho de jogadores e equipes em partidas futuras?
- Quais fatores mais influenciam vitórias, derrotas e empates?
- Como identificar talentos ou riscos de lesão?

2. Data Sources (Fontes de Dados)

- Estatísticas de partidas (posse, finalizações, passes, desarmes).
- Dados físicos (aceleração, distância percorrida, velocidade).
- Dados de contexto (clima, estádio, mando de campo, torcida).
- Dados históricos (resultados passados, desempenho por temporada).
- Dados de scouting e mercado (valor de jogador, idade, posição).

3. Heuristics (Heurísticas/Suposições)
- Nem todos os fatores têm o mesmo peso (ex.: posse ≠ vitória).
- Jogadores com performance consistente têm maior probabilidade de manter padrão.
- Lesões passadas aumentam risco futuro.
- O fator casa influencia fortemente os resultados.

4. Validation (Validação)

- Testes com dados históricos para medir precisão dos modelos.
- Comparação entre previsão e resultado real.
- Feedback de treinadores e analistas para validar insights.
- Visualização em dashboards (mapas de calor, gráficos de desempenho).

5. Implementation (Implementação)

- Coleta automática dos dados (via sensores, APIs, bancos de dados de jogos).
- Limpeza e tratamento dos dados.
- Treinamento de modelos de machine learning (regressão, árvores, redes neurais).
- Testes com validação cruzada.
- Deploy do modelo em ambiente de análise ou aplicativo para comissão técnica.

6. Results (Resultados Esperados)

- Previsões de resultado de jogos com base em dados históricos.
- Identificação de jogadores-chave para cada partida.
- Insights sobre condicionamento físico e risco de lesão.
- Apoio à tomada de decisão em escalações e contratações.

7. Next Steps (Próximos Passos)

- Refinar o modelo com dados em tempo real.
- Incorporar visão computacional (ex.: análise de vídeos de jogos).
- Expandir para previsão de mercado (valorização de atletas).
- Integração com ferramentas de gestão esportiva para tomada de decisão.

![alt text](analytic-canva.png)

**Dica:** O Canvas Analítico serve como guia visual para alinhar expectativas e direcionar o desenvolvimento. Ele poderá (e deverá) ser revisitado e atualizado ao longo do projeto.

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Vídeo de apresentação da Etapa 01

Nesta etapa, o grupo deverá produzir um vídeo de 5 a 8 minutos apresentando o trabalho realizado, no qual cada integrante deve dizer seu nome e apresentar uma parte do conteúdo desenvolvido, garantindo que todos participem ativamente da gravação. A ausência de participação de qualquer membro resultará em penalização na nota final desta etapa. Recomenda-se que o grupo elabore previamente um roteiro para organizar a ordem das falas, distribuir o tempo de forma equilibrada e assegurar que todos os tópicos relevantes sejam apresentados de maneira clara e objetiva.

# Referências

Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
