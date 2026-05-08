import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from database import init_db
from controller import handle_listar_cinemas, handle_consultar_cartaz


def exibir_cinemas(cinemas):
    print("\n=== Unidades disponíveis ===")
    for c in cinemas:
        print(f"  [{c['id']}] {c['nome']} — {c['cidade']}/{c['estado']}")


def exibir_cartaz(filmes):
    print("\n=== Filmes em Cartaz ===")
    for filme in filmes:
        print(f"\n  Título        : {filme['titulo']}")
        print(f"  Gênero        : {filme['genero']}")
        print(f"  Classificação : {filme['classificacao']}")
        print(f"  Sessões:")
        for s in filme["sessoes"]:
            print(f"    • {s['data']}  {s['inicio']} → {s['termino']}")


def main():
    init_db()

    print("╔════════════════════════════════╗")
    print("║   Sistema de Rede de Cinemas   ║")
    print("╚════════════════════════════════╝")

    while True:
        print("\n[1] Consultar filmes em cartaz por unidade")
        print("[0] Sair")
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando sistema.")
            break

        elif opcao == "1":
            resultado = handle_listar_cinemas()
            if not resultado["sucesso"]:
                print(f"\nErro: {resultado['erro']}")
                continue

            exibir_cinemas(resultado["dados"])

            try:
                cinema_id = int(input("\nDigite o ID da unidade: ").strip())
            except ValueError:
                print("ID inválido.")
                continue

            resultado_cartaz = handle_consultar_cartaz(cinema_id)
            if not resultado_cartaz["sucesso"]:
                print(f"\nAviso: {resultado_cartaz['erro']}")
            else:
                exibir_cartaz(resultado_cartaz["dados"])

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
