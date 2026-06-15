# Checklist para Nota Maxima

## Situacao Atual

| Requisito | Status | Observacao |
| --- | --- | --- |
| Equipe com 3 ou 4 integrantes | Feito | Grupo possui 3 integrantes. |
| Duas linguagens distintas | Feito | C e Python. |
| Implementacao do algoritmo | Feito | Quick Sort em C e Python. |
| Codigo bem estruturado | Em andamento | Estrutura inicial criada; ainda pode receber comentarios e organizacao final. |
| Testes funcionais | Feito | C e Python passaram em 5/5 testes. |
| Analise Big-O, Big-Omega e Big-Theta | Em andamento | Base adicionada ao relatorio; pode ser expandida na versao final. |
| Melhor, medio e pior caso | Feito | Benchmarks executados para os tres cenarios. |
| 30 rodadas por tamanho/caso/linguagem | Feito | `data/resultados.csv` possui as medias e desvios-padrao. |
| Entradas pequena, media e grande | Feito | Foram usados 100, 1000 e 3000 elementos. |
| Tabelas com tempos | Feito | Resultados salvos em `data/resultados.csv`. |
| Graficos com curva teorica | Feito | Graficos gerados em `plots/`. |
| Descricao de hardware | Feito | Ambiente de execucao preenchido no relatorio com CPU, RAM, SO e modelo do notebook. |
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
