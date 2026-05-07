

## 1. Requisitos Funcionais Principais
 
| ID | Requisito |
|----|-----------|
| RF01 | Cadastrar unidades de cinema com capacidade e endereço completo (logradouro, cidade, estado) |
| RF02 | Cadastrar filmes com título, duração, gênero, diretor e elenco |
| RF03 | Associar filmes em cartaz a uma unidade de cinema |
| RF04 | Cadastrar sessões de um filme em uma unidade, com data, horário de início e horário de término |
| RF05 | Registrar o público diário de cada sessão |
| RF06 | Consultar o total de público por sessão |
| RF07 | Consultar o total de público por filme (somando todas as sessões) |
| RF08 | Consultar o total de público por unidade de cinema |
| RF09 | Consultar informações de elenco, diretor e gênero de um filme |
| RF10 | Listar filmes em cartaz em uma determinada unidade |
| RF11 | Listar sessões disponíveis de um filme em uma unidade |
 
---
 
## 2. Regras de Negócio Essenciais
 
| ID | Regra |
|----|-------|
| RN01 | Uma sessão não pode ser agendada se o horário conflitar com outra sessão na mesma sala/unidade |
| RN02 | O intervalo mínimo entre o término de uma sessão e o início da próxima deve ser respeitado (ex.: 20 minutos) |
| RN03 | O horário de término da sessão deve ser calculado automaticamente com base no horário de início e na duração do filme |
| RN04 | O público registrado em uma sessão não pode exceder a capacidade da unidade de cinema |
| RN05 | Um filme só pode ser exibido em uma unidade se estiver associado ao seu programa de exibição (cartaz) |
| RN06 | Cada sessão pertence a exatamente um filme e a exatamente uma unidade de cinema |
| RN07 | Um filme pode ter múltiplos diretores e múltiplos atores (relacionamento N:N) |
| RN08 | O registro de público é diário e vinculado a uma sessão específica |
 
---
 
## 3. Atores do Sistema
 
- **Administrador/Funcionário:** responsável por cadastrar cinemas, filmes, sessões e registrar o público.
- **Espectador:** consulta filmes em cartaz, sessões disponíveis e informações sobre os filmes.
 
