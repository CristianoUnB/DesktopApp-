class Turma:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def matricular(self, aluno):
        if aluno in self.alunos:
            raise ValueError(f"{aluno.nome} já está na turma.")
        self.alunos.append(aluno)

    def remover(self, aluno):
        if aluno not in self.alunos:
            raise ValueError(f"{aluno.nome} não está na turma.")
        self.alunos.remove(aluno)

    def apresentar_todos(self):
        pessoas = [self.professor] + self.alunos
        return [pessoa.apresentar() for pessoa in pessoas]

    def media_da_turma(self):
        if not self.alunos:
            return 0.0
        total = sum(aluno.media() for aluno in self.alunos)
        return round(total / len(self.alunos), 2)
