TCC00289 - COMPILADORES - A12020 / 1º
Tradução de declarações Imp à Π IR
Christiano Braga
•
8 de jul. Editado às 25 de jul.
100 pontos
Data de entrega: 30 de jul.
1. Baixe o arquivo anexo no seu repositório Git Hub do curso.
2. Crie o arquivo examples/fibo.imp2 contendo uma implementação iterativa da função de Fibonacci e que calcule Fibonacci de 10.
3. Atribua valores apropriados às variáveis no arquivo de teste imp2-transf-to-piir-decl-test.py de forma a obter o seguinte ao executá-lo:

$ python3 imp2-transf-to-piir-decl-test.py -v
test_fibo (__main__.TestImpToPiIRDecl) ... ok
test_run (__main__.TestImpToPiIRDecl) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.966s

OK
4. Faça um commit e um pull para o seu repositório Git Hub.
imp2-transf-to-piir-decl-test.allana.py
Texto

Comentários da turma
Seus trabalhos
Atribuído
Comentários particulares

import unittest
import tatsu
from impiler import Impiler
from pi import run

class TestImpToPiIRDecl(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_parse(self, file_name, ast):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        self.assertEqual(str(pi_ast), ast)

    def __test_run(self, file_name, s, locs, env, sto, val, cnt):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        (tr, ns, dt) = run(pi_ast)
        state_str = tr[s]
        loc_str = "locs : " + locs
        env_str = "env : " + env
        sto_str = "sto : " + sto
        val_str = "val : " + val
        cnt_str = "cnt : " + cnt
        self.assertTrue(loc_str in state_str)
        self.assertTrue(env_str in state_str)
        self.assertTrue(sto_str in state_str)
        self.assertTrue(val_str in state_str)
        self.assertTrue(cnt_str in state_str)                        
        
    def test_fibo(self):
        self.__test_parse('examples/fibo.imp2', "Blk(DSeq(DSeq(DSeq(Bind(Id(n), Ref(Num(10))), Bind(Id(i), Ref(Num(0)))), Bind(Id(j), Ref(Num(1)))), Bind(Id(k), Ref(Num(1)))), Loop(Lt(Id(k), Id(n)), Blk(Bind(Id(t), Ref(Num(0))), CSeq(CSeq(CSeq(Assign(Id(t), Sum(Id(i), Id(j))), Assign(Id(i), Id(j))), Assign(Id(j), Id(t))), Assign(Id(k), Sum(Id(k), Num(1)))))))")

    def test_run(self):
        # Qual o menor estado que no qual fiboncci n está calculado?
        s = 0
        # Qual o estado do componente locs (BlockLocs) em s?
        locs = "?"
        # Qual o estado do componente env (Ambiente) em s?
        env = "?"
        # Qual o estado do componente sto (Memória) em s?
        sto = "?"
        # Qual o estado do componente val (Pilha de valores) em s?
        val = "?"
        # Qual o estado do componente cnt (Pilha de controle) em s?
        cnt = "?"
        self.__test_run('examples/fibo.imp2', s, locs, env, sto, val, cnt)
        
if __name__ == '__main__':
    unittest.main()

