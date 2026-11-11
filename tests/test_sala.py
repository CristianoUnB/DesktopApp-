import unittest

from sala import Aluno, Pessoa, Professor, Relatorio, Turma


class TestSala(unittest.TestCase):
    def setUp(self):
        self.professor = Professor("Carlos", "Matemática")
        self.ana = Aluno("Ana", "1")
        self.bruno = Aluno("Bruno", "2")
        self.turma = Turma("8A", self.professor)
        self.turma.matricular(self.ana)
        self.turma.matricular(self.bruno)

    def test_tipos(self):
        self.assertIsInstance(self.ana, Pessoa)
        self.assertIsInstance(self.professor, Pessoa)
        self.assertNotIsInstance(self.professor, Aluno)

    def test_apresentar_de_cada_tipo(self):
        self.assertTrue(self.ana.apresentar().startswith("Aluno"))
        self.assertTrue(self.professor.apresentar().startswith("Professor"))
        self.assertTrue(Pessoa("X").apresentar().startswith("Pessoa"))

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            Pessoa("  ")

    def test_notas_e_media(self):
        for nota in (8, 6):
            self.ana.adicionar_nota(nota)
        self.assertEqual(self.ana.media(), 7.0)
        self.assertEqual(self.ana.boletim.situacao(), "Aprovado")

    def test_situacoes(self):
        self.assertEqual(self.ana.boletim.situacao(), "Sem notas")
        self.bruno.adicionar_nota(3)
        self.assertEqual(self.bruno.boletim.situacao(), "Reprovado")

    def test_nota_invalida(self):
        with self.assertRaises(ValueError):
            self.ana.adicionar_nota(-1)
        with self.assertRaises(ValueError):
            self.ana.adicionar_nota(10.5)

    def test_boletins_separados(self):
        self.ana.adicionar_nota(10)
        self.assertEqual(self.bruno.boletim.notas, [])

    def test_matricula_e_remocao(self):
        with self.assertRaises(ValueError):
            self.turma.matricular(self.ana)
        self.turma.remover(self.ana)
        self.assertEqual(self.turma.alunos, [self.bruno])
        with self.assertRaises(ValueError):
            self.turma.remover(self.ana)

    def test_apresentar_todos(self):
        linhas = self.turma.apresentar_todos()
        self.assertEqual(len(linhas), 3)
        self.assertTrue(linhas[0].startswith("Professor"))

    def test_media_da_turma(self):
        self.assertEqual(self.turma.media_da_turma(), 0.0)
        self.ana.adicionar_nota(10)
        self.bruno.adicionar_nota(6)
        self.assertEqual(self.turma.media_da_turma(), 8.0)
        self.assertEqual(Turma("V", self.professor).media_da_turma(), 0.0)

    def test_relatorio(self):
        self.ana.adicionar_nota(9)
        texto = Relatorio().gerar(self.turma)
        self.assertIn("Ana", texto)
        self.assertIn("Média da turma", texto)


if __name__ == "__main__":
    unittest.main()
