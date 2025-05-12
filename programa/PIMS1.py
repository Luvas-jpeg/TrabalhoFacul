import streamlit as st
import json
import os
import webbrowser
from datetime import datetime
import re

# Carregar o arquivo CSS
def load_css():
    with open("stylesheet/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Configuração da página
st.set_page_config(
    page_title="Sistema de Cursos Online",
    page_icon="📚",
    layout="centered"
)

# Carregar CSS
load_css()

# Criar pasta data se não existir
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Arquivo para armazenar dados dos usuários
USERS_FILE = os.path.join(DATA_DIR, "usuarios.json")

# Inicializar arquivo de usuários se não existir
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w", encoding='utf-8') as f:
        json.dump({}, f, ensure_ascii=False, indent=4)

# Função para carregar usuários
def carregar_usuarios():
    try:
        with open(USERS_FILE, "r", encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

# Função para salvar usuários
def salvar_usuarios(usuarios):
    with open(USERS_FILE, "w", encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

# Função para registrar acesso
def registrar_acesso(username):
    usuarios = carregar_usuarios()
    if username in usuarios:
        if "acessos" not in usuarios[username]:
            usuarios[username]["acessos"] = 0
        usuarios[username]["acessos"] += 1
        usuarios[username]["ultimo_acesso"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        salvar_usuarios(usuarios)

# Função para validar senha forte
def validar_senha_forte(senha):
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"
    
    if not re.search(r'[A-Z]', senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula"
    
    if not re.search(r'[a-z]', senha):
        return False, "A senha deve conter pelo menos uma letra minúscula"
    
    if not re.search(r'[0-9]', senha):
        return False, "A senha deve conter pelo menos um número"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False, "A senha deve conter pelo menos um caractere especial (!@#$%^&*(),.?\":{}|<>)"
    
    return True, "Senha válida"

# Informações dos cursos
cursos = {
    "Introdução à Informática": {
        "video": "https://www.youtube.com/watch?v=HhqE8wzJWdw",
        "perguntas": [
            {
                "pergunta": "O que é um sistema operacional?",
                "opcoes": ["Um programa para editar textos", "Um software que gerencia os recursos do computador", "Um dispositivo de hardware", "Um tipo de vírus"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual destes é um dispositivo de entrada?",
                "opcoes": ["Monitor", "Impressora", "Teclado", "Caixa de som"],
                "resposta_correta": 2
            },
            {
                "pergunta": "O que significa a sigla CPU?",
                "opcoes": ["Central Processing Unit", "Computer Personal Unit", "Control Processing Unit", "Central Personal Unit"],
                "resposta_correta": 0
            },
            {
                "pergunta": "Qual é a função principal da memória RAM?",
                "opcoes": ["Armazenar dados permanentemente", "Processar informações", "Armazenar dados temporariamente durante o uso", "Conectar o computador à internet"],
                "resposta_correta": 2
            },
            {
                "pergunta": "O que é um arquivo PDF?",
                "opcoes": ["Um tipo de vírus", "Um formato de documento portátil", "Um programa de edição de imagens", "Um sistema operacional"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual destes é um exemplo de software?",
                "opcoes": ["Mouse", "Teclado", "Microsoft Word", "Impressora"],
                "resposta_correta": 2
            },
            {
                "pergunta": "O que é um navegador web?",
                "opcoes": ["Um dispositivo para conectar à internet", "Um programa para acessar páginas na internet", "Um tipo de vírus", "Um sistema operacional"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual é a função principal de um antivírus?",
                "opcoes": ["Acelerar a conexão com a internet", "Proteger o computador contra ameaças digitais", "Editar documentos", "Armazenar arquivos"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é um backup?",
                "opcoes": ["Um tipo de vírus", "Uma cópia de segurança dos dados", "Um programa de edição de imagens", "Um dispositivo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual destes é um exemplo de hardware?",
                "opcoes": ["Windows", "Microsoft Word", "Mouse", "Internet Explorer"],
                "resposta_correta": 2
            }
        ]
    },
    "Cybersegurança": {
        "video": "https://www.youtube.com/playlist?list=PLHz_AreHm4dlaTyjolzCFC6IjLzO8O0XV",
        "perguntas": [
            {
                "pergunta": "Qual é a principal finalidade da segurança da informação no contexto de ambientes digitais?",
                "opcoes": [
                    "Proporcionar anonimato absoluto durante a navegação na internet.",
                    "Minimizar os impactos de falhas técnicas por meio de redundância operacional.",
                    "Estabelecer uma estrutura de proteção que assegure os ativos informacionais quanto à confidencialidade, integridade e disponibilidade.",
                    "Viabilizar o uso de recursos computacionais com desempenho e acessibilidade otimizados."
                ],
                "resposta_correta": 2
            },
            {
                "pergunta": "No arcabouço da segurança da informação, os pilares de confidencialidade, integridade e disponibilidade são conhecidos como:",
                "opcoes": [
                    "Princípios de consistência algorítmica.",
                    "Elementos centrais do gerenciamento de riscos de TI.",
                    "Fundamentos da tríade CIA, que norteia as boas práticas de proteção de dados.",
                    "Componentes da arquitetura lógica de segurança em redes públicas."
                ],
                "resposta_correta": 2
            },
            {
                "pergunta": "No contexto da proteção de dados, a criptografia assimétrica difere da simétrica porque:",
                "opcoes": [
                    "Permite a autenticação mútua entre as partes através de tokens digitais temporários.",
                    "Utiliza uma chave pública para criptografar e uma chave privada correspondente para descriptografar, assegurando comunicação segura.",
                    "Garante maior velocidade de transmissão em conexões peer-to-peer.",
                    "Reduz a necessidade de troca de chaves criptográficas entre os interlocutores."
                ],
                "resposta_correta": 1
            },
            {
                "pergunta": "Em relação à criação de credenciais seguras, qual prática representa uma abordagem resiliente contra ataques de força bruta?",
                "opcoes": [
                    "Adotar expressões memorizáveis com substituições visuais (ex: \"S3gur@!\").",
                    "Manter um padrão de senhas similar em múltiplos serviços para facilitar a memorização.",
                    "Empregar geradores de senhas baseados em padrões predefinidos e previsíveis.",
                    "Construir senhas longas com entropia elevada, evitando reutilização e aplicando critérios alfanuméricos e simbólicos."
                ],
                "resposta_correta": 3
            },
            {
                "pergunta": "A engenharia social, dentro do escopo das ameaças cibernéticas, pode ser caracterizada como:",
                "opcoes": [
                    "Um processo técnico que explora vulnerabilidades em protocolos criptográficos.",
                    "Uma forma de coleta automatizada de dados a partir de sistemas expostos na rede.",
                    "Uma tática de persuasão que visa explorar fragilidades humanas para induzir ao fornecimento de informações sensíveis.",
                    "Uma metodologia de segmentação de perfis com base em análise de comportamento digital."
                ],
                "resposta_correta": 2
            },
            {
                "pergunta": "Assinale a alternativa que melhor descreve a funcionalidade de softwares maliciosos (malwares):",
                "opcoes": [
                    "Aplicações legítimas modificadas para rastrear o comportamento do usuário para fins comerciais.",
                    "Conjuntos de rotinas implementadas com a intenção deliberada de comprometer a segurança, a integridade ou a confidencialidade dos sistemas afetados.",
                    "Ferramentas utilizadas exclusivamente por cibercriminosos para fins de espionagem estatal.",
                    "Extensões de navegadores que interferem no desempenho do sistema operacional."
                ],
                "resposta_correta": 1
            },
            {
                "pergunta": "O ataque conhecido como phishing geralmente se vale de quais estratégias para capturar dados sensíveis?",
                "opcoes": [
                    "Manipulação de variáveis ambientais em dispositivos IoT.",
                    "Distribuição de malwares embutidos em bibliotecas de código aberto.",
                    "Comunicação fraudulenta, geralmente por e-mail ou mensagens, que simula instituições legítimas com o objetivo de obter credenciais ou dados pessoais.",
                    "Criação de sites espelho que operam em protocolos criptográficos inválidos."
                ],
                "resposta_correta": 2
            },
            {
                "pergunta": "A manutenção da integridade e segurança de sistemas operacionais é fortemente dependente de:",
                "opcoes": [
                    "Recompilação do kernel e desativação de serviços de rede pouco utilizados.",
                    "Análise contínua de logs de acesso e políticas de conformidade.",
                    "Instalação regular de atualizações e correções de segurança fornecidas pelo fabricante.",
                    "Criação de imagens de disco para recuperação em caso de falha física."
                ],
                "resposta_correta": 2
            },
            {
                "pergunta": "Uma medida fundamental para assegurar a proteção de redes domésticas sem fio consiste em:",
                "opcoes": [
                    "Alterar o SSID para um nome genérico, reduzindo a exposição de informações pessoais.",
                    "Ativar o filtro de endereços MAC para impedir a conexão de dispositivos não autorizados.",
                    "Utilizar criptografia WPA2 ou WPA3 e senhas com alta complexidade, além de configurar o roteador com parâmetros de segurança atualizados.",
                    "Desabilitar o DHCP para limitar a atribuição automática de IPs."
                ],
                "resposta_correta": 2
            },
            {
                "pergunta": "A autenticação multifatorial (MFA) é um mecanismo de segurança que:",
                "opcoes": [
                    "Emprega biometria como única forma de identificação do usuário.",
                    "Introduz múltiplos estágios de autenticação baseados exclusivamente em senhas sequenciais.",
                    "Combina elementos distintos (conhecimento, posse, herança) para garantir robustez contra acessos indevidos.",
                    "Se aplica apenas em ambientes corporativos com sistemas legados."
                ],
                "resposta_correta": 2
            }
        ]
    },
    "Lógica de Programação em Python": {
        "video": "https://www.youtube.com/watch?v=nIHq1MtJaKs",
        "perguntas": [
            {
                "pergunta": "O que é uma variável em Python?",
                "opcoes": ["Um tipo de vírus", "Um local para armazenar dados", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é um loop em programação?",
                "opcoes": ["Um tipo de vírus", "Uma estrutura que repete um bloco de código", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é uma função em Python?",
                "opcoes": ["Um tipo de vírus", "Um bloco de código reutilizável", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é uma condicional em Python?",
                "opcoes": ["Um tipo de vírus", "Uma estrutura que executa código baseado em condições", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é uma lista em Python?",
                "opcoes": ["Um tipo de vírus", "Uma estrutura de dados ordenada", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é um dicionário em Python?",
                "opcoes": ["Um tipo de vírus", "Uma estrutura de dados com chave-valor", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é um módulo em Python?",
                "opcoes": ["Um tipo de vírus", "Um arquivo contendo código Python reutilizável", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é uma exceção em Python?",
                "opcoes": ["Um tipo de vírus", "Um erro que ocorre durante a execução do programa", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é um método em Python?",
                "opcoes": ["Um tipo de vírus", "Uma função associada a um objeto", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            },
            {
                "pergunta": "O que é uma classe em Python?",
                "opcoes": ["Um tipo de vírus", "Um modelo para criar objetos", "Um programa antivírus", "Um tipo de hardware"],
                "resposta_correta": 1
            }
        ]
    }
}

# Função principal
def main():
    # Inicializar estado da sessão
    if 'logado' not in st.session_state:
        st.session_state.logado = False
        st.session_state.usuario_atual = None
        st.session_state.pagina = "login"
        st.session_state.curso_atual = None
        st.session_state.respostas = []
        st.session_state.pontuacao = 0

    # Página de login/cadastro
    if st.session_state.pagina == "login":
        mostrar_login()
    # Página de seleção de cursos
    elif st.session_state.pagina == "cursos":
        mostrar_cursos()
    # Página do curso
    elif st.session_state.pagina == "curso":
        mostrar_curso()
    # Página de atividades
    elif st.session_state.pagina == "atividades":
        mostrar_atividades()
    # Página de resultado
    elif st.session_state.pagina == "resultado":
        mostrar_resultado()
    # Página de conclusão
    elif st.session_state.pagina == "conclusao":
        mostrar_conclusao()

# Função para mostrar a página de login/cadastro
def mostrar_login():
    st.title("Sistema de Cursos Online")
    
    tab1, tab2 = st.tabs(["Login", "Cadastro"])
    
    with tab1:
        st.subheader("Login")
        username = st.text_input("Nome de usuário", key="login_username")
        password = st.text_input("Senha", type="password", key="login_password")
        
        if st.button("Entrar"):
            if not username or not password:
                st.error("Por favor, preencha todos os campos.")
            else:
                usuarios = carregar_usuarios()
                if username in usuarios and usuarios[username]["senha"] == password:
                    st.session_state.logado = True
                    st.session_state.usuario_atual = username
                    st.session_state.pagina = "cursos"
                    registrar_acesso(username)
                    st.success(f"Boas Vindas, {username}!")
                    st.rerun()
                else:
                    st.error("Nome de usuário ou senha incorretos.")
    
    with tab2:
        st.subheader("Cadastro")
        new_username = st.text_input("Nome de usuário", key="cadastro_username")
        new_password = st.text_input("Senha", type="password", key="cadastro_password")
        confirm_password = st.text_input("Confirmar senha", type="password", key="confirm_password")
        
        # Adicionar informações sobre os requisitos da senha
        st.markdown("""
        **Requisitos da senha:**
        - Mínimo de 8 caracteres
        - Pelo menos uma letra maiúscula
        - Pelo menos uma letra minúscula
        - Pelo menos um número
        - Pelo menos um caractere especial (!@#$%^&*(),.?\":{}|<>)"
        """)
        
        if st.button("Cadastrar"):
            if not new_username or not new_password or not confirm_password:
                st.error("Por favor, preencha todos os campos.")
            elif new_password != confirm_password:
                st.error("As senhas não coincidem.")
            else:
                # Validar força da senha
                senha_valida, mensagem = validar_senha_forte(new_password)
                if not senha_valida:
                    st.error(mensagem)
                else:
                    usuarios = carregar_usuarios()
                    if new_username in usuarios:
                        st.error("Este nome de usuário já está em uso.")
                    else:
                        usuarios[new_username] = {
                            "senha": new_password,
                            "cursos_concluidos": [],
                            "notas": {},
                            "acessos": 0,
                            "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        }
                        salvar_usuarios(usuarios)
                        st.success("Cadastro realizado com sucesso! Faça login para continuar.")

# Função para mostrar a página de seleção de cursos
def mostrar_cursos():
    if not st.session_state.logado:
        st.session_state.pagina = "login"
        st.rerun()
        return
    
    usuarios = carregar_usuarios()
    cursos_concluidos = usuarios[st.session_state.usuario_atual]["cursos_concluidos"]
    
    st.title(f"Boas Vindas, {st.session_state.usuario_atual}!")
    st.subheader("Escolha um curso para começar:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        curso = "Introdução à Informática"
        concluido = curso in cursos_concluidos
        st.write(f"### {curso}")
        if concluido:
            st.success("✅ Concluído")
            nota = usuarios[st.session_state.usuario_atual]["notas"].get(curso, "N/A")
            st.write(f"Nota anterior: {nota}/10")
        if st.button("Selecionar", key=curso):
            st.session_state.curso_atual = curso
            st.session_state.pagina = "curso"
            st.rerun()
    
    with col2:
        curso = "Cybersegurança"
        concluido = curso in cursos_concluidos
        st.write(f"### {curso}")
        if concluido:
            st.success("✅ Concluído")
            nota = usuarios[st.session_state.usuario_atual]["notas"].get(curso, "N/A")
            st.write(f"Nota anterior: {nota}/10")
        if st.button("Selecionar", key=curso):
            st.session_state.curso_atual = curso
            st.session_state.pagina = "curso"
            st.rerun()
    
    with col3:
        curso = "Lógica de Programação em Python"
        concluido = curso in cursos_concluidos
        st.write(f"### {curso}")
        if concluido:
            st.success("✅ Concluído")
            nota = usuarios[st.session_state.usuario_atual]["notas"].get(curso, "N/A")
            st.write(f"Nota anterior: {nota}/10")
        if st.button("Selecionar", key=curso):
            st.session_state.curso_atual = curso
            st.session_state.pagina = "curso"
            st.rerun()
    
    st.write("---")
    
    # Verificar se todos os cursos foram concluídos
    if len(cursos_concluidos) == 3:
        st.session_state.pagina = "conclusao"
        st.rerun()
    
    # Botão de logout
    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario_atual = None
        st.session_state.pagina = "login"
        st.rerun()

# Função para mostrar a página do curso
def mostrar_curso():
    if not st.session_state.logado or not st.session_state.curso_atual:
        st.session_state.pagina = "login"
        st.rerun()
        return
    
    st.title(st.session_state.curso_atual)
    
    if st.button("Assistir Aula"):
        webbrowser.open_new_tab(cursos[st.session_state.curso_atual]["video"])
    
    if st.button("Realizar Atividades"):
        st.session_state.respostas = []
        st.session_state.pontuacao = 0
        st.session_state.pagina = "atividades"
        st.rerun()
    
    if st.button("Voltar para Cursos"):
        st.session_state.curso_atual = None
        st.session_state.pagina = "cursos"
        st.rerun()

# Função para mostrar a página de atividades
def mostrar_atividades():
    if not st.session_state.logado or not st.session_state.curso_atual:
        st.session_state.pagina = "login"
        st.rerun()
        return
    
    st.title(f"Atividades - {st.session_state.curso_atual}")
    st.write("Responda às perguntas abaixo. Você precisa acertar pelo menos 7 questões para concluir o curso.")
    
    perguntas = cursos[st.session_state.curso_atual]["perguntas"]
    
    for i, pergunta in enumerate(perguntas):
        st.write(f"### {i+1}. {pergunta['pergunta']}")
        resposta = st.radio(
            f"Selecione uma opção (Pergunta {i+1}):",
            options=pergunta['opcoes'],
            key=f"pergunta_{i}",
            index=None
        )
        
        if resposta:
            indice_resposta = pergunta['opcoes'].index(resposta)
            if i < len(st.session_state.respostas):
                st.session_state.respostas[i] = indice_resposta
            else:
                st.session_state.respostas.append(indice_resposta)
    
    if len(st.session_state.respostas) == len(perguntas) and None not in st.session_state.respostas:
        if st.button("Enviar Respostas"):
            # Calcular pontuação
            st.session_state.pontuacao = 0
            for i, resposta in enumerate(st.session_state.respostas):
                if resposta == perguntas[i]['resposta_correta']:
                    st.session_state.pontuacao += 1
            
            st.session_state.pagina = "resultado"
            st.rerun()
    
    if st.button("Voltar para o Curso"):
        st.session_state.pagina = "curso"
        st.rerun()

# Função para mostrar a página de resultado
def mostrar_resultado():
    if not st.session_state.logado or not st.session_state.curso_atual:
        st.session_state.pagina = "login"
        st.rerun()
        return
    
    st.title(f"Resultado - {st.session_state.curso_atual}")
    
    if st.session_state.pontuacao >= 7:
        st.success(f"Parabéns! Você acertou {st.session_state.pontuacao} de 10 questões e concluiu o curso!")
        
        # Registrar curso como concluído e salvar nota
        usuarios = carregar_usuarios()
        if st.session_state.curso_atual not in usuarios[st.session_state.usuario_atual]["cursos_concluidos"]:
            usuarios[st.session_state.usuario_atual]["cursos_concluidos"].append(st.session_state.curso_atual)
            usuarios[st.session_state.usuario_atual]["notas"][st.session_state.curso_atual] = st.session_state.pontuacao
            salvar_usuarios(usuarios)
    else:
        st.error(f"Você acertou {st.session_state.pontuacao} de 10 questões. Você precisa acertar pelo menos 7 para concluir o curso.")
        
        if st.button("Tentar Novamente"):
            st.session_state.respostas = []
            st.session_state.pontuacao = 0
            st.session_state.pagina = "atividades"
            st.rerun()
    
    if st.button("Voltar para Cursos"):
        st.session_state.curso_atual = None
        st.session_state.pagina = "cursos"
        st.rerun()

# Função para mostrar a página de conclusão
def mostrar_conclusao():
    if not st.session_state.logado:
        st.session_state.pagina = "login"
        st.rerun()
        return
    
    st.title("🎉 PARABÉNS! 🎉")
    st.balloons()
    
    st.markdown("""
    ## 🎊 Você concluiu todos os cursos disponíveis! 🎊
    
    Você demonstrou dedicação e empenho ao completar todos os nossos cursos.
    Esperamos que o conhecimento adquirido seja útil em sua jornada!
    
    ### 🏆 Certificado de Conclusão 🏆
    
    Este certificado é concedido a:
    """)
    
    st.subheader(f"🌟 {st.session_state.usuario_atual} 🌟")
    
    st.markdown("""
    Por ter concluído com sucesso todos os cursos da nossa plataforma.
    
    Cursos concluídos:
    """)
    
    usuarios = carregar_usuarios()
    notas = usuarios[st.session_state.usuario_atual]["notas"]
    
    for curso in usuarios[st.session_state.usuario_atual]["cursos_concluidos"]:
        nota = notas.get(curso, "N/A")
        st.markdown(f"- ✅ {curso} - Nota: {nota}/10")
    
    st.markdown("""
    🚀 Continue aprendendo e crescendo! 🚀
    """)
    
    if st.button("Voltar para Cursos"):
        st.session_state.pagina = "cursos"
        st.rerun()
    
    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario_atual = None
        st.session_state.pagina = "login"
        st.rerun()

# Executar o aplicativo
if __name__ == "__main__":
    main()
