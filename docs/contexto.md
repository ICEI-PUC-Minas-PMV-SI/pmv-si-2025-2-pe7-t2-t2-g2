# Introdução

Texto descritivo introdutório apresentando a visão geral do projeto a ser desenvolvido considerando o contexto em que ele se insere, os objetivos gerais, a justificativa e o público-alvo do projeto.

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

*estimar o número de gols por jogo,

*classificar o resultado da partida (vitória, empate ou derrota) e

*agrupar os clubes em perfis táticos de desempenho.

Objetivos Específicos

*Aplicar modelos de regressão (Regressão Linear, Random Forest Regressor e XGBoost) para estimar o número esperado de gols em cada partida, utilizando métricas como RMSE e R² para avaliar o desempenho.

*Comparar diferentes modelos de classificação supervisionada (Regressão Logística, Random Forest Classifier e XGBoost) para prever o desfecho de cada jogo, analisando métricas como acurácia, precisão, recall e F1-score.

*Explorar algoritmos de clusterização (K-Means, DBSCAN, HDBSCAN) para identificar padrões e agrupar os clubes em perfis táticos (ofensivo, defensivo, equilibrado), avaliando a qualidade dos agrupamentos por meio de métricas como Silhouette Score.

Otimizar os hiperparâmetros dos modelos selecionados a fim de melhorar as métricas de desempenho e maximizar a capacidade preditiva e explicativa das análises.

## Justificativa

Nesta seção, apresente a importância e a motivação para trabalhar com o conjunto de dados escolhido. Explique por que esse dataset é relevante e como ele se conecta ao problema identificado anteriormente.

Indique:
* Razões para a escolha dos objetivos específicos – Justifique por que decidiu aprofundar sua investigação nessas metas, relacionando-as ao potencial de solução ou melhoria para o problema.
* Relevância do estudo do problema – Mostre a importância de compreender e tratar a questão apresentada, tanto no contexto acadêmico quanto no profissional.
* Impacto social, econômico ou ambiental – Descreva como o problema afeta a sociedade ou um setor específico, buscando sempre quantificar o impacto por meio de dados reais.

**Importante:**
* Apresente números, estatísticas e informações concretas, citando as fontes (relatórios, artigos científicos, portais oficiais etc.).
* Mantenha a objetividade e a clareza, evitando argumentos genéricos.
* Construa um texto coeso que conecte o problema, os objetivos e a relevância do trabalho.

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)

## Público-Alvo

Nesta seção, descreva quem poderá se beneficiar com a sua investigação, apresentando os diferentes perfis de pessoas ou grupos impactados.

O objetivo aqui não é definir clientes específicos ou papéis exatos dentro da aplicação, mas sim compreender o perfil dos usuários e partes interessadas. Para isso, considere:
* Conhecimentos prévios relacionados ao domínio do problema e ao uso de tecnologia;
* Nível de familiaridade com recursos digitais e possíveis barreiras de uso;
* Contexto profissional e hierárquico, quando aplicável (ex.: nível de decisão, responsabilidades, área de atuação);
* Necessidades e expectativas que podem ser atendidas pelo projeto.

**Dica:** Seja objetivo e baseie suas descrições em informações reais ou plausíveis para o contexto escolhido. Isso ajudará a manter o foco no desenvolvimento de soluções relevantes e aplicáveis.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)

## Estado da arte

Nesta seção, descreva abordagens da literatura que tratam problemas semelhantes ao seu. Seu objetivo é documentar métodos, dados, métricas e resultados.

### O que levantar (mínimo 5 trabalhos)
Para **cada estudo encontrado** aderente à temática do grupo, registre de forma objetiva:
* Problema e contexto: que problema o trabalho buscou resolver e em qual domínio/cenário foi aplicado.
* Dados (dataset): origem, tamanho, período, variáveis/atributos, pré-processamentos relevantes (faltantes, balanceamento, normalização).
* Abordagem/algoritmos: algoritmos utilizados e parâmetros principais (quando informados).
* Métricas de avaliação: quais e por quê (ex.: Acurácia, F1, AUC, RMSE, MAE, etc.).
* Resultados: principais números, comparações internas, limitações citadas e conclusões.

* Texto-síntese crítico (2–4 parágrafos) respondendo:
- O que os estudos concordam? Onde divergem?
- Quais lacunas permanecem (dados, métricas, cenários, limitações técnicas/éticas)?
- Como seu projeto se alinha aos estudos identificados?

**Dica:** Prefira artigos dos últimos 5 anos ou referências clássicas indispensáveis.

### Ferramentas inteligentes permitidas
Você pode utilizar: Perplexity, SciSpace, Elicit, Research Rabbit, Litmaps.
Use-as para descoberta, organização e triagem de literatura. 

**Atenção:** 
* Sempre acesse a fonte original (PDF/artigo) antes de citar; verifique números e conclusões.
* Registre DOI/URL oficial e dados bibliográficos completos.
* Evite “alucinações” das ferramentas: desconfie de referências sem DOI ou que você não consiga localizar oficialmente.
* Use as ferramentas inteligentes para mapear redes de citação (Research Rabbit), mapas de tópicos (Litmaps), filtrar por período e gerar resumos iniciais (Perplexity/SciSpace/Elicit).
* Leia os trabalhos mais promissores e descarte estudos fora de escopo.

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

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

Nesta seção, você deverá estruturar e preencher o seu Canvas Analítico, que tem como objetivo registrar a organização das ideias e apresentar o modelo de negócio do projeto.

O Canvas deve ser preenchido integralmente, mesmo que algumas informações ainda não estejam totalmente definidas. Nessa etapa inicial, é aceitável trabalhar com hipóteses ou estimativas, desde que sejam coerentes com o problema e o contexto definidos.

**Dica:** O Canvas Analítico serve como guia visual para alinhar expectativas e direcionar o desenvolvimento. Ele poderá (e deverá) ser revisitado e atualizado ao longo do projeto.

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Vídeo de apresentação da Etapa 01

Nesta etapa, o grupo deverá produzir um vídeo de 5 a 8 minutos apresentando o trabalho realizado, no qual cada integrante deve dizer seu nome e apresentar uma parte do conteúdo desenvolvido, garantindo que todos participem ativamente da gravação. A ausência de participação de qualquer membro resultará em penalização na nota final desta etapa. Recomenda-se que o grupo elabore previamente um roteiro para organizar a ordem das falas, distribuir o tempo de forma equilibrada e assegurar que todos os tópicos relevantes sejam apresentados de maneira clara e objetiva.

# Referências

Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
