# 📚 Sistema de Gestão de Biblioteca

Este repositório contém a modelagem e especificação do **Sistema de Gestão de Biblioteca**, mapeado a partir de uma sessão de *Event Storming* realizada em conjunto com especialistas do domínio (bibliotecários e atendentes).

---

## 🌐 Contexto de Domínio
A biblioteca tem como objetivo permitir que usuários consultem o acervo, realizem empréstimos e devoluções de livros. Os processos descritos abaixo refletem as operações reais, regras de negócio cruciais e os principais acontecimentos necessários para o funcionamento correto e eficiente da biblioteca.

### 🎯 Objetivo do Sistema
Garantir o controle preciso sobre o acervo de livros, fluxo de usuários e ciclos de empréstimos, assegurando o cumprimento rigoroso das regras de negócio e facilitando o acesso dos leitores aos materiais.

---

## 🔄 Fluxos de Trabalho (Processos)

### 📖 1. Cadastro e Organização do Acervo
* **Operações de Equipe:** Permite cadastrar novos títulos, atualizar informações cadastrais e remover livros obsoletos ou danificados do acervo.
* **Consulta:** Usuários podem realizar buscas flexíveis no catálogo por título, autor ou categoria.

### 🔑 2. Empréstimo de Livros
Ao solicitar um empréstimo, o sistema realiza uma validação multifator antes da liberação:
* [x] O usuário precisa estar devidamente cadastrado.
* [x] O usuário deve estar com a situação **Ativa** (não bloqueado).
* [x] Não pode haver registros de empréstimos atrasados no perfil do usuário.
* [x] Deve respeitar o limite máximo de livros permitidos em posse simultânea.
* [x] O livro solicitado deve estar com o status **Disponível**.

> **Nota:** Uma vez aprovado, o sistema registra a retirada e calcula a data prevista para a devolução.

### ↩️ 3. Devolução de Livros
No ato da devolução do material, o sistema avalia:
* **Prazo:** Se o livro retornou dentro da data prevista ou se houve atraso.
* **Penalidades:** Em caso de atraso, é gerada uma multa automática.
* **Restrições:** Enquanto houver pendências financeiras ou cadastrais, o usuário fica temporariamente impedido de realizar novos empréstimos.

### ⏳ 4. Reserva de Livros
* Quando um livro desejado já está emprestado, o usuário pode solicitar uma reserva.
* O sistema gerencia uma fila de espera ordenada por ordem de pedido.
* Assim que o livro retorna ao acervo, o próximo usuário da fila é notificado para efetivar o empréstimo.

---

## 👥 Perfis de Usuários
Os usuários da biblioteca possuem um histórico completo de suas interações e podem transicionar entre três estados principais:
* 🟢 **Ativo:** Liberado para utilizar todos os serviços.
* 🔴 **Bloqueado:** Impedido de realizar novas ações por violação de regras.
* 🟡 **Com pendências:** Possui alguma irregularidade (ex: multa ou atraso) que restringe novos empréstimos até a regularização.

---

## 🛠️ Regras de Negócio (Policies)
1. Um usuário só pode pegar livros emprestados se estiver com o status **Ativo**.
2. Um usuário **Bloqueado** não pode realizar empréstimos em nenhuma circunstância.
3. Existe um teto (quantidade máxima) de livros que cada usuário pode manter emprestado ao mesmo tempo.
4. Livros com o status "Emprestado" ficam indisponíveis para novos empréstimos até que retornem.
5. Um livro com reservas ativas deve rigorosamente respeitar a ordem da fila de espera.
6. Devoluções após a data de vencimento geram multas de forma automática.
7. Usuários inadimplentes (com multas ou pendências em aberto) têm o direito de novos empréstimos bloqueado.

---

## ⚡ Eventos de Negócio (Domain Events)
Os seguintes eventos foram identificados durante o *Event Storming* e representam fatos imutáveis que ocorreram no sistema:

### Gerenciamento de Usuários
* `UsuarioCadastrado`
* `UsuarioBloqueado`
* `UsuarioDesbloqueado`

### Gerenciamento do Acervo
* `LivroCadastrado`
* `LivroDisponibilizado`

### Ciclo de Empréstimos e Devoluções
* `EmprestimoSolicitado`
* `EmprestimoAprovado`
* `LivroEmprestado`
* `LivroDevolvido`

### Penalidades
* `AtrasoIdentificado`
* `MultaGerada`

### Fluxo de Reservas
* `ReservaCriada`
* `ReservaAtendida`
* `ReservaCancelada`
