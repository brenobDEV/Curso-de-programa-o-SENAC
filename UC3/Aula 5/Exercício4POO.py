'''Exercício 4: O Gerador de Relatórios (Foco em Polimorfismo)
Contexto: O polimorfismo permite que o servidor chame exatamente o mesmo método em
objetos de tipos diferentes, e cada um deles responderá com seu próprio comportamento
específico.
Tarefas:
1. Crie duas classes independentes: RelatorioPDF e RelatorioExcel.
2. Ambas as classes devem possuir um método com exatamente o mesmo nome e
parâmetros: gerar(self, dados).
3. Regras de comportamento:
○ Na classe RelatorioPDF, o método deve imprimir: "Gerando arquivo PDF
com os dados: [dados]..."
○ Na classe RelatorioExcel, o método deve imprimir: "Gerando planilha
Excel com os dados: [dados]..."
4. O Teste Polimórfico: Crie uma lista contendo uma instância de RelatorioPDF e
uma instância de RelatorioExcel. Faça um laço for que percorra essa lista e
chame o método gerar("Vendas de Maio") para cada objeto, sem usar
nenhum comando if.'''


