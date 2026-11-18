# 09 · Arquitetura e manutenção

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulos 1 a 5; um estudo de caso já executado.

## Objetivos

Delimitar domínio, interface e infraestrutura; escolher abstrações pela necessidade do comportamento.

## Atividade orientadora

Use um aplicativo dos módulos anteriores para isolar uma regra da interface. Compare com um padrão de projeto apenas quando o problema justificar.

O Grimório dos Padrões oferece exemplos em TypeScript: use-os para estudar conceitos e implemente sua atividade em Dart. MVC, MVVM, MVP e Clean Architecture são alternativas de estudo, não módulos de código garantidos neste índice.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[O Grimório dos Padrões, Fantasia Técnica e Masmorra ASCII](../../docs/books.md): compare conceitos e aplique apenas os necessários ao caso.

## Estudos de caso e referências

- [o-grimorio-dos-padroes](https://github.com/kleberandrade/o-grimorio-dos-padroes) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).
- [Masmorra ASCII](https://masmorra.io/): fundamentos em Dart, persistência e organização de um jogo no terminal.

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Responsabilidades.** Objetivo: Desenhar o mapa de dependências do caso escolhido. Conclusão: explicar quais módulos conhecem interface, domínio e armazenamento.

2. **Regra.** Objetivo: Isolar uma decisão de negócio. Conclusão: testes chamam a regra sem framework de UI.

3. **Infraestrutura.** Objetivo: Substituir um acesso a dados por contrato. Conclusão: teste usa implementação alternativa sem mudar a regra.

4. **Refatoração.** Objetivo: Melhorar a estrutura preservando comportamento. Conclusão: demonstrar testes antes e depois e justificar a redução de complexidade.

5. **Decisão.** Objetivo: Registrar uma escolha arquitetural. Conclusão: comparar uma alternativa e explicitar contexto, consequência e limite da decisão.
