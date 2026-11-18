# 05 · Persistência local

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulos 1 a 4.

## Objetivos

Persistir dados, reconstruir estado após reiniciar e tratar evolução do formato armazenado.

## Atividade orientadora

Cadastre um registro, encerre e reabra o aplicativo. Documente o mecanismo de armazenamento realmente usado pela versão atual.

SQLite, Sembast e Hive aparecem nos títulos históricos. O README e o código atuais determinam o mecanismo em uso e a compatibilidade de plataforma.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[Masmorra ASCII e Agência Holística](../../docs/books.md): compare persistência e investigação de falhas com o aplicativo escolhido.

[Agência Holística · Volume II — Tudo Tem Memória](https://kleberandrade.dev/books/agencia-vol-2): Compare o estado exibido com o estado armazenado e registre como detectar uma inconsistência.

[Agência Holística · Volume III — A Conta Que Ficou](https://kleberandrade.dev/books/agencia-vol-3): Relacione a leitura a um teste de restauração: recupere uma amostra e confira seus dados, além da existência do arquivo.

## Estudos de caso e referências

- [todo-list-aulas-flutter](https://github.com/kleberandrade/todo-list-aulas-flutter) — consulte o README e o código atuais.
- [borrowed-stuff-flutter](https://github.com/kleberandrade/borrowed-stuff-flutter) — consulte o README e o código atuais.
- [my-money-fluter](https://github.com/kleberandrade/my-money-fluter) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).
- [Masmorra ASCII](https://masmorra.io/): fundamentos em Dart, persistência e organização de um jogo no terminal.

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Reabertura.** Objetivo: Preservar um registro entre sessões. Conclusão: demonstrar criação, reinício e leitura do mesmo conteúdo.

2. **Atualização.** Objetivo: Editar e excluir um registro. Conclusão: mudanças continuam corretas após reabrir.

3. **Formato.** Objetivo: Definir o comportamento para dados armazenados inválidos. Conclusão: teste reproduz o caso e evita perda silenciosa.

4. **Evolução.** Objetivo: Modificar o esquema com estratégia explícita. Conclusão: uma amostra do formato anterior continua legível ou recebe migração testada.

5. **Isolamento.** Objetivo: Testar o repositório com armazenamento temporário. Conclusão: duas execuções não compartilham dados acidentalmente.
