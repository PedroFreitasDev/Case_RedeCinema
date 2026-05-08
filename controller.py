from service import obter_cinemas, obter_filmes_em_cartaz


def handle_listar_cinemas():
    try:
        return {"sucesso": True, "dados": obter_cinemas()}
    except ValueError as e:
        return {"sucesso": False, "erro": str(e)}


def handle_consultar_cartaz(cinema_id: int):
    filmes = obter_filmes_em_cartaz(cinema_id)
    if filmes is None:
        return {"sucesso": False, "erro": "Nenhum filme em cartaz para esta unidade."}
    return {"sucesso": True, "dados": filmes}
