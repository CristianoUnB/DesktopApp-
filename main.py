from sala import Aluno, Pessoa, Professor, Relatorio, Turma


def titulo(texto):
    print(f"\n--- {texto} ---")


def main():
    titulo("Cadastro de pessoas")
    professor = Professor("Carlos Souza", "Matemática")
    ana = Aluno("Ana Lima", "2026001")
    bruno = Aluno("Bruno Reis", "2026002")
    print(professor.apresentar())
    print(ana.apresentar())
    print(bruno.apresentar())
    print(Pessoa("Visitante").apresentar())

    titulo("Criação da turma e matrículas")
    turma = Turma("8º A", professor)
    turma.matricular(ana)
    turma.matricular(bruno)
    for linha in turma.apresentar_todos():
        print(linha)

    titulo("Lançamento de notas")
    for nota in (8, 7, 9):
        ana.adicionar_nota(nota)
    for nota in (4, 5):
        bruno.adicionar_nota(nota)
    print(f"{ana.nome}: notas {ana.boletim.notas} -> média {ana.media()}")
    print(f"{bruno.nome}: notas {bruno.boletim.notas} -> média {bruno.media()}")
    print("Situação da Ana:", ana.boletim.situacao())
    print("Situação do Bruno:", bruno.boletim.situacao())

    titulo("Relatório da turma")
    print(Relatorio().gerar(turma))

    titulo("Remoção de aluno")
    turma.remover(bruno)
    print("Alunos na turma:", [a.nome for a in turma.alunos])

    titulo("Erros tratados")
    for acao in (lambda: turma.matricular(ana),
                 lambda: turma.remover(bruno),
                 lambda: ana.adicionar_nota(11),
                 lambda: Aluno("  ", "1")):
        try:
            acao()
        except ValueError as erro:
            print("Erro esperado:", erro)


if __name__ == "__main__":
    main()
