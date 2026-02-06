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
    footer {{visibility: hidden !important;}}
    .stApp {{ background-color: #ffffff !important; }}
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, label, div {{
        color: #1a1a1a !important;
    }}
    /* BOX RISPOSTA */
    .risposta-box {{
        background-color: #f8f9fa !important;
        border-left: 10px solid {ROSSO_BRAND} !important;
        padding: 30px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
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
st.markdown("<p style='text-align: center; font-weight: bold;'>Non rispondere con la pancia. Rispondi con la strategia.</p>", unsafe_allow_html=True)
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
# 4. DATABASE RISPOSTE CON VARIANTI (MULTIPLE CHOICES)
# =================================================================
# Ogni sezione ora ha una lista [] di risposte possibili.
risposte = {
    "Servizio lento / Camerieri distratti": {
        "Professionale (Chiede scusa)": [
            "Ci scusiamo sinceramente per l'attesa. La qualità richiede cura, ma quella sera abbiamo superato i tempi accettabili. Ci piacerebbe rimediare alla sua prossima visita.",
            "La puntualità è un nostro pilastro e ci dispiace aver fallito nel suo caso. Stiamo già lavorando con lo staff per ottimizzare i flussi. Grazie per la segnalazione.",
            "Siamo mortificati. Sappiamo che il tempo dei nostri clienti è prezioso. La prossima volta chieda di me, vorrei offrirle un aperitivo per scusarmi personalmente."
        ],
        "Ironico (L'Esorcista)": [
            "Amiamo fare le cose con calma e amore, ma forse quella sera abbiamo esagerato con la calma! La prossima volta ci metta un po' di pepe, correremo di più!",
            "I nostri camerieri non erano distratti, stavano solo ammirando la bellezza dei piatti prima di servirli. Battute a parte, ci spiace per l'attesa, faremo più palestra per correre tra i tavoli!",
            "Dicono che l'attesa aumenti il desiderio... ma forse 40 minuti sono troppi anche per il desiderio più grande! Ci scusi, stiamo già mettendo i motori turbo ai ragazzi."
        ],
        "Duro (Difesa del Team)": [
            "I nostri ragazzi danno l'anima ogni sera. Un rallentamento può capitare nei momenti di picco, ma preferiamo servire un piatto perfetto in ritardo che uno mediocre in fretta.",
            "Accettiamo la critica, ma difendiamo il lavoro della nostra squadra che gestisce centinaia di coperti con passione. Lavoreremo per migliorare, senza però sacrificare la qualità del servizio.",
            "Gestire un ristorante non è una gara di Formula 1. Ci scusiamo per l'attesa, ma il rispetto per il lavoro del nostro staff viene prima di tutto."
        ]
    },
    "Prezzo troppo alto / Rapporto Q/P": {
        "Professionale (Chiede scusa)": [
            "Il valore di un'esperienza non è solo nel piatto, ma nella ricerca delle materie prime e nel servizio. Ci spiace che non abbia percepito questo valore, ne faremo tesoro.",
            "Siamo consapevoli di non essere il locale più economico, ma puntiamo all'eccellenza. Il nostro listino riflette costi reali di qualità che non intendiamo tagliare.",
            "Grazie per il feedback. Il nostro obiettivo è offrire un rapporto qualità-prezzo onesto. Analizzeremo la sua segnalazione per capire dove possiamo migliorare l'esperienza."
        ],
        "Ironico (L'Esorcista)": [
            "La qualità costa, la mediocrità costa meno. Noi abbiamo scelto la prima strada, ma capiamo che non sia per tutti. Ci sono molti ottimi fast food nei paraggi!",
            "Più che un conto, quello è un investimento in felicità e prodotti d'eccellenza. Se il ritorno sull'investimento non l'ha soddisfatta, ci spiace, ma la qualità resta il nostro unico credo.",
            "Il prezzo è quello che paghi, il valore è quello che ottieni. Se ha visto solo i numeri sul pezzo di carta, significa che non siamo riusciti a trasmetterle l'amore che mettiamo in ogni ingrediente."
        ],
        "Duro (Difesa del Team)": [
            "Dietro quei prezzi ci sono fornitori locali pagati il giusto, personale in regola e materie prime selezionate. Non facciamo sconti sulla dignità del nostro lavoro.",
            "Svalutare il prezzo significa svalutare il prodotto e chi lo cucina. Se cerca il risparmio a tutti i costi, purtroppo la nostra filosofia è molto diversa dalla sua.",
            "Mantenere certi standard ha un costo. Se preferisce pagare meno per prodotti industriali, il mercato è pieno di opzioni. Noi continueremo sulla strada dell'identità."
        ]
    }
    # (Daniele, qui puoi aggiungere le altre categorie seguendo lo stesso schema con le parentesi [ ])
}

# =================================================================
# 5. GENERAZIONE
# =================================================================
if st.button("GENERA RISPOSTA STRATEGICA 🪄", type="primary"):
    if problema == "Scegli l'accusa..." or stile == "Scegli lo stile...":
        st.warning("Seleziona sia il problema che lo stile!")
    else:
        # La magia: random.choice pesca un elemento a caso dalla lista delle varianti
        varianti = risposte.get(problema, {}).get(stile, ["Ops, questa combinazione è in fase di scrittura!"])
        risultato = random.choice(varianti)
        
        st.markdown(f"""
            <div class="risposta-box">
                <p style="color: #888; font-size: 12px; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px;">Esorcismo completato:</p>
                <h4 style="margin-top:0;">{nome_cliente},</h4>
                <p style="font-size: 18px; font-style: italic; line-height: 1.5;">{risultato}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 **Non ti convince?** Clicca di nuovo sul tasto per generare una variante diversa!")

# =================================================================
# 6. FOOTER E HUB
# =================================================================
st.write("")
st.link_button("🌐 VEDI TUTTE LE NOSTRE WEB APP", "https://hub-comunicattivamente.streamlit.app/")

st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; font-size: 14px;">
        © 2024 <a href="https://www.comunicattivamente.it" target="_blank" style="color:{ROSSO_BRAND}; font-weight:bold; text-decoration:none;">comunicAttivamente</a><br>
        La tua difesa contro il Caos Digitale.
    </div>
""", unsafe_allow_html=True)
