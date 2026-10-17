# Testes de ponta a ponta — WorkFlow FATEC

Testes automatizados com **Selenium** e **pytest** que usam o sistema pelo navegador, como uma pessoa usaria: abrem o frontend, fazem login e verificam para onde cada perfil é levado.

## O que é testado

| Arquivo | Cobre |
|---|---|
| `test_login.py` | Login de administrador, primeiro acesso (troca de senha obrigatória), senha errada, troca entre as abas Funcionário e Aluno (RA), senha curta e botão de mostrar senha |
| `test_route_protection.py` | Redirecionamento para `/login` sem sessão e bloqueio de rotas de outro perfil (ex.: admin em `/aluno`) |

As páginas seguem o padrão *Page Object*: os seletores e ações de cada tela ficam em `pages/` (`login_page.py`, `base_page.py`), e os testes só descrevem o comportamento esperado.

## Pré-requisitos

1. **Backend** rodando com o banco populado — siga o [README do backend](https://github.com/4dsm2026/backend_fatecProjeto#readme), incluindo `pnpm prisma:seed`. Os testes usam os usuários do seed (listados em `config.py`).
2. **Frontend** rodando em `http://localhost:3000` — siga o [README do frontend](https://github.com/4dsm2026/frontend_fatecProjeto#readme).
3. **Python 3.10+** e **Google Chrome**. O Selenium baixa o chromedriver sozinho.

> Os testes de primeiro acesso esperam que os usuários do seed **ainda não tenham trocado a senha**. Se você já trocou, rode o seed de novo.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
git config core.hooksPath .githooks
```

O último comando ativa os hooks do git (padrão de commit e bloqueio de arquivos grandes) — veja o [guia de contribuição](https://github.com/4dsm2026/.github/blob/main/CONTRIBUTING.md#hooks-do-git).

## Como rodar

```bash
pytest                             # todos os testes, Chrome invisível
pytest test_login.py               # um arquivo
pytest -k first_access             # testes cujo nome contém o texto
HEADLESS=false pytest test_login.py  # abre o Chrome na tela (bom para depurar)
```

### Variáveis de ambiente

| Variável | Padrão | Uso |
|---|---|---|
| `BASE_URL` | `http://localhost:3000` | Endereço do frontend |
| `HEADLESS` | `true` | `false` mostra o navegador |
| `SELENIUM_TIMEOUT` | `10` | Segundos de espera por cada elemento |

## Escrevendo um teste novo

1. Se a tela ainda não tem *Page Object*, crie um em `pages/` herdando de `BasePage`, com os seletores como constantes da classe.
2. Escreva o teste em um arquivo `test_<assunto>.py`, usando a fixture `driver` (definida em `conftest.py`).
3. Indique na docstring a issue ou história de usuário que o teste verifica.

## Contribuindo

Siga o [guia de contribuição da organização](https://github.com/4dsm2026/.github/blob/main/CONTRIBUTING.md). Neste repositório, os PRs vão direto para `main`.
