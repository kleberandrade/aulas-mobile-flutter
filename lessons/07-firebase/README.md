# 07 · Firebase e autenticação

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulos 4 e 5; separação de interfaces de dados.

## Objetivos

Compreender sessão, autorização, persistência remota e testes de regras de acesso.

## Atividade orientadora

Escolha um aplicativo e identifique o fluxo local e o fluxo Firebase documentados. Use emuladores quando configurados; contas de produção não são pré-requisito dos exercícios de interface.

Os métodos de login do índice de 2019–2020 são contexto histórico. Login por telefone, Google ou senha só deve ser apresentado como disponível quando a versão atual o implementar e documentar.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[A Guerra das Arquiteturas](../../docs/books.md): discuta limites entre identidade, regras de acesso e armazenamento.

## Estudos de caso e referências

- [lost-and-found-flutter](https://github.com/kleberandrade/lost-and-found-flutter) — consulte o README e o código atuais.
- [trampo-flutter](https://github.com/kleberandrade/trampo-flutter) — consulte o README e o código atuais.
- [adotai-flutter](https://github.com/kleberandrade/adotai-flutter) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Sessão.** Objetivo: Modelar entrada, saída e sessão expirada. Conclusão: testes cobrem os três estados com dados de teste.

2. **Autorização.** Objetivo: Definir quem pode editar um registro. Conclusão: teste de regra ou política nega acesso a outro usuário.

3. **Persistência.** Objetivo: Separar implementação local e remota. Conclusão: contrato comum e modo de execução identificado na interface ou documentação.

4. **Erro.** Objetivo: Tratar falha de gravação. Conclusão: informar o erro e evitar confirmação de sucesso prematura.

5. **Configuração.** Objetivo: Reproduzir o ambiente de teste. Conclusão: instruções sem segredos e evidência dos testes executados, distinguindo emulador de produção.
