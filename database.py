import sqlite3

DB_PATH = "cinema.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS cinema (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            nome       TEXT    NOT NULL,
            capacidade INTEGER NOT NULL,
            logradouro TEXT    NOT NULL,
            cidade     TEXT    NOT NULL,
            estado     TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS filme (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo        TEXT    NOT NULL,
            duracao_min   INTEGER NOT NULL,
            genero        TEXT    NOT NULL,
            classificacao TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS cartaz (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id   INTEGER NOT NULL,
            filme_id    INTEGER NOT NULL,
            data_inicio TEXT    NOT NULL,
            data_fim    TEXT    NOT NULL,
            FOREIGN KEY (cinema_id) REFERENCES cinema(id),
            FOREIGN KEY (filme_id)  REFERENCES filme(id)
        );

        CREATE TABLE IF NOT EXISTS sessao (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            cartaz_id       INTEGER NOT NULL,
            data            TEXT    NOT NULL,
            horario_inicio  TEXT    NOT NULL,
            horario_termino TEXT    NOT NULL,
            FOREIGN KEY (cartaz_id) REFERENCES cartaz(id)
        );
    """)

    cursor.execute("SELECT COUNT(*) FROM cinema")
    if cursor.fetchone()[0] == 0:
        cursor.executescript("""
            INSERT INTO cinema (nome, capacidade, logradouro, cidade, estado) VALUES
                ('Cinemax Centro',   200, 'Av. Paulista, 1000', 'Sao Paulo',            'SP'),
                ('Cinemax Shopping', 150, 'Rua das Flores, 50', 'Vargem Grande do Sul', 'SP');

            INSERT INTO filme (titulo, duracao_min, genero, classificacao) VALUES
                ('Interestelar',       169, 'Ficcao Cientifica', '12 anos'),
                ('O Poderoso Chefao', 175, 'Drama',              '16 anos'),
                ('Inception',          148, 'Ficcao Cientifica', '12 anos');

            INSERT INTO cartaz (cinema_id, filme_id, data_inicio, data_fim) VALUES
                (1, 1, '2026-05-01', '2026-05-31'),
                (1, 3, '2026-05-01', '2026-05-31'),
                (2, 2, '2026-05-01', '2026-05-31');

            INSERT INTO sessao (cartaz_id, data, horario_inicio, horario_termino) VALUES
                (1, '2026-05-07', '14:00', '16:49'),
                (1, '2026-05-07', '18:00', '20:49'),
                (2, '2026-05-07', '15:00', '17:28'),
                (3, '2026-05-07', '19:00', '21:55');
        """)

    conn.commit()
    conn.close()
