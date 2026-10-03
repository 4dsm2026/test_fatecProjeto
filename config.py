import os

# URL do frontend rodando localmente (pnpm dev). Ajuste via variável de
# ambiente BASE_URL se a porta/host forem diferentes.
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")

# Timeout padrão (segundos) para as esperas explícitas do Selenium.
DEFAULT_TIMEOUT = int(os.getenv("SELENIUM_TIMEOUT", "10"))

# HEADLESS=false roda o Chrome com interface visível (útil para debugar).
HEADLESS = os.getenv("HEADLESS", "true").lower() != "false"

# Usuários criados pelo `pnpm prisma:seed` no backend_fatecProjeto.
USERS = {
    "admin": {
        "mode": "email",
        "identifier": "admin@example.com",
        "password": "wf-fatec2026",
        "papel": "ADMINISTRADOR",
        "primeiro_acesso": False,
        "home": "/admin/home",
    },
    "backoffice": {
        "mode": "email",
        "identifier": "ana.costa@fatec.sp.gov.br",
        "password": "Fatec@2026",
        "papel": "BACKOFFICE",
        "primeiro_acesso": True,
        "home": "/admin/home",
    },
    "aluno_1": {
        "mode": "ra",
        "identifier": "123456789",
        "password": "Fatec@2026",
        "papel": "USUARIO",
        "primeiro_acesso": True,
        "home": "/aluno/home",
    },
    "aluno_2": {
        "mode": "ra",
        "identifier": "987654321",
        "password": "Fatec@2026",
        "papel": "USUARIO",
        "primeiro_acesso": True,
        "home": "/aluno/home",
    },
    "aluno_3": {
        "mode": "ra",
        "identifier": "998877665",
        "password": "Fatec@2026",
        "papel": "USUARIO",
        "primeiro_acesso": True,
        "home": "/aluno/home",
    },
}
