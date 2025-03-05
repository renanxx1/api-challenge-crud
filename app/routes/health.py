from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health Check"])
def health_check():
    """
    Este módulo fornece um endpoint simples para verificar se a API está rodando corretamente.
    O objetivo é permitir que ferramentas de monitoramento e balanceadores de carga 
    possam verificar a disponibilidade do serviço.

    - **Método:** GET
    - **Rota:** `/health`
    - **Tags:** ["Health Check"]

    - **Retorno:**
        - `200 OK` com um JSON indicando que a API está funcional.
    """
    return {"status": "ok"}
