# Flutter Mobile Development · Course Hub

[![Documentation checks](https://github.com/kleberandrade/aulas-mobile-flutter/actions/workflows/docs.yml/badge.svg)](https://github.com/kleberandrade/aulas-mobile-flutter/actions/workflows/docs.yml)
![Material: lessons](https://img.shields.io/badge/material-lessons-02569B)
![Topics: Dart and Flutter](https://img.shields.io/badge/topics-Dart%20%26%20Flutter-0175C2)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[Português brasileiro](README.pt-BR.md) · [Study guide](docs/study-guide.md) · [Books and learning sites](docs/books.md) · [Current case studies](docs/case-studies.md)

Course hub for mobile development taught by **Prof. Kleber de Oliveira Andrade** at **Fatec Americana**, in the Systems Analysis and Development program. The course guides retain the original Portuguese teaching language; this page provides an English overview.

This repository contains lessons, study plans and references. Application code and execution instructions live in the individual case-study repositories.

## Learning path

Each module provides objectives, prerequisites, a suggested activity, references and exactly five practical exercises with completion criteria.

1. [Fundamentos de Dart e orientação a objetos](lessons/01-dart/README.md)
2. [Formulários e validação](lessons/02-forms/README.md)
3. [Layouts e interação](lessons/03-layouts/README.md)
4. [APIs HTTP e estado assíncrono](lessons/04-apis/README.md)
5. [Persistência local](lessons/05-local-data/README.md)
6. [Serviços externos e aprendizado de máquina](lessons/06-services/README.md)
7. [Firebase e autenticação](lessons/07-firebase/README.md)
8. [Internet das Coisas](lessons/08-iot/README.md)
9. [Arquitetura e manutenção](lessons/09-architecture/README.md)
10. [Aplicações completas e trabalho final](lessons/10-final-project/README.md)

## Start here

Follow the [study guide](docs/study-guide.md), then open the [current application repository](docs/case-studies.md) for the selected case study. Use its current README, SDK constraints and checks: several repositories have been modernized since the original articles were written.

There is no Flutter application or `pubspec.yaml` in this hub. Module activities are learning proposals, not claims that every exercise is already implemented in a linked app.

## Books, sites and references

- [Masmorra ASCII](https://masmorra.io/): a companion path for learning Dart through a terminal roguelike.
- [Books and learning sites by Kleber Andrade](docs/books.md): suggested readings mapped to course topics.
- [Official Dart, Flutter and integration resources](docs/resources.md).
- [Current case studies and repository snapshot](docs/case-studies.md).
- [Original 2019–2020 index and article links](docs/history/README-2019-2020.md), preserved as historical material.

The original article titles are not proof of the libraries, authentication methods or platforms currently used. Follow the updated repositories first and compare older articles with their current implementation.

## Maintaining the course

Run `python3 tools/check_docs.py` from this directory. The dependency-free documentation check validates local Markdown links and anchors, the ten-module sequence and exercise structure. GitHub Actions runs the same check; it does not compile linked apps or grade students' solutions.

See [Contributing](CONTRIBUTING.md) and [Changelog](CHANGELOG.md). Course by **Kleber de Oliveira Andrade**, **Faculdade de Tecnologia de Americana**. The original [MIT license](LICENSE) is preserved. External books, articles, images and applications retain their own authorship and terms.
