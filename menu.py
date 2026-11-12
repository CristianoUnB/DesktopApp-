from sala import Aluno, Professor, Relatorio, Turma


class Menu:
    def __init__(self):
        self.professores = []
        self.alunos = []
        self.turmas = []

    def executar(self):
        acoes = {
            "1": self.cadastrar_professor,
            "2": self.cadastrar_aluno,
            "3": self.criar_turma,
            "4": self.matricular_aluno,
            "5": self.remover_aluno,
            "6": self.lancar_nota,
            "7": self.ver_boletim,
            "8": self.apresentar_turma,
            "9": self.relatorio_da_turma,
            "10": self.listar_cadastros,
        }
        while True:
            self.mostrar_opcoes()
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "0":
                print("Até logo!")
                break
            acao = acoes.get(opcao)
            if acao is None:
                print("Opção inválida.")
                continue
            try:
                acao()
            except ValueError as erro:
                print("Erro:", erro)

    def mostrar_opcoes(self):
        print("\n===== Gerenciador =====")
        print("1  - Cadastrar professor")
        print("2  - Cadastrar aluno")
        print("3  - Criar turma")
        print("4  - Matricular aluno em turma")
        print("5  - Remover aluno de turma")
        print("6  - Lançar nota")
        print("7  - Ver boletim de um aluno")
        print("8  - Apresentar pessoas de uma turma")
        print("9  - Relatório da turma")
        print("10 - Listar cadastros")
        print("0  - Sair")

    def escolher(self, itens, rotulo, descrever):
        if not itens:
            raise ValueError(f"Nenhum cadastro de {rotulo} encontrado.")
        for posicao, item in enumerate(itens, start=1):
            print(f"  {posicao}. {descrever(item)}")
        try:
            numero = int(input(f"Número ({rotulo}): "))
        except ValueError:
            raise ValueError("Digite um número válido.") from None
        if not 1 <= numero <= len(itens):
            raise ValueError("Escolha inválida.")
        return itens[numero - 1]

    def escolher_professor(self):
        return self.escolher(self.professores, "professor", lambda p: p.apresentar())

    def escolher_aluno(self):
        return self.escolher(self.alunos, "aluno", lambda a: a.apresentar())

    def escolher_turma(self):
        return self.escolher(self.turmas, "turma", lambda t: t.nome)

    def cadastrar_professor(self):
        nome = input("Nome do professor: ")
        disciplina = input("Disciplina: ")
        self.professores.append(Professor(nome, disciplina))
        print("Professor cadastrado.")

    def cadastrar_aluno(self):
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula: ").strip()
        if not matricula:
            raise ValueError("A matrícula não pode ser vazia.")
        self.alunos.append(Aluno(nome, matricula))
        print("Aluno cadastrado.")

    def criar_turma(self):
        nome = input("Nome da turma: ").strip()
        if not nome:
            raise ValueError("O nome da turma não pode ser vazio.")
        professor = self.escolher_professor()
        self.turmas.append(Turma(nome, professor))
        print("Turma criada.")

    def matricular_aluno(self):
        turma = self.escolher_turma()
        aluno = self.escolher_aluno()
        turma.matricular(aluno)
        print(f"{aluno.nome} matriculado em {turma.nome}.")

    def remover_aluno(self):
        turma = self.escolher_turma()
        aluno = self.escolher(turma.alunos, "aluno", lambda a: a.apresentar())
        turma.remover(aluno)
        print(f"{aluno.nome} removido de {turma.nome}.")

    def lancar_nota(self):
        aluno = self.escolher_aluno()
        try:
            nota = float(input("Nota (0 a 10): ").replace(",", "."))
        except ValueError:
            raise ValueError("Digite uma nota válida.") from None
        aluno.adicionar_nota(nota)
        print(f"Nota lançada. Nova média de {aluno.nome}: {aluno.media()}")

    def ver_boletim(self):
        aluno = self.escolher_aluno()
        print(f"Notas de {aluno.nome}: {aluno.boletim.notas}")
        print(f"Média: {aluno.media()} - {aluno.boletim.situacao()}")

    def apresentar_turma(self):
        turma = self.escolher_turma()
        for linha in turma.apresentar_todos():
            print(linha)

    def relatorio_da_turma(self):
        turma = self.escolher_turma()
        print(Relatorio().gerar(turma))

    def listar_cadastros(self):
        print("Professores:")
        for professor in self.professores:
            print("  ", professor.apresentar())
        print("Alunos:")
        for aluno in self.alunos:
            print("  ", aluno.apresentar())
        print("Turmas:")
        for turma in self.turmas:
            print(f"   {turma.nome} - {len(turma.alunos)} aluno(s)")


if __name__ == "__main__":
    Menu().executar()
