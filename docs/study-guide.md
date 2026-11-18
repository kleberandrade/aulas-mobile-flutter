# Guia de estudo

[Índice do curso](../README.pt-BR.md) · [Estudos de caso](case-studies.md) · [Livros e sites](books.md)

## Preparação do ambiente

Conhecimentos de lógica, funções, condições e repetição ajudam no acompanhamento. Comece com Dart antes das interfaces Flutter.

Use a [instalação oficial](https://docs.flutter.dev/install) para seu sistema e plataforma. Consulte a [trilha inicial](https://docs.flutter.dev/learn/pathway). Identifique seu ambiente com:

```sh
flutter --version
dart --version
flutter doctor -v
```

Esses comandos não instalam dependências deste índice. Resolva os requisitos da plataforma escolhida; aceites de licença e contas são decisões de quem prepara o ambiente.

Escolha um [estudo de caso](case-studies.md), abra seu repositório e siga o README atual. Confira `pubspec.yaml`, lockfile, comandos de teste e plataformas suportadas. Não rode `flutter pub get` nesta raiz. Não copie versões de tutoriais históricos por cima de um projeto já modernizado.

## Percurso

Siga os dez módulos do índice: Dart; formulários; layouts; APIs; dados locais; serviços; Firebase; IoT; arquitetura; trabalho final. Revise arquitetura durante as atividades, não apenas no fim. O [Masmorra ASCII](https://masmorra.io/) oferece um caminho paralelo para praticar Dart no terminal; veja as [leituras associadas](books.md).

Não há carga horária nem calendário oficial fixado neste repositório. O docente adapta as atividades e o uso de serviços/hardware à turma.

## Rotina de cada módulo

Leia os objetivos, execute um fluxo documentado do estudo de caso e registre o ambiente. Faça uma mudança pequena com dados sintéticos e verifique o resultado. Cada módulo termina com cinco exercícios; os critérios indicam evidências esperadas, não um gabarito ou correção automática.

Na entrega do seu próprio repositório, registre o que mudou, a justificativa, os testes executados e as limitações. Inclua capturas reais, nomes de autores e fontes. Não envie senhas, tokens, arquivos de conta de serviço ou dados pessoais.

## Critérios de conclusão

- Demonstrar o fluxo principal e pelo menos um caso inválido.
- Separar regras da interface e testar decisões relevantes.
- Explicar os estados de carregamento, erro e ausência de dados quando aplicáveis.
- Informar versões e passos reais para reproduzir a execução.
- Identificar fixtures, simulações, emuladores e integrações reais.

Um teste no navegador não comprova funcionamento de Bluetooth, câmera ou publicação em lojas. Os modos locais dos projetos modernizados não devem ser confundidos com integrações de produção. Use configuração e emuladores documentados para testar serviços externos.
