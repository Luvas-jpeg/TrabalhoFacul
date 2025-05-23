# Sistema de Cursos Online - Projeto Integrado Multidisciplinar (PIM)

## Resumo Executivo
Este projeto consiste no desenvolvimento de uma plataforma de ensino a distância (EAD) desenvolvida como requisito do Projeto Integrado Multidisciplinar do primeiro semestre do curso de Análise e Desenvolvimento de Sistemas da Universidade Paulista (UNIP). O sistema implementa uma solução completa para gestão de cursos online, incorporando elementos de segurança, usabilidade e interatividade.

## Contextualização
O projeto foi desenvolvido visando integrar os conhecimentos adquiridos durante o primeiro semestre do curso, aplicando conceitos de programação, banco de dados, interface com usuário e segurança da informação em um contexto prático e real.

## Objetivos
1. Desenvolver uma plataforma de ensino a distância funcional e escalável
2. Implementar sistema de autenticação seguro com validação de credenciais
3. Criar interface gráfica responsiva e intuitiva
4. Estabelecer sistema de avaliação e acompanhamento do progresso discente
5. Implementar mecanismos de persistência de dados
6. Integrar recursos multimídia para enriquecimento do conteúdo

## Metodologia
O desenvolvimento do projeto seguiu uma abordagem estruturada, utilizando:
- Metodologia ágil para gestão do projeto
- Versionamento de código com Git
- Desenvolvimento iterativo e incremental
- Testes contínuos de funcionalidade
- Documentação sistemática do processo

## Tecnologias Implementadas
### Backend
- Python 3.x como linguagem principal
- JSON para persistência de dados
- Expressões regulares para validação de entrada
- Datetime para gerenciamento temporal

### Frontend
- Streamlit para interface web responsiva
- CSS para estilização e layout
- Integração com API do YouTube para conteúdo audiovisual

### Segurança
- Validação de senha forte
- Armazenamento seguro de credenciais
- Controle de sessão de usuário
- Registro de atividades

## Funcionalidades Implementadas
1. **Sistema de Autenticação**
   - Registro de novos usuários
   - Login com validação de credenciais
   - Recuperação de sessão

2. **Gestão de Cursos**
   - Catálogo de cursos disponíveis
   - Integração com conteúdo audiovisual
   - Sistema de avaliação com feedback imediato

3. **Acompanhamento de Progresso**
   - Histórico de acessos
   - Registro de conclusão de cursos
   - Certificação de conclusão

4. **Interface do Usuário**
   - Design responsivo
   - Navegação intuitiva
   - Feedback visual de ações

## Estrutura do Projeto
```
trabalhofacul/
├── programa/
│   └── PIM-1S.py          # Código fonte principal
├── data/
│   └── usuarios.json      # Armazenamento de dados
├── stylesheet/
│   └── style.css          # Estilização da interface
└── README.md              # Documentação do projeto
```

## Requisitos do Sistema
### Requisitos Funcionais
- Sistema de autenticação completo
- Gestão de cursos e conteúdo
- Sistema de avaliação
- Geração de certificados
- Registro de progresso

### Requisitos Não-Funcionais
- Interface responsiva
- Segurança na autenticação
- Persistência de dados
- Performance adequada
- Usabilidade intuitiva

## Instalação e Execução
1. Clone o repositório
```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Execute o projeto
```bash
streamlit run programa/PIM-1S.py
```

## Equipe de Desenvolvimento
- Lucas Vinícios Martins Alves - R6602G9
- Arthur Lucio Parmezan - H70FDH6
- Luis Otávio Freitas Faria - R8651C0
- Luan Alves Magalhães - H659IA0
- Vinicius Cristiano Carmin - H5872C4
- David Rodrigues Vilchiez - R866238

## Considerações sobre o Desenvolvimento
O projeto foi desenvolvido com suporte de ferramentas de Inteligência Artificial, utilizadas principalmente para:
- Otimização de código
- Sugestão de implementações
- Resolução de problemas técnicos
- Documentação

A equipe manteve o controle total sobre as decisões de desenvolvimento e arquitetura, utilizando a IA como ferramenta de suporte ao processo de desenvolvimento.

## Conclusão
O projeto demonstra a aplicação prática dos conhecimentos adquiridos no primeiro semestre do curso, resultando em uma solução completa e funcional para ensino a distância. A implementação bem-sucedida das funcionalidades planejadas e a integração das diferentes tecnologias utilizadas comprovam a eficácia da abordagem adotada.

## Considerações Finais
O desenvolvimento deste projeto proporcionou uma valiosa oportunidade de aplicação prática dos conhecimentos teóricos adquiridos durante o primeiro semestre do curso. A integração de diferentes disciplinas, como programação, banco de dados e interface com usuário, permitiu a criação de uma solução robusta e funcional.

Os principais desafios enfrentados incluíram:
- Implementação de um sistema de autenticação seguro
- Desenvolvimento de uma interface intuitiva e responsiva
- Integração eficiente com recursos externos
- Garantia de persistência e integridade dos dados

As soluções desenvolvidas demonstraram a viabilidade de criar uma plataforma de ensino a distância com recursos modernos e uma experiência de usuário satisfatória.

## Créditos dos Cursos
Os conteúdos dos cursos foram desenvolvidos com base em materiais educacionais de alta qualidade disponíveis na plataforma YouTube:

### Introdução à Informática
- Canal: Certificados Cursos Online
- Playlist: "Curso de Informática Básica"
- Link: https://www.youtube.com/watch?v=9fNHAD7ZDL4&list=PL-QAz5R5Rlm7wn20xLTIr84gbS2XkzqEZ

### Cybersegurança
- Canal: Curso em Vídeo
- Playlist: "Curso de Segurança da Informação"
- Link: https://www.youtube.com/watch?v=KvPtIl-Gz2E&list=PLHz_AreHm4dlaTyjolzCFC6IjLzO8O0XV

### Lógica de Programação em Python
- Canal: Joviano Silveira
- Playlist: "Curso de Python"
- Link: https://www.youtube.com/watch?v=pv1XzosXVQc&list=PLQpSyz5rZmJpFVb1TidOflNMcVnpDdzAn

### Fake News e Desinformação
- Material: Atividade de Extensão - Combate à Desinformação
- Fonte: Material didático da UNIP
- Arquivo: Atividade de extenção - Combate a desinformação (2).pdf

## Referências
### Bibliografia
1. SILVA, Maurício Samy. HTML5: A Linguagem de Marcação que Revolucionou a Web. 2. ed. São Paulo: Novatec, 2014.
2. SOMMERVILLE, Ian. Engenharia de Software. 9. ed. São Paulo: Pearson, 2011.
3. TANENBAUM, Andrew S. Sistemas Operacionais Modernos. 4. ed. São Paulo: Pearson, 2016.

### Documentação Técnica
1. Python Software Foundation. Python Documentation. Disponível em: https://docs.python.org/
2. Streamlit. Streamlit Documentation. Disponível em: https://docs.streamlit.io/
3. JSON. JSON Documentation. Disponível em: https://www.json.org/

### Ferramentas e Frameworks
1. Visual Studio Code - Editor de código
2. Git - Sistema de controle de versão
3. GitHub - Plataforma de hospedagem de código
4. Streamlit - Framework para desenvolvimento web
5. Plotly - Biblioteca para visualização de dados

## Licença
Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).

## Contato
Para informações adicionais ou sugestões, entre em contato com a equipe de desenvolvimento através dos canais institucionais da UNIP.
