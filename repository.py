from database import get_connection


def listar_cinemas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, cidade, estado FROM cinema ORDER BY cidade")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def buscar_filmes_por_cinema(cinema_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            f.id          AS filme_id,
            f.titulo,
            f.genero,
            f.classificacao,
            s.horario_inicio,
            s.horario_termino,
            s.data
        FROM cartaz c
        JOIN filme  f ON f.id = c.filme_id
        JOIN sessao s ON s.cartaz_id = c.id
        WHERE c.cinema_id = ?
        ORDER BY f.titulo, s.horario_inicio
    """, (cinema_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
