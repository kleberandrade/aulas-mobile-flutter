# 02 · Formulários e validação

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulo 1; estado básico de um widget.

## Objetivos

Separar campos, conversão e regras de cálculo. Oferecer mensagens úteis e resultados reproduzíveis.

## Atividade orientadora

Escolha uma calculadora, execute o fluxo atual e acrescente um caso de validação com teste. Use a regra e as unidades documentadas no estudo escolhido.

As calculadoras representam domínios diferentes. Não transfira uma fórmula ou regra de arredondamento entre elas sem justificativa.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[A Ordem do Código Limpo](../../docs/books.md): discuta nomes e regras compreensíveis ao revisar o formulário.

## Estudos de caso e referências

- [calculadora-imc-aulas-flutter](https://github.com/kleberandrade/calculadora-imc-aulas-flutter) — consulte o README e o código atuais.
- [interest-calculator-flutter](https://github.com/kleberandrade/interest-calculator-flutter) — consulte o README e o código atuais.
- [floor-calculator-flutter](https://github.com/kleberandrade/floor-calculator-flutter) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Campos obrigatórios.** Objetivo: Validar um formulário vazio. Conclusão: mostrar erros junto aos campos sem produzir resultado fictício.

2. **Conversão.** Objetivo: Definir a entrada numérica aceita. Conclusão: demonstrar separador decimal, texto inválido e comportamento documentado.

3. **Unidades.** Objetivo: Explicitar grandezas usadas. Conclusão: rótulos e resultados coerentes, com teste de um valor calculado de forma independente.

4. **Regra isolada.** Objetivo: Extrair um cálculo da interface. Conclusão: testar a regra sem inicializar widgets.

5. **Interação.** Objetivo: Verificar o formulário completo. Conclusão: teste de widget preenche campos, calcula e cobre pelo menos uma correção após erro.
