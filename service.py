from repository import listar_cinemas, buscar_filmes_por_cinema


def obter_cinemas():
    cinemas = listar_cinemas()
    if not cinemas:
        raise ValueError("Nenhuma unidade de cinema cadastrada.")
    return cinemas


def obter_filmes_em_cartaz(cinema_id: int):
    resultados = buscar_filmes_por_cinema(cinema_id)
    if not resultados:
        return None  # nenhum filme encontrado

    # Agrupa sessões por filme
    filmes = {}
    for row in resultados:
        fid = row["filme_id"]
        if fid not in filmes:
            filmes[fid] = {
                "titulo": row["titulo"],
                "genero": row["genero"],
                "classificacao": row["classificacao"],
                "sessoes": []
            }
        filmes[fid]["sessoes"].append({
            "data": row["data"],
            "inicio": row["horario_inicio"],
            "termino": row["horario_termino"]
        })

    return list(filmes.values())
