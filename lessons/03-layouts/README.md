# 03 · Layouts e interação

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulos 1 e 2.

## Objetivos

Construir hierarquia visual, estados de interação e layouts adaptáveis. Manter a regra de negócio separada da apresentação.

## Atividade orientadora

Escolha um estudo de caso e revise seu fluxo em tela estreita, tela ampla e navegação por teclado.

Regras de jogo e operações matemáticas pertencem ao domínio. Mudanças visuais devem preservar os resultados existentes.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[A Ordem do Código Limpo](../../docs/books.md): relacione clareza da implementação às decisões de interação.

## Estudos de caso e referências

- [marcador-truco-aulas-flutter](https://github.com/kleberandrade/marcador-truco-aulas-flutter) — consulte o README e o código atuais.
- [calculadora-flutter](https://github.com/kleberandrade/calculadora-flutter) — consulte o README e o código atuais.
- [tic-tac-toe-flutter](https://github.com/kleberandrade/tic-tac-toe-flutter) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Responsividade.** Objetivo: Adaptar uma tela em duas larguras. Conclusão: nenhuma ação essencial inacessível ou conteúdo cortado.

2. **Semântica.** Objetivo: Identificar controles para tecnologias assistivas. Conclusão: ações possuem nomes úteis, não apenas ícones sem descrição.

3. **Foco.** Objetivo: Completar um fluxo por teclado. Conclusão: ordem de foco previsível e ativação visível.

4. **Estado.** Objetivo: Preservar uma partida ou cálculo ao alterar o layout. Conclusão: um teste demonstra que os dados permanecem.

5. **Feedback.** Objetivo: Comunicar uma ação inválida. Conclusão: mensagem compreensível e interface pronta para nova tentativa.
