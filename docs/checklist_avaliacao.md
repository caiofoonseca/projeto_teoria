# Checklist para Nota Máxima

## Situação Atual

| Requisito | Status | Observação |
| --- | --- | --- |
| Equipe com 3 ou 4 integrantes | Feito | Grupo possui 3 integrantes. |
| Duas linguagens distintas | Feito | C e Python. |
| Implementação do algoritmo | Feito | Quick Sort em C e Python. |
| Código bem estruturado | Feito | Código organizado em `src/`, `scripts/`, `data/`, `plots/`, `examples/` e `docs/`. |
| Testes funcionais | Feito | C e Python passaram em 5/5 testes. |
| Análise Big-O, Big-Omega e Big-Theta | Feito | Análise incluída no relatório final e nos slides. |
| Melhor, médio e pior caso | Feito | Benchmarks executados para os três cenários. |
| 30 rodadas por tamanho/caso/linguagem | Feito | `data/resultados.csv` possui as médias e desvios-padrão. |
| Entradas pequena, média e grande | Feito | Foram usados 100, 1000 e 3000 elementos. |
| Tabelas com tempos | Feito | Resultados salvos em `data/resultados.csv`. |
| Gráficos com curva teórica | Feito | Gráficos gerados em `plots/`. |
| Descrição de hardware | Feito | Ambiente de execução preenchido no relatório com CPU, RAM, SO e modelo do notebook. |
| Relatório em PDF | Feito | Relatório final salvo em `docs/relatorio_final.pdf`. |
| Slides | Feito | Apresentação salva em `docs/apresentacao_quicksort.pdf`. |
| Link do GitHub no relatório/Classroom | Feito | Link incluído no README, no relatório e nos slides. |

## Observação sobre Entrada e Saída

A especificação recebida não determina que o programa seja obrigado a ler um arquivo chamado `entrada.txt` nem gerar um arquivo chamado `saida.txt`.

No projeto atual:

- `examples/entrada.txt` e `examples/saida.txt` são exemplos de uso e validação.
- O programa lê os dados pela entrada padrão.
- O usuário pode digitar os dados manualmente ou redirecionar um arquivo. No PowerShell, use `Get-Content examples/entrada.txt | python src/python/quicksort.py` ou `Get-Content examples/entrada.txt | .\build\quicksort.exe`.

Se o professor informar um formato obrigatório diferente, o código deve ser ajustado exatamente para esse formato.
