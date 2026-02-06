import streamlit as st
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (#DC0612)
# =================================================================
st.set_page_config(page_title="L'Esorcista delle Recensioni", page_icon="🛡️", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
<style>
    header {{visibility: hidden !important;}}
    .stApp {{ background-color: #ffffff !important; }}
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, label, div {{
        color: #1a1a1a !important;
    }}
    /* BOX RISPOSTA */
    .risposta-box {{
        background-color: #f8f9fa !important;
        border: 2px solid {ROSSO_BRAND} !important;
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
    }}
    .stButton>button {{ 
        width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; 
        background-color: {ROSSO_BRAND} !important; color: white !important;
    }}
</style>
""", unsafe_allow_html=True)

# =================================================================
# 2. LOGO E TITOLO
# =================================================================
st.markdown(f"<h1 style='text-align: center; color: {ROSSO_BRAND};'>🛡️ L'ESORCISTA DELLE RECENSIONI</h1>", unsafe_allow_html=True)
st.write("Trasforma un attacco in un'opportunità di marketing.")
st.divider()

# =================================================================
# 3. INPUT UTENTE
# =================================================================
col1, col2 = st.columns(2)

with col1:
    problema = st.selectbox("DI COSA SI LAMMENTANO?", [
        "Scegli l'accusa...",
        "Servizio lento / Camerieri distratti",
        "Prezzo troppo alto / Rapporto Q/P",
        "Cibo (freddo, non buono, poco)",
        "Cliente maleducato / Recensione falsa"
    ])

with col2:
    stile = st.selectbox("CHE TONO VUOI USARE?", [
        "Scegli lo stile...",
        "Professionale (Chiede scusa)",
        "Ironico (L'Esorcista)",
        "Duro (Difesa del Team)"
    ])

nome_cliente = st.text_input("Nome del cliente (opzionale):", "Gentile cliente")

# =================================================================
# 4. DATABASE RISPOSTE (SOP)
# =================================================================
# Qui puoi divertirti ad aggiungere tutte le varianti che vuoi!
risposte = {
    "Servizio lento / Camerieri distratti": {
        "Professionale (Chiede scusa)": "Ci dispiace molto per l'attesa. La serata è stata particolarmente intensa, ma questo non giustifica la mancanza di attenzione. La prossima volta chieda di me, vorrei scusarmi di persona.",
        "Ironico (L'Esorcista)": "Amiamo le cose fatte bene, e a volte la qualità richiede tempo. Forse abbiamo corso meno del solito, ma non eravamo distratti: stavamo solo preparando il suo piatto con troppa cura!",
        "Duro (Difesa del Team)": "I nostri ragazzi lavorano al massimo ogni sera. Può capitare un rallentamento, ma preferiamo un piatto servito con 5 minuti di ritardo che un servizio frettoloso e senza cuore."
    },
    "Prezzo troppo alto / Rapporto Q/P": {
        "Professionale (Chiede scusa)": "I nostri prezzi riflettono la scelta di materie prime di altissima qualità. Capiamo che possa sembrare sopra la media, ma l'eccellenza ha un costo che non vogliamo abbassare.",
        "Ironico (L'Esorcista)": "L'unico modo per abbassare il prezzo sarebbe abbassare la qualità, ma preferiamo perdere un cliente per il prezzo che per un piatto mediocre. L'eccellenza non è per tutti.",
        "Duro (Difesa del Team)": "Dietro quel prezzo ci sono stipendi onesti, affitti e prodotti selezionati. Se cerca il risparmio assoluto, purtroppo ha sbagliato locale."
    },
    "Cibo (freddo, non buono, poco)": {
        "Professionale (Chiede scusa)": "Siamo mortificati. Se ce lo avesse fatto notare subito, avremmo rifatto il piatto all'istante. Ci dia una seconda possibilità, la cena la offriamo noi.",
        "Ironico (L'Esorcista)": "I gusti sono soggettivi, ma la nostra qualità è oggettiva. Ci spiace che il suo palato non abbia vibrato con noi, ma i nostri chef sanno il fatto loro.",
        "Duro (Difesa del Team)": "Usiamo solo prodotti freschi e ricette collaudate. Accettiamo le critiche, ma i nostri standard sono altissimi e confermati da migliaia di clienti soddisfatti."
    },
    "Cliente maleducato / Recensione falsa": {
        "Professionale (Chiede scusa)": "Non abbiamo traccia della sua visita nel nostro database. Se c'è stato un errore, ci contatti in privato per risolvere.",
        "Ironico (L'Esorcista)": "Complimenti per la fantasia! Peccato che quella sera fossimo chiusi per turno. La prossima volta provi a venire davvero, magari le piacerà!",
        "Duro (Difesa del Team)": "Non permettiamo che il lavoro dei nostri ragazzi venga infangato da recensioni anonime e prive di fondamento. Ci vediamo in tribunale se necessario."
    }
}

# =================================================================
# 5. GENERAZIONE
# =================================================================
if st.button("GENERA RISPOSTA PERFETTA 🪄", type="primary"):
    if problema == "Scegli l'accusa..." or stile == "Scegli lo stile...":
        st.warning("Seleziona sia il problema che lo stile!")
    else:
        risultato = risposte[problema][stile]
        st.markdown(f"""
            <div class="risposta-box">
                <p style="color: #888; font-size: 12px; margin-bottom: 5px;">COPIA E INCOLLA QUESTA:</p>
                <h4 style="margin-top:0;">{nome_cliente},</h4>
                <p style="font-size: 18px; font-style: italic;">{risultato}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 **Consiglio dell'Esorcista:** Rispondi sempre entro 24 ore. L'indifferenza uccide più di una brutta recensione.")

# =================================================================
# 6. FOOTER E HUB
# =================================================================
st.write("")
st.link_button("🌐 VEDI TUTTE LE NOSTRE WEB APP", "https://hub-comunicattivamente.streamlit.app/")

st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; font-size: 14px;">
        © 2024 <a href="https://www.comunicattivamente.it" target="_blank" style="color:{ROSSO_BRAND}; font-weight:bold;">comunicAttivamente</a><br>
        Powered by SuPeR & Streamlit
    </div>
""", unsafe_allow_html=True)
