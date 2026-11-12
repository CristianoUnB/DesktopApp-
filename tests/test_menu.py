import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from menu import Menu


def executar_com(entradas):
    menu = Menu()
    saida = StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(saida):
        menu.executar()
    return menu, saida.getvalue()


class TestMenu(unittest.TestCase):
    def test_fluxo_completo(self):
        menu, saida = executar_com([
            "1", "Carlos", "Matemática",
            "2", "Ana", "1",
            "2", "Bruno", "2",
            "3", "8A", "1",
            "4", "1", "1",
            "4", "1", "2",
            "6", "1", "8",
            "6", "1", "10",
            "7", "1",
            "8", "1",
            "9", "1",
            "10",
            "5", "1", "2",
            "0",
        ])
        self.assertEqual(len(menu.professores), 1)
        self.assertEqual(len(menu.alunos), 2)
        self.assertEqual([a.nome for a in menu.turmas[0].alunos], ["Ana"])
        self.assertEqual(menu.alunos[0].media(), 9.0)
        self.assertIn("Média da turma", saida)
        self.assertIn("Aprovado", saida)

    def test_erros_nao_quebram_o_menu(self):
        menu, saida = executar_com([
            "x",            # opção inválida
            "3", "8A",     # criar turma sem professor
            "6",            # nota sem alunos
            "1", " ", "Fis",  # nome vazio
            "2", "Ana", "",   # matrícula vazia
            "2", "Ana", "1",
            "6", "1", "abc",  # nota inválida
            "6", "1", "11",   # nota fora do intervalo
            "6", "5",         # aluno inexistente
            "0",
        ])
        self.assertIn("Opção inválida", saida)
        self.assertIn("Nenhum cadastro de professor", saida)
        self.assertIn("Nenhum cadastro de aluno", saida)
        self.assertIn("O nome não pode ser vazio", saida)
        self.assertIn("A matrícula não pode ser vazia", saida)
        self.assertIn("Digite uma nota válida", saida)
        self.assertIn("A nota deve estar entre 0 e 10", saida)
        self.assertIn("Escolha inválida", saida)
        self.assertEqual(menu.alunos[0].boletim.notas, [])


if __name__ == "__main__":
    unittest.main()
