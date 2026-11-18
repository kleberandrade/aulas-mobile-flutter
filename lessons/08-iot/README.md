# 08 · Internet das Coisas

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulo 4; noções de mensagens e conexão.

## Objetivos

Entender protocolos, serialização, estado de conexão e limites entre simulação e hardware.

## Atividade orientadora

Explore um fluxo MQTT ou Bluetooth documentado. Comece com transporte simulado; teste hardware apenas com os requisitos específicos atendidos.

Bluetooth e Arduino exigem plataforma e equipamento compatíveis. O tópico Twilio/SMS do programa antigo não possui tutorial vinculado aqui e não autoriza disparos de mensagens.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[A Guerra das Arquiteturas](../../docs/books.md): discuta responsabilidades entre aplicativo, transporte e dispositivo.

## Estudos de caso e referências

- [mqtt_aulas_flutter](https://github.com/kleberandrade/mqtt_aulas_flutter) — consulte o README e o código atuais.
- [controlled-robot-arduino](https://github.com/kleberandrade/controlled-robot-arduino) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Mensagem.** Objetivo: Definir um contrato de comando. Conclusão: documentar unidade, intervalo e rejeição de mensagens inválidas.

2. **Conexão.** Objetivo: Representar desconexão e reconexão. Conclusão: teste demonstra transições sem indicar conexão inexistente.

3. **Simulação.** Objetivo: Substituir o transporte. Conclusão: executar um comando em teste sem hardware e rotular esse modo.

4. **Limites.** Objetivo: Tratar comandos fora de intervalo ou sem autorização. Conclusão: teste comprova a rejeição na fronteira correspondente.

5. **Plataforma.** Objetivo: Documentar uma execução. Conclusão: listar equipamento, sistema e protocolo efetivamente testados, sem generalizar um teste web para rádio real.
