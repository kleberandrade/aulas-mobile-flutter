# 04 · APIs HTTP e estado assíncrono

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulos 1 a 3; Future e async/await.

## Objetivos

Consumir dados externos, converter JSON na fronteira e distinguir carregamento, vazio, sucesso e erro.

## Atividade orientadora

Escolha uma consulta e implemente uma resposta de erro reproduzível. Use cliente substituível nos testes, sem depender de rede externa.

A implementação atual do aplicativo define a API e as bibliotecas utilizadas. Não presuma que DIO ou Google Sheets continuam sendo a integração ativa apenas pelo título de um artigo antigo.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[A Agência Holística de Depuração](../../docs/books.md): use a leitura como ponto de partida para investigar falhas de integração.

[Agência Holística · Volume II — Tudo Tem Memória](https://kleberandrade.dev/books/agencia-vol-2): Use a leitura para investigar uma falha de integração com logs e uma sequência reproduzível.

[Agência Holística · Volume III — A Conta Que Ficou](https://kleberandrade.dev/books/agencia-vol-3): Discuta tentativas repetidas e idempotência: um teste com cliente simulado deve verificar se a repetição duplica um efeito.

## Estudos de caso e referências

- [search-cep-aulas-flutter](https://github.com/kleberandrade/search-cep-aulas-flutter) — consulte o README e o código atuais.
- [quiz-covid19-flutter](https://github.com/kleberandrade/quiz-covid19-flutter) — consulte o README e o código atuais.
- [movies-flutter](https://github.com/kleberandrade/movies-flutter) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Estados.** Objetivo: Representar carregamento, vazio e resultado. Conclusão: cada estado pode ser demonstrado com dados controlados.

2. **Parsing.** Objetivo: Validar uma resposta inesperada. Conclusão: JSON inválido ou campo ausente produz erro tratado.

3. **Falhas.** Objetivo: Tratar timeout ou indisponibilidade. Conclusão: exibir mensagem e permitir nova tentativa sem dados de sucesso inventados.

4. **Concorrência.** Objetivo: Impedir resultado antigo de substituir a consulta mais recente. Conclusão: teste controla a ordem das duas respostas.

5. **Contrato.** Objetivo: Documentar uma consulta. Conclusão: descrever entrada, saída, limites e executar testes com fixtures sintéticas.
