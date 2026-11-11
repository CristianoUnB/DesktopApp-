class Relatorio:
    def gerar(self, turma):
        linhas = [f"Turma {turma.nome} - {turma.professor.nome}"]
        for aluno in turma.alunos:
            linhas.append(
                f"{aluno.nome}: média {aluno.media()} ({aluno.boletim.situacao()})"
            )
        linhas.append(f"Média da turma: {turma.media_da_turma()}")
        return "\n".join(linhas)
