import streamlit as st

# Configurazione iniziale della pagina Streamlit ottimizzata per mobile
st.set_page_config(page_title="EcoRischio Liguria", layout="centered")

# CSS universale: blocca lo scroll a 100vh e separa gli stili dei pulsanti
st.markdown("""
<style>
 /* Vincola l'applicazione all'altezza esatta della vista del telefono */
 html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
 max-height: 100vh !important;
 height: 100vh !important;
 overflow: hidden !important;
 }
 
 /* Compatta l'area di lavoro eliminando i padding nativi eccessivi */
 .main .block-container {
 padding-top: 0.2rem !important;
 padding-bottom: 0.2rem !important;
 padding-left: 0.5rem !important;
 padding-right: 0.5rem !important;
 max-height: 100vh !important;
 display: flex !important;
 flex-direction: column !important;
 justify-content: space-between !important;
 }

 /* Ottimizzazione dei testi per preservare lo spazio verticalizzato */
 h3 {
 margin-top: 0px !important;
 margin-bottom: 4px !important;
 font-size: 1.2rem !important;
 }
 p, div, span {
 margin-bottom: 2px !important;
 font-size: 13.5px !important;
 }
 .stMarkdown {
 margin-bottom: 0px !important;
 }

 /* Classe specifica per forzare l'affiancamento orizzontale continuo su mobile */
 .riga-pulsanti-flex {
 display: flex !important;
 flex-direction: row !important;
 flex-wrap: nowrap !important;
 justify-content: space-between !important;
 width: 100% !important;
 gap: 8px !important;
 margin-bottom: 4px !important;
 }

 /* Stile base universale dei pulsanti operativi inferiori */
 .riga-pulsanti-flex button {
 width: 100% !important;
 height: 42px !important;
 font-size: 14.5px !important;
 font-weight: bold !important;
 border-radius: 10px !important;
 border: none !important;
 }

 /* Colore Rosso per il primo pulsante operativo (NO / ASSENTE / ALTRO) */
 .riga-pulsanti-flex div:nth-of-type(1) button {
 background-color: #e74c3c !important;
 color: white !important;
 }

 /* Colore Verde per il secondo pulsante operativo (SI / PRESENTE / CONFERMA) */
 .riga-pulsanti-flex div:nth-of-type(2) button {
 background-color: #2ecc71 !important;
 color: white !important;
 }

 /* BARRA SUPERIORE ISOLATA: Stile neutro, scuro e discreto senza colori accesi */
 .barra-superiore-nav {
 display: flex !important;
 flex-direction: row !important;
 gap: 10px !important;
 margin-bottom: 2px !important;
 }
 .barra-superiore-nav button {
 background-color: transparent !important;
 color: #8a9199 !important;
 border: 1px solid #3b424a !important;
 height: 32px !important;
 font-size: 12.5px !important;
 font-weight: normal !important;
 border-radius: 6px !important;
 padding: 0px 12px !important;
 }

 /* Riquadro per le immagini surrogato ad altezza percentuale reattiva */
 .box-immagine-surrogato {
 width: 100%;
 height: 18vh !important;
 border: 2px dashed #bdc3c7;
 border-radius: 8px;
 display: flex;
 align-items: center;
 justify-content: center;
 background-color: #f8f9fa;
 color: #7f8c8d;
 font-weight: bold;
 text-align: center;
 font-size: 12.5px;
 margin-bottom: 4px;
 padding: 6px;
 }
</style>
""", unsafe_allow_html=True)

# Funzione helper per generare il riquadro rettangolare senza caricare file esterni
def mostra_box_immagine(testo_etichetta):
 st.markdown(f'<div class="box-immagine-surrogato">RIQUADRO: {testo_etichetta}</div>', unsafe_allow_html=True)
# -------------------------------------------------------------------------
# DATABASE AMBIENTALE LIGURE CON ETICHETTE DI TESTO AL POSTO DEI LINK WEB
# -------------------------------------------------------------------------
DATABASE_AMBIENTALE = {
 "Ambiente Costiero e Marino": {
 "etichetta_img": "Ambiente Costiero e Marino della Liguria",
 "descrizione": "Contesto marino, litorali sabbiosi e scogliere della Liguria.",
 "sottocategorie": {
 "Ambiente Marino Subacqueo": {
 "peso_habitat": 40,
 "etichetta_img": "Ambiente Marino Subacqueo (Fondali)",
 "descrizione": "Fondali marini e praterie sommerse.",
 "flora": [
 ("Ulva lactuca", 5, "Alga Lattuga di mare", "Lattuga di mare (alga verde comune)."),
 ("Padina pavonica", 5, "Alga a coda di pavone", "Alga a coda di pavone."),
 ("Posidonia oceanica", 15, "Prateria di Posidonia oceanica", "Pianta marina protetta."),
 ("Cymodocea nodosa", 15, "Erba marina Cymodocea nodosa", "Erba marina che forma praterie.")
 ],
 "fauna": [
 ("Coris julis", 5, "Pesce Donzella", "Donzella, pesce di scogliera."),
 ("Octopus vulgaris", 5, "Polpo comune", "Polpo comune."),
 ("Pinna nobilis", 15, "Mollusco Nacchera di mare", "Nacchera di mare protetta."),
 ("Hippocampus hippocampus", 15, "Cavalluccio marino", "Cavalluccio marino.")
 ]
 },
 "Costa Rocciosa e Scogliere": {
 "peso_habitat": 35,
 "etichetta_img": "Scarpate rocciose marine e zone sopralitorali",
 "descrizione": "Scarpate rocciose marine e zone sopralitorali.",
 "flora": [
 ("Crithmum maritimum", 5, "Finocchio marino", "Finocchio marino."),
 ("Limonium vulgare", 5, "Campanella delle spiagge", "Campanella delle spiagge / Limonio."),
 ("Campanula sabatia", 15, "Campanula di Savona", "Campanula di Savona, endemismo ligure protetto."),
 ("Centaurea paniculata", 15, "Fiordaliso sfiocchettato", "Fiordaliso sfiocchettato.")
 ],
 "fauna": [
 ("Pachygrapsus marmoratus", 5, "Granchio corridore delle scogliere", "Granchio corridore delle scogliere."),
 ("Podarcis muralis", 5, "Lucertola muraiola", "Lucertola muraiola."),
 ("Gulosus aristotelis", 15, "Marangone dal ciuffo", "Marangone dal ciuffo (uccello marino)."),
 ("Falco peregrinus", 15, "Falco pellegrino", "Falco pellegrino.")
 ]
 },
 "Litorale Sabbioso e Chiotto (Spiagge)": {
 "peso_habitat": 30,
 "etichetta_img": "Arenili e depositi ciottolosi costieri",
 "descrizione": "Arenili e depositi ciottolosi costieri.",
 "flora": [
 ("Cakile maritima", 5, "Ravastrello marittimo", "Ravastrello marittimo."),
 ("Medicago marina", 5, "Erba medica marina", "Erba medica marina."),
 ("Pancratium maritimum", 15, "Giglio marino delle dune", "Giglio marino delle dune."),
 ("Eryngium maritimum", 15, "Calcatreppola marina", "Calcatreppola marina.")
 ],
 "fauna": [
 ("Talitrus saltator", 5, "Pulce di mare", "Pulce di mare."),
 ("Theba pisana", 5, "Chiocciolina delle sabbie", "Chiocciolina delle sabbie."),
 ("Charadrius dubius", 15, "Corriere piccolo", "Corriere piccolo."),
 ("Charadrius alexandrinus", 15, "Corriere fratino", "Corriere fratino, volatile protetto delle dune.")
 ]
 }
 }
 },
 "Ambiente d'Acqua Dolce e Umido": {
 "etichetta_img": "Rivi, torrenti, fiumare e specchi palustri",
 "descrizione": "Rivi, torrenti, fiumare e specchi palustri.",
 "sottocategorie": {
 "Zone Umide, Laghi e Zone Palustri": {
 "peso_habitat": 35,
 "etichetta_img": "Acque ferme, paludi e laghetti d'alta quota",
 "descrizione": "Acque ferme, paludi e laghetti d'alta quota.",
 "flora": [
 ("Phragmites australis", 5, "Canna di palude", "Canna di palude."),
 ("Typha latifolia", 5, "Mazza di sorda / Tifa", "Mazza di sorda / Tifa."),
 ("Drosera rotundifolia", 15, "Pianta carnivora delle torbiere liguri", "Pianta carnivora delle torbiere liguri."),
 ("Adiantum capillus-veneris", 15, "Felce Capelvenere", "Capelvenere, felce di ambienti umidi sgocciolanti.")
 ],
 "fauna": [
 ("Pelophylax esculentus", 5, "Rana verde comune", "Rana verde comune."),
 ("Anax imperator", 5, "Libellula imperatore", "Libellula imperatore."),
 ("Speleomantes strinatii", 15, "Geotritone di Strinati", "Geotritone di Strinati, anfibio endemico protetto."),
 ("Bombina variegata", 15, "Ululone dal ventre giallo", "Ululone dal ventre giallo.")
 ]
 },
 "Corsi d'Acqua (Rivi, Torrenti e Fiumare)": {
 "peso_habitat": 30,
 "etichetta_img": "Rete idrografica superficiale corrente ligure",
 "descrizione": "Rete idrografica superficiale corrente.",
 "flora": [
 ("Apium nodiflorum", 5, "Sedano d'acqua", "Sedano d'acqua."),
 ("Mentha spicata", 5, "Menta selvatica", "Menta selvatica."),
 ("Adiantum capillus-veneris", 15, "Felce capelvenere", "Felce capelvenere."),
 ("Ranunculus aquatilis", 15, "Ranuncolo d'acqua flottante", "Ranuncolo d'acqua flottante.")
 ],
 "fauna": [
 ("Potamon fluviatile", 5, "Granchio di fiume d'acqua dolce", "Granchio di fiume d'acqua dolce."),
 ("Hierophis viridiflavus", 5, "Biacco (serpente innocuo)", "Biacco (serpente innocuo comune)."),
 ("Salmo trutta", 15, "Trota fario autoctona", "Trota fario autoctona."),
 ("Alcedo atthis", 15, "Martino pescatore", "Martino pescatore.")
 ]
 }
 }
 },
 "Ambiente Forestale e Boschivo": {
 "etichetta_img": "Boschi montani, macchia litoranea e colline liguri",
 "descrizione": "Boschi montani, macchia litoranea e formazioni collinari.",
 "sottocategorie": {
 "Boschi Montani di Conifere e Faggete": {
 "peso_habitat": 30,
 "etichetta_img": "Faggete interne e foreste di alta quota alpine o appenniniche",
 "descrizione": "Faggete interne e foreste di alta quota alpine o appenniniche.",
 "flora": [
 ("Fagus sylvatica", 5, "Faggio comune", "Faggio comune."),
 ("Vaccinium myrtillus", 5, "Mirtillo nero", "Mirtillo nero."),
 ("Ilex aquifolium", 15, "Agrifoglio spontaneo protetto", "Agrifoglio spontaneo protetto."),
 ("Taxus baccata", 15, "Albero del Tasso protetto", "Tasso, relitto glaciale protetto.")
 ],
 "fauna": [
 ("Sus scrofa", 5, "Cinghiale europeo", "Cinghiale europeo."),
 ("Sciurus vulgaris", 5, "Scoiattolo rosso comune", "Scoiattolo rosso comune."),
 ("Canis lupus", 15, "Lupo appenninico", "Lupo appenninico."),
 ("Speleomantes strinatii", 15, "Geotritone di Strinati forestale", "Geotritone di Strinati.")
 ]
 },
 "Macchia Mediterranea e Boschi Costieri": {
 "peso_habitat": 25,
 "etichetta_img": "Arbusteti densi, leccete costiere e pinete marittime",
 "descrizione": "Arbusteti densi, leccete costiere e pinete marittime.",
 "flora": [
 ("Pistacia lentiscus", 5, "Lentisco", "Lentisco."),
 ("Olea europaea", 5, "Olivo selvatico / Oleastro", "Olivo selvatico / Oleastro."),
 ("Chamaerops humilis", 15, "Palma nana mediterranea", "Palma nana mediterranea spontanea."),
 ("Arbutus unedo", 15, "Albero del Corbezzolo", "Corbezzolo.")
 ],
 "fauna": [
 ("Sus scrofa", 5, "Cinghiale della macchia", "Cinghiale."),
 ("Tarentola mauritanica", 5, "Geco comune ligure", "Geco comune."),
 ("Timon lepidus", 15, "Lucertola ocellata ligure", "Lucertola ocellata, il piu grande sauro europeo."),
 ("Testudo hermanni", 15, "Tartaruga di terra protetta", "Tartaruga di terra protetta.")
 ]
 },
 "Boschi di Latifoglie Decidue (Fascia Collinare)": {
 "peso_habitat": 20,
 "etichetta_img": "Castagneti, cerrete e boschi misti collinari",
 "descrizione": "Castagneti, cerrete e boschi misti collinari.",
 "flora": [
 ("Castanea sativa", 5, "Albero del Castagno", "Castagno."),
 ("Quercus pubescens", 5, "Albero di Roverella", "Roverella."),
 ("Anemone nemorosa", 15, "Anemone dei boschi", "Anemone dei boschi."),
 ("Paeonia officinalis", 15, "Peonia selvatica protetta", "Peonia selvatica protetta.")
 ],
 "fauna": [
 ("Sus scrofa", 5, "Cinghiale collinare", "Cinghiale."),
 ("Podarcis muralis", 5, "Lucertola muraiola dei boschi", "Lucertola muraiola."),
 ("Lucanus cervus", 15, "Coleottero Cervo volante", "Cervo volante, coleottero protetto europeo."),
 ("Hierophis viridiflavus", 15, "Serpente Biacco", "Biacco.")
 ]
 }
 }
 },
 "Ambiente Montano Alto e Rupestre": {
 "etichetta_img": "Cime, ghiaioni alpini, pascoli e pareti rocciose liguri",
 "descrizione": "Cime, ghiaioni alpini, pascoli e pareti rocciose.",
 "sottocategorie": {
 "Ambienti Rupestri e Ghiaioni d'Alta Quota": {
 "peso_habitat": 30,
 "etichetta_img": "Pareti di roccia nuda e sfasciumi d'alta quota",
 "descrizione": "Pareti di roccia nuda e sfasciumi d'alta quota.",
 "flora": [
 ("Sempervivum arachnoideum", 5, "Semprevivo ragnatelo", "Semprevivo ragnatelo."),
 ("Sedum acre", 5, "Borracina acre", "Borracina acre."),
 ("Primula allionii", 15, "Primula di Allioni rupicola", "Primula di Allioni, rarissimo endemismo rupicolo."),
 ("Campanula sabatia", 15, "Campanula ligure montana", "Campanula ligure.")
 ],
 "fauna": [
 ("Podarcis muralis", 5, "Lucertola muraiola rupestre", "Lucertola muraiola."),
 ("Prunella collaris", 5, "Uccello Sordone d'alta quota", "Sordone (uccello d'alta quota)."),
 ("Aquila chrysaetos", 15, "Aquila reale ligure", "Aquila reale."),
 ("Falco peregrinus", 15, "Falco pellegrino montano", "Falco pellegrino.")
 ]
 },
 "Praterie di Altitudine e Pascoli": {
 "peso_habitat": 25,
 "etichetta_img": "Praterie naturali sopra il limite degli alberi",
 "descrizione": "Praterie naturali sopra il limite degli alberi.",
 "flora": [
 ("Trifolium alpinum", 5, "Trifoglio alpino", "Trifoglio alpino."),
 ("Tarassaco montano", 5, "Tarassaco di montagna", "Tarassaco di montagna."),
 ("Narcissus poeticus", 15, "Narciso selvatico protetto", "Narciso selvatico protetto."),
 ("Viola bertolonii", 15, "Viola di Bertoloni endemica", "Viola di Bertoloni, endemismo ligure-provenzale.")
 ],
 "fauna": [
 ("Chionomys nivalis", 5, "Arvicola delle nevi", "Arvicola delle nevi."),
 ("Falco tinnunculus", 5, "Falco Gheppio", "Gheppio."),
 ("Vipera ursinii", 15, "Vipera dell'Orsini iper-protetta", "Vipera dell'Orsini, specie rarissima e iper-protetta."),
 ("Anthus campestris", 15, "Uccello Calandro delle praterie", "Calandro.")
 ]
 }
 }
 },
 "Ambiente Antropizzato e Agricolo": {
 "etichetta_img": "Zone urbane, fasce terrazzate e oliveti storici liguri",
 "descrizione": "Zone urbane, fasce terrazzate, oliveti storici liguri.",
 "sottocategorie": {
 "Terrazzamenti, Oliveti e Vigneti / Zone Urbane": {
 "peso_habitat": 15,
 "etichetta_img": "Muretti a secco tradizionali e insediamenti rurali o urbani",
 "descrizione": "Muretti a secco tradizionali e insediamenti rurali o urbani.",
 "flora": [
 ("Olea europaea", 5, "Albero dell'Olivo coltivato", "Olivo coltivato."),
 ("Parietaria officinalis", 5, "Erba vetriola delle mura", "Erba vetriola delle mura."),
 ("Anacamptis pyramidalis", 15, "Orchidea piramidale selvatica", "Orchidea piramidale selvatica protetta."),
 ("Capparis spinosa", 15, "Pianta del cappero delle vecchie mura", "Pianta del cappero delle vecchie mura.")
 ],
 "fauna": [
 ("Sus scrofa", 5, "Cinghiale in zona urbana", "Cinghiale urbano."),
 ("Tarentola mauritanica", 5, "Geco dei muretti a secco", "Geco dei muretti."),
 ("Pipistrellus kuhlii", 15, "Pipistrello albolimbato urbano", "Pipistrello albolimbato."),
 ("Euplagia quadripunctaria", 15, "Falena dell'edera protetta", "Falena dell'edera (Specie protetta Direttiva Habitat).")
 ]
 }
 }
 }
}
# -------------------------------------------------------------------------
# MATRICI OPERA E MATRICI FISICHE ATOMICHE (CON ETICHETTE DI TESTO)
# -------------------------------------------------------------------------
MATRICI_FISICHE_EDILIZIE = {
 "suolo": [
 ("Terreno sabbioso o roccia compatta", 0, "Terreno sabbioso stabilizzato o roccia compatta di cantiere", "Basso rischio di compattamento."),
 ("Terreno limoso o argilloso", 15, "Deposito di terreno limoso o argilloso umido di cantiere", "Rischio moderato di fango e instabilita."),
 ("Humus fertile, organico o forestale", 20, "Strato di humus fertile, organico o forestale protetto", "Alto valore ecologico e rischio erosione.")
 ],
 "pendenza": [
 ("Terreno pianeggiante o debole pendenza (inferiore a 15 gradi)", 0, "Versante di cantiere pianeggiante o a debole pendenza", "Bassa suscettibilita al dissesto."),
 ("Forte pendenza, versante o scarpata (superiore a 15 gradi)", 25, "Forte pendenza, versante instabile o scarpata ligure", "Versante instabile ad alto rischio.")
 ],
 "idro": [
 ("Presenza di fossi di scolo, canali artificiali o rii temporanei?", 10, "Fossi di scolo idrico, canali artificiali o rii temporanei", "Rileva corsi idrici minori stagionali."),
 ("Presenza di ruscelli, torrenti, fiumi perenni o specchi d'acqua?", 25, "Ruscello, torrente o fiume perenne entro cento metri", "Presenza idrica perenne stabile entro 100m.")
 ],
 "stato_acqua": [
 ("Corpo idrico visibilmente compromesso (scarichi, rifiuti, torbidita)?", 15, "Corpo idrico alterato da scarichi, rifiuti o forte torbidita", "Seleziona SI se la qualita dell'acqua e alterata.")
 ],
 "opera": [
 ("Manufatto leggero o temporaneo (legno, chioschi, recinzioni pesanti)", 15, "Manufatto edilizio leggero, temporaneo o prefabbricato in legno", "Basso impatto fisico volumetrico."),
 ("Edifici civili o industriali (abitazioni, uffici, parcheggi interrati)", 30, "Edificio civile o industriale permanente, fondazioni standard", "Impatto strutturale permanente medio-alto."),
 ("Infrastrutture pesanti o lineari (strade, ponti, gallerie, grandi muri)", 40, "Infrastruttura pesante lineare, tracciato stradale o grande muro", "Massimo impatto per modificazione dell'assetto del suolo.")
 ],
 "superficie": [
 ("Superficie ridotta (inferiore a 100 metri quadri)", 0, "Superficie di cantiere ridotta inferiore a cento metri quadri", "Minima area impermeabilizzata."),
 ("Superficie media (compresa tra 100 e 500 metri quadri)", 15, "Superficie di cantiere media compresa tra cento e cinquecento metri", "Modifica planimetrica standard."),
 ("Superficie estesa (superiore a 500 metri quadri)", 30, "Superficie estesa di progetto superiore a cinquecento metri quadri", "Ampia impronta di cantiere e impermeabilizzazione.")
 ],
 "altezza": [
 ("Altezza minima fuori terra (inferiore a 3 metri)", 0, "Elevazione minima fuori terra inferiore a tre metri di altezza", "Sviluppo verticale trascurabile."),
 ("Altezza moderata fuori terra (compresa tra 3 e 7 metri)", 10, "Elevazione moderata fuori terra compresa tra tre e sette metri", "Impatto visivo o faunistico medio."),
 ("Altezza rilevante fuori terra (superiore a 7 metri)", 20, "Elevazione strutturale rilevante superiore a sette metri fuori terra", "Forte impatto verticale permanente.")
 ],
 "scavi": [
 ("Scavi profondi o invasivi (fondazioni complesse, pali, tiranti, sotterranei)", 30, "Scavi edili ipogei profondi, pali di fondazione o tiranti", "Forte alterazione degli strati profondi geologici. (Se NO = punti 15).")
 ],
 "disturbi": [
 ("Logistica di cantiere pesante (transito frequente mezzi, stoccaggio)", 25, "Logistica pesante di cantiere e transito frequente di mezzi", "Disturbo logistico temporaneo."),
 ("Rumori continui o impulsivi (demolizioni, scavi meccanici, perforazioni)", 25, "Sorgenti acustiche continue o impulsive, scavi e demolizioni", "Disturbo acustico."),
 ("Inquinamento luminoso (illuminazione notturna di cantiere o esercizio)", 25, "Sorgenti di illuminazione notturna artificiale di cantiere", "Disturbo fotometrico della fauna notturna.")
 ]
}
# Lista ordinata sequenziale di tutti i possibili passi della procedura
ELENCO_PASSI = [
 "macro_area", "sottocategoria", "flora", "fauna", "suolo", "pendenza", 
 "idro", "stato_acqua", "bivio_opera", "opera", "superficie", "altezza", 
 "scavi", "disturbi", "risultato"
]

# -------------------------------------------------------------------------
# INIZIALIZZAZIONE DELLA SESSIONE E LOGICA DI NAVIGAZIONE
# -------------------------------------------------------------------------
if "micro_passo" not in st.session_state:
 st.session_state.micro_passo = "macro_area"
if "indice_corrente" not in st.session_state:
 st.session_state.indice_corrente = 0
if "cronologia" not in st.session_state:
 st.session_state.cronologia = []
if "scelte" not in st.session_state:
 st.session_state.scelte = {
 "macro_area": None, "sottocategoria": None, "peso_habitat": 0,
 "flora_rilevata": [], "fauna_rilevata": [], "punti_suolo": 0, "suolo_testo": "",
 "punti_pendenza": 0, "pendenza_testo": "", "punti_idro": 0, "idro_testo": "",
 "punti_stato_acqua": 0, "stato_acqua_testo": "Non applicabile", "punti_opera": 0, "opera_testo": "",
 "punti_superficie": 0, "superficie_testo": "", "punti_altezza": 0, "altezza_testo": "",
 "punti_scavi": 15, "scavi_testo": "Scavi superficiali o assenti", "disturbi_selezionati": [], "punti_disturbo": 0
 }

def reset_totale():
 st.session_state.micro_passo = "macro_area"
 st.session_state.indice_corrente = 0
 st.session_state.cronologia = []
 st.session_state.scelte = {
 "macro_area": None, "sottocategoria": None, "peso_habitat": 0,
 "flora_rilevata": [], "fauna_rilevata": [], "punti_suolo": 0, "suolo_testo": "",
 "punti_pendenza": 0, "pendenza_testo": "", "punti_idro": 0, "idro_testo": "",
 "punti_stato_acqua": 0, "stato_acqua_testo": "Non applicabile", "punti_opera": 0, "opera_testo": "",
 "punti_superficie": 0, "superficie_testo": "", "punti_altezza": 0, "altezza_testo": "",
 "punti_scavi": 15, "scavi_testo": "Scavi superficiali o assenti", "disturbi_selezionati": [], "punti_disturbo": 0
 }
 st.rerun()

def passo_precedente():
 if st.session_state.cronologia:
     stato_prec = st.session_state.cronologia.pop()
     st.session_state.micro_passo = stato_prec["micro_passo"]
     st.session_state.indice_corrente = stato_prec["indice_corrente"]
     st.rerun()

def salva_stato_cronologia():
 st.session_state.cronologia.append({
 "micro_passo": st.session_state.micro_passo,
 "indice_corrente": st.session_state.indice_corrente
 })

mp = st.session_state.micro_passo
idx = st.session_state.indice_corrente
# -------------------------------------------------------------------------
# INTERFACCIA GRAFICA SUPERIORE CONDIVISA (BARRA AVANZAMENTO E CONTROLLI)
# -------------------------------------------------------------------------
if mp != "risultato":
    # Genera la barra superiore neutra e isolata con pulsanti piccoli e affiancati
    st.markdown('<div class="barra-superiore-nav">', unsafe_allow_html=True)
    nav_col1, nav_col2 = st.columns([1, 4])
    with nav_col1:
        if st.button("Indietro", key="btn_nav_indietro", disabled=(len(st.session_state.cronologia) == 0)):
            passo_precedente()
    with nav_col2:
        if st.button("Reset", key="btn_nav_reset"):
            reset_totale()
    st.markdown('</div>', unsafe_allow_html=True)
    
    try:
        progresso = ELENCO_PASSI.index(mp) / (len(ELENCO_PASSI) - 1)
    except ValueError:
        progresso = 0.0
    st.progress(progresso)

# -------------------------------------------------------------------------
# NAVIGAZIONE ATOMICA / SCHERMATE DI SWIPE MOBILE
# -------------------------------------------------------------------------
# 1. SCELTA MACRO AREA
if mp == "macro_area":
    lista_macro = list(DATABASE_AMBIENTALE.keys())
    if idx >= len(lista_macro): idx = 0
    nome = lista_macro[idx]
    dati = DATABASE_AMBIENTALE[nome]
    
    st.caption(f"Filtro Contesto: Macro-Ambiente ({idx+1}/{len(lista_macro)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(dati["etichetta_img"])
    st.write(f"*{dati['descrizione']}*")
    
    # Riquadro pulsanti decisionali vincolati alla classe flex inferiore
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO", key=f"macro_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista_macro)
            st.rerun()
    with col2:
        if st.button("SI", key=f"macro_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["macro_area"] = nome
            st.session_state.micro_passo = "sottocategoria"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
# 2. SCELTA SOTTOCATEGORIA
elif mp == "sottocategoria":
    macro = st.session_state.scelte["macro_area"]
    lista_sotto = list(DATABASE_AMBIENTALE[macro]["sottocategorie"].keys())
    if idx >= len(lista_sotto): idx = 0
    nome = lista_sotto[idx]
    dati = DATABASE_AMBIENTALE[macro]["sottocategorie"][nome]
    
    st.caption(f"Dettaglio Specifica Habitat ({idx+1}/{len(lista_sotto)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(dati["etichetta_img"])
    st.write(f"*{dati['descrizione']}* (Vulnerabilita: {dati['peso_habitat']} pt)")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO", key=f"sotto_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista_sotto)
            st.rerun()
    with col2:
        if st.button("SI", key=f"sotto_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["sottocategoria"] = nome
            st.session_state.scelte["peso_habitat"] = dati["peso_habitat"]
            st.session_state.micro_passo = "flora"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 3. VALUTAZIONE SPECIE FLORA
elif mp == "flora":
    macro = st.session_state.scelte["macro_area"]
     sotto = st.session_state.scelte["sottocategoria"]
    lista_flora = DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["flora"]
    nome_sp, punti_sp, etichetta_img, desc = lista_flora[idx]
    
    st.caption(f"Rilevamento Specie Botaniche ({idx+1}/{len(lista_flora)})")
    st.markdown(f"### {nome_sp}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}* (Rilevanza: {punti_sp} pt)")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ASSENTE", key=f"flo_no_{idx}"):
            salva_stato_cronologia()
            if idx + 1 < len(lista_flora):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "fauna"
                st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("PRESENTE", key=f"flo_si_{idx}"):
            salva_stato_cronologia()
            if nome_sp not in st.session_state.scelte["flora_rilevata"]:
                st.session_state.scelte["flora_rilevata"].append(nome_sp)
            if idx + 1 < len(lista_flora):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "fauna"
                st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
# 4. VALUTAZIONE SPECIE FAUNA
elif mp == "fauna":
    macro = st.session_state.scelte["macro_area"]
    sotto = st.session_state.scelte["sottocategoria"]
    lista_fauna = DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["fauna"]
    nome_sp, punti_sp, etichetta_img, desc = lista_fauna[idx]
    
    st.caption(f"Rilevamento Fauna Locale ({idx+1}/{len(lista_fauna)})")
    st.markdown(f"### {nome_sp}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}* (Rilevanza: {punti_sp} pt)")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ASSENTE", key=f"fau_no_{idx}"):
            salva_stato_cronologia()
            if idx + 1 < len(lista_fauna):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "suolo"
                st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("PRESENTE", key=f"fau_si_{idx}"):
            salva_stato_cronologia()
            if nome_sp not in st.session_state.scelte["fauna_rilevata"]:
                st.session_state.scelte["fauna_rilevata"].append(nome_sp)
            if idx + 1 < len(lista_fauna):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "suolo"
                st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MATRICE FISICA - SUOLO
elif mp == "suolo":
    lista = MATRICI_FISICHE_EDILIZIE["suolo"]
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption(f"Tipo di Suolo Superficiale ({idx+1}/{len(lista)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"suo_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"suo_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_suolo"] = punti
            st.session_state.scelte["suolo_testo"] = nome
            st.session_state.micro_passo = "pendenza"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
# 6. MATRICE FISICA - OROGRAFIA E PENDENZA
elif mp == "pendenza":
    lista = MATRICI_FISICHE_EDILIZIE["pendenza"]
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption(f"Orografia e Pendenza ({idx+1}/{len(lista)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"pen_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"pen_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_pendenza"] = punti
            st.session_state.scelte["pendenza_testo"] = nome
            st.session_state.micro_passo = "idro"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 7. MATRICE FISICA - IDROGRAFIA
elif mp == "idro":
    lista = MATRICI_FISICHE_EDILIZIE["idro"]
    if idx >= len(lista):
        st.session_state.scelte["punti_idro"] = 0
        st.session_state.scelte["idro_testo"] = "Assente (Nessun corpo idrico entro 100m)"
        st.session_state.scelte["punti_stato_acqua"] = 0
        st.session_state.scelte["stato_acqua_testo"] = "Non applicabile (Idrografia assente)"
        st.session_state.micro_passo = "bivio_opera"
        st.session_state.indice_corrente = 0
        st.rerun()
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption(f"Verifica Presenza Idrica entro 100m ({idx+1}/{len(lista)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO", key=f"idr_no_{idx}"):
            st.session_state.indice_corrente += 1
            st.rerun()
    with col2:
        if st.button("SI / CONFERMA", key=f"idr_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_idro"] = punti
            st.session_state.scelte["idro_testo"] = nome
            st.session_state.micro_passo = "stato_acqua"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 8. MATRICE FISICA - STATO DELL'ACQUA
elif mp == "stato_acqua":
    lista = MATRICI_FISICHE_EDILIZIE["stato_acqua"]
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption("Stato Ecologico Qualitativo dell'Acqua")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO (Limpida/Buona)", key=f"sta_no_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_stato_acqua"] = 0
            st.session_state.scelte["stato_acqua_testo"] = "Nessuna anomalia evidente, acqua limpida"
            st.session_state.micro_passo = "bivio_opera"
            st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("SI (Compromessa)", key=f"sta_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_stato_acqua"] = punti
            st.session_state.scelte["stato_acqua_testo"] = nome
            st.session_state.micro_passo = "bivio_opera"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
# 9. BIVIO DI PROSEGUIMENTO VERSO IL CALCOLO DELL'OPERA
elif mp == "bivio_opera":
    st.caption("Fase di Caratterizzazione Ambientale Ultimata")
    st.markdown("### Vuoi proseguire con il calcolo dell'impatto dell'opera?")
    st.write("Selezionando SI inserirai i dati dell'infrastruttura e dei cantieri. Selezionando NO l'analisi ambientale verra conclusa subito.")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO", key="bivio_no"):
            salva_stato_cronologia()
            st.session_state.micro_passo = "risultato"
            st.session_state.indice_corrente = 999
            st.rerun()
    with col2:
        if st.button("SI", key="bivio_si"):
            salva_stato_cronologia()
            st.session_state.micro_passo = "opera"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 10. CARATTERISTICHE OPERA - CATEGORIA EDILIZIA
elif mp == "opera":
    lista = MATRICI_FISICHE_EDILIZIE["opera"]
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption(f"Tipologia Strutturale dell'Opera Edilizia ({idx+1}/{len(lista)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etchetta_img if 'etchetta_img' in locals() else etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"ope_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"ope_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_opera"] = punti
            st.session_state.scelte["opera_testo"] = nome
            st.session_state.micro_passo = "superficie"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 11. CARATTERISTICHE OPERA - SUPERFICIE PROGETTO
elif mp == "superficie":
    lista = MATRICI_FISICHE_EDILIZIE["superficie"]
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption(f"Estensione Area Impermeabilizzata ({idx+1}/{len(lista)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"sup_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"sup_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_superficie"] = punti
            st.session_state.scelte["superficie_testo"] = nome
            st.session_state.micro_passo = "altezza"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
# 12. CARATTERISTICHE OPERA - ELEVAZIONE (ALTEZZA)
elif mp == "altezza":
    lista = MATRICI_FISICHE_EDILIZIE["altezza"]
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption(f"Sviluppo Verticale Massimo Fuori Terra ({idx+1}/{len(lista)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"alt_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"alt_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_altezza"] = punti
            st.session_state.scelte["altezza_testo"] = nome
            st.session_state.micro_passo = "scavi"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 13. CARATTERISTICHE OPERA - INVASIVITA SCAVI
elif mp == "scavi":
    lista = MATRICI_FISICHE_EDILIZIE["scavi"]
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption("Invasivita Ipogea e Struttura delle Fondazioni")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO (Scavi Superficiali)", key=f"sca_no_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_scavi"] = 15
            st.session_state.scelte["scavi_testo"] = "Scavi superficiali o assenti"
            st.session_state.micro_passo = "disturbi"
            st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("SI (Scavi Profondi)", key=f"sca_si_{idx}"):
            salva_stato_cronologia()
            st.session_state.scelte["punti_scavi"] = punti
            st.session_state.scelte["scavi_testo"] = nome
            st.session_state.micro_passo = "disturbi"
            st.session_state.indice_corrente = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 14. FATTORI DI DISTURBO DEL CANTIERE
elif mp == "disturbi":
    lista = MATRICI_FISICHE_EDILIZIE["disturbi"]
    if idx >= len(lista):
        st.session_state.scelte["punti_disturbo"] = len(st.session_state.scelte["disturbi_selezionati"]) * 25
        st.session_state.micro_passo = "risultato"
        st.session_state.indice_corrente = 0
        st.rerun()
    nome, punti, etichetta_img, desc = lista[idx]
    
    st.caption(f"Sorgenti di Pressione Antropica in Cantiere ({idx+1}/{len(lista)})")
    st.markdown(f"### {nome}")
    mostra_box_immagine(etichetta_img)
    st.write(f"*{desc}*")
    
    st.markdown('<div class="riga-pulsanti-flex">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ASSENTE", key=f"dis_no_{idx}"):
            salva_stato_cronologia()
            st.session_state.indice_corrente += 1
            st.rerun()
    with col2:
        if st.button("PRESENTE", key=f"dis_si_{idx}"):
            salva_stato_cronologia()
            if nome not in st.session_state.scelte["disturbi_selezionati"]:
                st.session_state.scelte["disturbi_selezionati"].append(nome)
            st.session_state.indice_corrente += 1
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
# 15. SCHERMATA FINALE CON REPORT
elif mp == "risultato":
    if st.session_state.indice_corrente == 999:
        st.success("AMBIENTE CARATTERIZZATO!")
        st.write("Analisi conclusa raccogliendo soltanto i dati della sensibilita ecologica locale.")
        
        with st.expander("Visualizza Dati Ambientali Salvati"):
            st.write(f"**Macro-area:** {st.session_state.scelte['macro_area']}")
            st.write(f"**Sottocategoria:** {st.session_state.scelte['sottocategoria']}")
            st.write(f"**Flora:** {', '.join(st.session_state.scelte['flora_rilevata']) if st.session_state.scelte['flora_rilevata'] else 'Nessuna'}")
            st.write(f"**Fauna:** {', '.join(st.session_state.scelte['fauna_rilevata']) if st.session_state.scelte['fauna_rilevata'] else 'Nessuna'}")
            st.write(f"**Suolo:** {st.session_state.scelte['suolo_testo']}")
            st.write(f"**Orografia:** {st.session_state.scelte['pendenza_testo']}")
            st.write(f"**Idrografia:** {st.session_state.scelte['idro_testo']}")
    else:
        st.markdown("### Valutazione dell'Impatto Ecologico")
        macro = st.session_state.scelte["macro_area"]
        sotto = st.session_state.scelte["sottocategoria"]
        
        lista_flora_rif = {nome: pt for nome, pt, _, _ in DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["flora"]}
        lista_fauna_rif = {nome: pt for nome, pt, _, _ in DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["fauna"]}
        
        punti_base_s = 20
        punti_habitat = st.session_state.scelte["peso_habitat"]
        flora_scelta = st.session_state.scelte["flora_rilevata"]
        punti_flora = 8 if len(flora_scelta) == 0 else sum(lista_flora_rif.get(sp, 0) for sp in flora_scelta)
        fauna_scelta = st.session_state.scelte["fauna_rilevata"]
        punti_fauna = 8 if len(fauna_scelta) == 0 else sum(lista_fauna_rif.get(sp, 0) for sp in fauna_scelta)
        
        punti_suolo = st.session_state.scelte["punti_suolo"]
        punti_pendenza = st.session_state.scelte["punti_pendenza"]
        punti_idro = st.session_state.scelte["punti_idro"]
        punti_stato_acqua = st.session_state.scelte["punti_stato_acqua"]
        
        punti_s_totale = punti_base_s + punti_habitat + punti_flora + punti_fauna + punti_suolo + punti_pendenza + punti_idro + punti_stato_acqua
        s_normalizzato = min((punti_s_totale / 225.0) * 100.0, 100.0)
        
        punti_opera = st.session_state.scelte["punti_opera"]
        punti_superficie = st.session_state.scelte["punti_superficie"]
        punti_altezza = st.session_state.scelte["punti_altezza"]
        punti_scavi = st.session_state.scelte["punti_scavi"]
        
        punti_d_totale = punti_opera + punti_superficie + punti_altezza + punti_scavi
        d_normalizzato = min((punti_d_totale / 120.0) * 100.0, 100.0)
        
        punti_p_totale = st.session_state.scelte["punti_disturbo"]
        p_normalizzato = min((punti_p_totale / 75.0) * 100.0, 100.0)
        
        punteggio_finale = (s_normalizzato * 0.40) + (d_normalizzato * 0.45) + (p_normalizzato * 0.15)
        
        if punteggio_finale < 40.0:
            stato_impatto = "IMPATTO BASSO"
            colore_stato = "green"
        elif punteggio_finale < 70.0:
            stato_impatto = "IMPATTO MODERATO"
            colore_stato = "orange"
        else:
            stato_impatto = "IMPATTO CRITICO"
            colore_stato = "red"
        
        st.subheader(f"Punteggio Finale: {punteggio_finale:.1f} / 100")
        st.markdown(f"Stato di Allerta Ecologica: <span style='color:{colore_stato}; font-weight:bold; font-size:20px;'>{stato_impatto}</span>", unsafe_allow_html=True)
        st.write("---")
        st.write(f"Sensibilita Territoriale (S): {s_normalizzato:.1f} / 100")
        st.write(f"Impronta Strutturale (D): {d_normalizzato:.1f} / 100")
        st.write(f"Disturbo Fase Cantiere (P): {p_normalizzato:.1f} / 100")
        st.write("---")

    if st.button("Inizia una Nuova Valutazione", use_container_width=True, key="btn_ricomincia_finale"):
        reset_totale()
