import streamlit as st 
from streamlit_lottie import st_lottie
import requests
import base64

def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao carregar Lottie:", response.status_code)
        return None
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Resposta não é JSON válida.")
        return None


# Markdown
'''

# Olá, eu sou o André Santana Martins
---
## Sobre Mim

Sou Técnico de Informática na **Prefeitura de Belo Horizonte** e estou cursando **Análise e Desenvolvimento de Sistemas** na **UNIFENAS**, atualmente no 3º/5º período. Buscando aprimorar minhas habilidades e expandir meu conhecimento, estou me formando como **Desenvolvedor Full Stack** através da **Infinity School**.

Com foco nas principais linguagens de programação e tecnologias do mercado, estou sempre em busca de novos desafios e oportunidades para crescer como desenvolvedor.
'''
st.image("https://raw.githubusercontent.com/SantanaDZ/curriculo-teste/refs/heads/main/curriculo_online/img/profile.jpeg", width=180)
'''
'''
#lottie_json = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_kkflmtur.json")
#if lottie_json:
 #   st_lottie(lottie_json, height=300)
#else:
 #   st.warning("Falha ao carregar animação.")

'''        

---

## Experiência Profissional na área de tecnologia

2020 - 2022 

Estágio de Técnico de TI - Prodabel
'''
st.image("https://raw.githubusercontent.com/SantanaDZ/curriculo-teste/refs/heads/main/curriculo_online/img/PRODABEL.png",width=180)
         
'''
2022 - Atualmente

Técnico de TI - Zoom Tecnologia 
'''
st.image("https://raw.githubusercontent.com/SantanaDZ/curriculo-teste/refs/heads/main/curriculo_online/img/zoom.png",width=180)
'''

---

## Tecnologias que estou aprendendo e utilizando:

- **Frontend**: HTML, CSS, JavaScript, React
- **Backend**: Node.js, Express
- **Banco de Dados**: MySQL, MongoDB
- **Ferramentas**: Git, GitHub, Docker
- **Metodologias Ágeis**: Scrum, Kanban
'''
lottie_json = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")
if lottie_json:
    st_lottie(lottie_json, height=300)
else:
    st.warning("Falha ao carregar animação.")
'''    

---

# Projetos

Confira alguns dos meus projetos abaixo:

- [Cadastro de Produtos](https://github.com/SantanaDZ/Cadastro-de-Produtos) – Sistema de cadastro de produtos com interface gráfica.
- [Auto Cert](https://github.com/SantanaDZ/AUTO-CERT) – Gerador automático de certificados personalizados.
- [Curso Infinity](https://github.com/SantanaDZ/CURSO-INFINITY) – Projetos produzidos no curso Infinty.

---

# Como me encontrar

- **E-mail**: [andresantmartins@outlook.com](mailto:andresantmartins@outlook.com)
- **LinkedIn**: [André Santana Martins](https://www.linkedin.com/in/andre-santana-martins-b8b619355)
- **Telefone**: +55(31)98438-2472
---

Estou sempre aberto a novas oportunidades e colaborações. Sinta-se à vontade para entrar em contato! 

'''

st.markdown("###  Formulário de Contato ")

with st.form("formspree_form"):
    name = st.text_input("Nome")
    email = st.text_input("Email")
    message = st.text_area("Mensagem")
    submit = st.form_submit_button("Enviar")

    if submit:
        
        form_data = {
            "name": name,
            "email": email,
            "message": message
        }
        response = requests.post(
            "https://formspree.io/f/xkgbjnkd",  # Substitua com seu endpoint
            data=form_data
        )
        if response.status_code == 200:
            st.success("Mensagem enviada com sucesso!")
        else:
            st.error("Erro ao enviar. Tente novamente.")




lottie_json = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_kkflmtur.json")
if lottie_json:
    st_lottie(lottie_json, height=300)
else:
    st.warning("Falha ao carregar animação.")
