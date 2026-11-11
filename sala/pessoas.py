from .boletim import Boletim


class Pessoa:
    def __init__(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.nome = nome.strip()

    def apresentar(self):
        return f"Pessoa: {self.nome}"


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        self.boletim = Boletim()

    def apresentar(self):
        return f"Aluno: {self.nome} (matrícula {self.matricula})"

    def adicionar_nota(self, nota):
        self.boletim.adicionar(nota)

    def media(self):
        return self.boletim.media()


class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self):
        return f"Professor: {self.nome} (disciplina {self.disciplina})"
