import streamlit as st
import random

st.set_page_config(page_title="Teoria Musical 🎶", page_icon="🎶")

PERGUNTAS = [
    ("O que é musica?", ["é a arte do silencio.", "é a arte de expressar sentimentos.", "Nao sei.", "é a arte dos ruidos."], 1),
    ("Qual o elemento que se baseia na divisão ordenada do tempo, combinando sons curtos, longos e silencios?", ["timbre", "harmonia", "melodia", "ritmo"], 3),
    ("O que é altura?", ["é a propriedade do som ser curto ou longo.", "é a propriedade do som ser fraco ou forte.", "é a propriedade do som ser grave, medio ou agudo.", "é a propriedade que permite reconhecer a origem do som."], 2),
    ("O que é som?", ["é tudo o que ouvimos.", "é tudo o que vemos.", "é tudo o que produz sons naturais.", "é tudo o que sentimos."], 0),
    ("Quais sao os elementos mais importantes da musica?", ["harmonia, ritmo e arte.", "melodia, timbre e harmonia", "melodia, intensidade e altura", "melodia, harmonia e ritmo"], 3),
    ("Quantas e quais são as propriedades do som?", ["Sao 5: mi, sol, si, re e fa.", "Sao 4: duracao, intensidade, timbre e altura.", "Sao 4: melodia, harmonia, timbre e altura.", "Sao 4: Melodia, Harmonia, Ritmo e Contraponto."], 1),
    ("O que é timbre?", ["é a propriedade do som ser fraco ou forte.", "é a propriedade do som ser curto ou longo.", "é a propriedade que permite reconhecer a origem do som.", "é a propriedade do som ser grave, medio ou agudo."], 2),
    ("O que é Duracao?", ["é a propriedade do som ser curto ou longo.", "é a propriedade do som ser grave, medio ou agudo.", "é a propriedade do som ser fraco ou forte.", "é a propriedade que permite reconhecer a origem do som."], 0),
    ("O que é Intensidade?", ["é a propriedade do som ser grave, medio ou agudo.", "é a propriedade do som ser fraco ou forte.", "é a propriedade do som ser curto ou longo.", "é a propriedade que permite reconhecer a origem do som."], 3),
    ("O que é melodia?", ["é a producao dos sons sucessivos", "é a producao dos sons fortes", "é a producao dos sons fraco", "é a producao dos sons simultaneo"], 0),
    ("O que é harmonia?", ["é a producao dos sons fraco", "é a producao dos sons diferente", "é a producao dos sons iguais", "é a producao dos sons simultaneo"], 3),
    ("O que é ritmo?", ["é a vibracao de sons regulares", "é a combinacao de sons curtos, longos e silencios", "é a arte dos sons", "é a combinacao de sons curtos, fortes e fracos"], 1),
    ("O que são notas musicais?", ["são sinais que representam a frequencia na musica", "são sinais que representam o som na musica", "são sinais que representam ruidos dos instrumentos", "são sinais que representam a vibracao dos sons"], 1),
    ("Timbre, duração, altura e intensidade é: ?", ["propriedade da parte do som", "elementos da musica", "propriedade da musica", "propriedades do som"], 3),
    ("Quando o PENTAGRAMA não é suficiente, utilizamos?", ["Outra pauta superior ou inferior.", "Outro pentagrama superior ou inferior.", "Outro sistema de pautas.", "Linhas e espacos suplementares superiores e inferiores."], 3),
    ("Ao conjunto de sinais que representam a escrita musical da-se o nome de?", ["Notacao Figurativa", "Notacao Musical", "Notacao Instrumental", "Notacao de Arranjos"], 1),
    ("No hinario são utilizadas apenas as CLAVES de: ?", ["Sol, Fa e Do 2a linha", "Sol, Fa e Do 4a linha", "Sol, Fa e Do 1a linha", "Sol, Fa e Do 3a linha"], 3),
    ("A clave de DO é escrita em qual linha? ", ["5a linha", "3a linha", "4a linha", "1o espaco"], 1),
    ("A clave de sol é escrita em qual linha?", ["terceira linha", "segunda linha", "primeira linha", "quarta linha"], 1),
    ("O que é utilizado para REPRESENTAR os sons através das figuras?", ["conjunto de 6 linhas e 5 espacos", "conjunto de 4 linhas e 5 espacos", "conjunto de 5 linhas e 4 espacos", "conjunto de 5 linhas e 5 espacos"], 2),
    ("Existem 3 sinais de clave: sol, fa e do que REPRESENTAM o total de?", ["5 claves", "7 claves", "4 claves", "6 claves"], 1),
    ("O que as notas musicais representam?", ["os sons graficamente", "a media de velocidade", "a intensidade dos sons graficamente", "a articulacao e andamento dos sons graficamente"], 0),
    ("As notas musicais são:", ["4; do, re, mi e fa", "5; do, re, mi, fa e sol", "8; do, re, mi, fa, sol, la, si e do", "7; do, re, mi, fa, sol, la e si"], 3),
    ("O nome PENTAGRAMA vem do grego:", ["penta = linha; grama = cinco", "penta = cinco; grama = kilo", "penta = cinco; grama = linha", "penta = seis; grama = linha"], 2),
    ("Como são contados as linhas e espacos do pentagrama?", ["de cima para baixo", "de cima para o lado direito", "de baixo para o lado esquerdo", "de baixo para cima"], 3),
    ("Quais são os três sinais de clave existentes?", ["sol, fa e mi", "sol, fa e re", "la, fa e do", "sol, fa e do"], 3),
    ("A clave de FA é escrita em qual linha?", ["3a linha", "4a linha", "5a linha", "1a linha"], 1),
    ("Complete: a ____ é a produção ordenada de sons sucessivos. Exemplo: _____.", ["melodia, trompete", "ritmo, piano", "harmonia, trompete", "harmonia, flauta"], 0),
    ("Qual alternativa abaixo não tem um ritmo constante?", ["palma", "pisca-alerta do carro", "metronomo", "relogio"], 0),
    ("Qual das alternativas abaixo faz parte da propriedade do som 'altura'?", ["grave, medio, agudo", "alto, medio, baixo", "pianissimo, piano, extra forte", "grave, forte, agudo"], 0),
    ("De acordo com a teoria do MSA nos temos:", ["7 notas musicais", "6 notas musicais", "8 notas musicais", "5 notas musicais"], 0),
    ("O NOME e a ALTURA das figuras musicais no PENTAGRAMA sao determinados pela?", ["nota", "pausa", "pauta", "clave"], 3),
    ("No hinario, cantar ou tocar separadamente as vozes do soprano, contralto, tenor ou baixo caracterizam:", ["melodia", "ritmo", "harmonia", "altura"], 0),
]

CODIGO_VÁLIDOS = ["JESSICA2026", "MIRIA01", "GABI01", "FERNANDA01"]

# --- TELA DE CÓDIGO ---
if "liberado" not in st.session_state:
    st.session_state.liberado = False
if "perguntas" not in st.session_state:
    st.session_state.perguntas = random.sample(PERGUNTAS, len(PERGUNTAS))
    st.session_state.indice = 0
    st.session_state.acertos = 0
    st.session_state.respondeu = False
    st.session_state.finalizado = False

st.title("Teoria Musical 🎶")

if not st.session_state.liberado:
    st.write("Digite o código para entrar:")
    codigo = st.text_input("Código", type="password")
    if st.button("Entrar"):
        if codigo in CODIGO_VÁLIDOS:
            st.session_state.liberado = True
            st.rerun()
        else:
            st.error("Código errado! Tente de novo.")
    st.stop()

# --- QUIZ ---
perguntas = st.session_state.perguntas
indice = st.session_state.indice

if st.session_state.finalizado:
    porcentagem = st.session_state.acertos * 100 / len(perguntas)
    if porcentagem >= 70:
        st.success(f"PARABENS! Você acertou {int(porcentagem)}%! Você pode prosseguir para a Fase 2!")
        st.write("Fase 1 concluída!")
        st.markdown("### Deus abençoe! Nos vemos na Fase 2!\n**Jéssica Guida**")
    else:
        st.error(f"Você acertou {int(porcentagem)}%. Você precisa acertar 70% para prosseguir!")
        st.write("Tente de novo!")
    if st.button("Jogar de novo"):
        st.session_state.perguntas = random.sample(PERGUNTAS, len(PERGUNTAS))
        st.session_state.indice = 0
        st.session_state.acertos = 0
        st.session_state.respondeu = False
        st.session_state.finalizado = False
        st.rerun()
    st.stop()

st.write(f"Acertos: {st.session_state.acertos} | Pergunta: {indice+1}/{len(perguntas)}")
q = perguntas[indice]
st.subheader(f"{indice+1}. {q[0]}")

letras = ["A", "B", "C", "D"]
escolha = st.radio("Escolha:", [f"{letras[i]}) {q[1][i]}" for i in range(4)], key=f"q{indice}")

if st.button("Confirmar resposta") and not st.session_state.respondeu:
    st.session_state.respondeu = True
    idx_escolha = letras.index(escolha[0])
    if idx_escolha == q[2]:
        st.session_state.acertos += 1
        st.session_state.correto = True
    else:
        st.session_state.correto = False
    st.rerun()

if st.session_state.respondeu:
    if st.session_state.correto:
        st.success("Correto!")
    else:
        st.error(f"Errado! Resposta certa: {letras[q[2]]}) {q[1][q[2]]}")
    if st.button("Próxima"):
        st.session_state.respondeu = False
        if indice >= len(perguntas)-1:
            st.session_state.finalizado = True
        else:
            st.session_state.indice += 1
        st.rerun()
