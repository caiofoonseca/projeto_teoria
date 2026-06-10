# Checklist para Nota Maxima

## Situacao Atual

| Requisito | Status | Observacao |
| --- | --- | --- |
| Equipe com 3 ou 4 integrantes | Feito | Grupo possui 4 integrantes. |
| Duas linguagens distintas | Feito | C e Python. |
| Implementacao do algoritmo | Feito | Quick Sort em C e Python. |
| Codigo bem estruturado | Em andamento | Estrutura inicial criada; ainda pode receber comentarios e organizacao final. |
| Testes funcionais | Em andamento | Ha testes automaticos; C depende de `gcc` instalado. |
| Analise Big-O, Big-Omega e Big-Theta | Pendente | Deve entrar no relatorio. |
| Melhor, medio e pior caso | Em andamento | Benchmarks foram estruturados; falta executar e analisar resultados finais. |
| 30 rodadas por tamanho/caso/linguagem | Em andamento | Script de benchmark preparado para isso. |
| Entradas pequena, media e grande | Em andamento | Script usa 100, 1000 e 3000 elementos. |
| Tabelas com tempos | Em andamento | `data/resultados.csv` sera gerado pelo benchmark. |
| Graficos com curva teorica | Em andamento | Script de graficos preparado; depende de `matplotlib`. |
| Descricao de hardware | Pendente | Preencher com o computador usado nos testes finais. |
| Relatorio em PDF | Pendente | Base em Markdown criada; falta desenvolver e exportar para PDF. |
| Slides | Pendente | Ainda precisam ser criados. |
| Link do GitHub no relatorio/Classroom | Em andamento | README ja possui o link. |

## Observacao sobre Entrada e Saida

A especificacao recebida nao determina que o programa seja obrigado a ler um arquivo chamado `entrada.txt` nem gerar um arquivo chamado `saida.txt`.

No projeto atual:

- `examples/entrada.txt` e `examples/saida.txt` sao exemplos de uso e validacao.
- O programa le os dados pela entrada padrao.
- O usuario pode digitar os dados manualmente ou redirecionar um arquivo com `< examples/entrada.txt`.

Se o professor informar um formato obrigatorio diferente, o codigo deve ser ajustado exatamente para esse formato.
