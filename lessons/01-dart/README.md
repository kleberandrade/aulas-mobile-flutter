# 01 · Fundamentos de Dart e orientação a objetos

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Lógica de programação; funções e estruturas de controle.

## Objetivos

Tipos, null safety, coleções, funções e classes. Modelar regras sem depender da interface.

## Atividade orientadora

Implemente no seu repositório um pequeno inventário no terminal. Separe os dados dos comandos e trate entradas inválidas.

Estude o Masmorra ASCII como percurso paralelo: fundamentos e orientação a objetos antes das etapas avançadas. O jogo usa terminal, não widgets Flutter.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[Masmorra ASCII](../../docs/books.md): comece pelos fundamentos e pela orientação a objetos no terminal.

## Estudos de caso e referências

- [roguelike-dart](https://github.com/kleberandrade/roguelike-dart) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).
- [Masmorra ASCII](https://masmorra.io/): fundamentos em Dart, persistência e organização de um jogo no terminal.

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Tipos e validação.** Objetivo: Receber quantidade e nome de um item. Conclusão: rejeitar nome vazio e quantidade negativa sem encerrar o programa.

2. **Coleções.** Objetivo: Adicionar e consultar itens por nome. Conclusão: demonstrar coleção vazia, busca existente e busca sem resultado.

3. **Classes.** Objetivo: Representar um item como valor tipado. Conclusão: construção inválida impedida ou rejeitada de forma explícita.

4. **Null safety.** Objetivo: Modelar uma busca que pode não encontrar item. Conclusão: tratar a ausência sem usar uma asserção de não nulidade para ignorá-la.

5. **Testes.** Objetivo: Verificar regras do inventário. Conclusão: testes independentes cobrindo inclusão, consulta e rejeição de dados inválidos.
