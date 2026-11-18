# 06 · Serviços externos e aprendizado de máquina

[Índice do curso](../../README.pt-BR.md) · [Guia de estudo](../../docs/study-guide.md)

## Pré-requisitos

Módulo 4; compreensão de operações assíncronas.

## Objetivos

Separar interface e integração; comunicar configuração, falhas e limites de previsões.

## Atividade orientadora

Execute o modo documentado de um estudo de caso e identifique o que é integração real, fixture e modo demonstrativo.

OCR/ML Kit permanece como tópico histórico sem tutorial vinculado neste curso. A presença de um classificador não comprova uso de um serviço ou modelo específico.

Use a versão atual do repositório escolhido, dados sintéticos e os passos de validação que ele documenta. Registre o ambiente e diferencie execução real, emulação e demonstração local. As atividades abaixo são propostas para o seu repositório de estudo.

## Leitura sugerida

[O Último Sprint da Humanidade](../../docs/books.md): discuta quem valida resultados e código produzidos com automação.

## Estudos de caso e referências

- [chatbot-aulas-flutter](https://github.com/kleberandrade/chatbot-aulas-flutter) — consulte o README e o código atuais.
- [teachable-ml-flutter](https://github.com/kleberandrade/teachable-ml-flutter) — consulte o README e o código atuais.
- [Livros e sites relacionados ao curso](../../docs/books.md).
- [Documentação oficial atual](../../docs/resources.md).
- [Catálogo e estado consultado dos projetos](../../docs/case-studies.md).

Créditos: curso de Kleber de Oliveira Andrade, Fatec Americana. Materiais externos conservam sua autoria e licença.

## Exercícios práticos

1. **Configuração.** Objetivo: Separar parâmetros públicos e segredos. Conclusão: execução de teste documentada sem credencial versionada.

2. **Adaptador.** Objetivo: Substituir o serviço por um double de teste. Conclusão: o fluxo de interface é testado sem chamada real.

3. **Falha externa.** Objetivo: Tratar indisponibilidade. Conclusão: informar a falha sem apresentar resposta simulada como real.

4. **Limites.** Objetivo: Explicar as saídas da integração. Conclusão: diferenciar resposta, confiança quando existente e casos fora do escopo.

5. **Evidência.** Objetivo: Registrar uma execução reproduzível. Conclusão: indicar entrada sintética, modo usado, resultado e limitações observadas.
