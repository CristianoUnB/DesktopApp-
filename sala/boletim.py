class Boletim:
    def __init__(self):
        self.notas = []

    def adicionar(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.notas.append(nota)

    def media(self):
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 2)

    def situacao(self):
        if not self.notas:
            return "Sem notas"
        return "Aprovado" if self.media() >= 5 else "Reprovado"
