import streamlit as st

# Configurazione della pagina Streamlit per dispositivi mobili
st.set_page_config(page_title="EcoRischio Liguria", page_icon="🌿", layout="centered")

# CSS personalizzato per eliminare i ritardi e ingrandire i pulsanti touch su smartphone
st.markdown("""
<style>
    div.stButton > button {
        width: 100% !important;
        height: 60px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
    }
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# DATABASE AMBIENTALE LIGURE ORIGINALE INTEGRALE
# -------------------------------------------------------------------------
DATABASE_AMBIENTALE = {
    "Ambiente Costiero e Marino": {
        "immagine": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500",
        "descrizione": "Contesto marino, litorali sabbiosi e scogliere della Liguria.",
        "sottocategorie": {
            "Ambiente Marino Subacqueo": {
                "peso_habitat": 40,
                "immagine": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500",
                "descrizione": "Fondali marini e praterie sommerse.",
                "flora": [
                    ("Ulva lactuca", 5, "https://images.unsplash.com/photo-1546026423-cc4642628d2b?w=500", "Lattuga di mare (alga verde comune)."),
                    ("Padina pavonica", 5, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500", "Alga a coda di pavone."),
                    ("Posidonia oceanica", 15, "http://googleusercontent.com/image_collection/image_retrieval/8105213215481325883_0", "Pianta marina protetta fondamentale per l'ecosistema."),
                    ("Cymodocea nodosa", 15, "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500", "Erba marina che forma praterie su sabbia.")
                ],
                "fauna": [
                    ("Coris julis", 5, "https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?w=500", "Donzella, pesce colorato di scogliera."),
                    ("Octopus vulgaris", 5, "https://images.unsplash.com/photo-1545671913-b89ac1b4ac10?w=500", "Polpo comune."),
                    ("Pinna nobilis", 15, "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500", "Nacchera di mare, grande mollusco bivalve protetto."),
                    ("Hippocampus hippocampus", 15, "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?w=500", "Cavalluccio marino.")
                ]
            },
            "Costa Rocciosa e Scogliere": {
                "peso_habitat": 35,
                "immagine": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500",
                "descrizione": "Scarpate rocciose marine e zone sopralitorali.",
                "flora": [
                    ("Crithmum maritimum", 5, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500", "Finocchio marino."),
                    ("Limonium vulgare", 5, "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?w=500", "Campanella delle spiagge / Limonio."),
                    ("Campanula sabatia", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Campanula di Savona, endemismo ligure protetto."),
                    ("Centaurea paniculata", 15, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Fiordaliso sfiocchettato.")
                ],
                "fauna": [
                    ("Pachygrapsus marmoratus", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Granchio corridore delle scogliere."),
                    ("Podarcis muralis", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Lucertola muraiola."),
                    ("Gulosus aristotelis", 15, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Marangone dal ciuffo (uccello marino)."),
                    ("Falco peregrinus", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Falco pellegrino.")
                ]
            },
            "Litorale Sabbioso e Chiotto (Spiagge)": {
                "peso_habitat": 30,
                "immagine": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500",
                "descrizione": "Arenili e depositi ciottolosi costieri.",
                "flora": [
                    ("Cakile maritima", 5, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500", "Ravastrello marittimo."),
                    ("Medicago marina", 5, "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?w=500", "Erba medica marina."),
                    ("Pancratium maritimum", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Giglio marino delle dune."),
                    ("Eryngium maritimum", 15, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Calcatreppola marina.")
                ],
                "fauna": [
                    ("Talitrus saltator", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Pulce di mare."),
                    ("Theba pisana", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Chiocciolina delle sabbie."),
                    ("Charadrius dubius", 15, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Corriere piccolo."),
                    ("Charadrius alexandrinus", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Corriere fratino, volatile protetto delle dune.")
                ]
            }
        }
    },
    "Ambiente d'Acqua Dolce e Umido": {
        "immagine": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500",
        "descrizione": "Rivi, torrenti, fiumare e specchi palustri.",
        "sottocategorie": {
            "Zone Umide, Laghi e Zone Palustri": {
                "peso_habitat": 35,
                "immagine": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500",
                "descrizione": "Acque ferme, paludi e laghetti d'alta quota.",
                "flora": [
                    ("Phragmites australis", 5, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Canna di palude."),
                    ("Typha latifolia", 5, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Mazza di sorda / Tifa."),
                    ("Drosera rotundifolia", 15, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Pianta carnivora delle torbiere liguri."),
                    ("Adiantum capillus-veneris", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Capelvenere, felce di ambienti umidi sgocciolanti.")
                ],
                "fauna": [
                    ("Pelophylax esculentus", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Rana verde comune."),
                    ("Anax imperator", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Libellula imperatore."),
                    ("Speleomantes strinatii", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Geotritone di Strinati, anfibio endemico protetto."),
                    ("Bombina variegata", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Ululone dal ventre giallo.")
                ]
            },
            "Corsi d'Acqua (Rivi, Torrenti e Fiumare)": {
                "peso_habitat": 30,
                "immagine": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500",
                "descrizione": "Rete idrografica superficiale corrente.",
                "flora": [
                    ("Apium nodiflorum", 5, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Sedano d'acqua."),
                    ("Mentha spicata", 5, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Menta selvatica."),
                    ("Adiantum capillus-veneris", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Felce capelvenere."),
                    ("Ranunculus aquatilis", 15, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Ranuncolo d'acqua flottante.")
                ],
                "fauna": [
                    ("Potamon fluviatile", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Granchio di fiume d'acqua dolce."),
                    ("Hierophis viridiflavus", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Biacco (serpente innocuo comune)."),
                    ("Salmo trutta", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Trota fario autoctona."),
                    ("Alcedo atthis", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Martino pescatore.")
                ]
            }
        }
    },
    "Ambiente Forestale e Boschivo": {
        "immagine": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500",
        "descrizione": "Boschi montani, macchia litoranea e formazioni collinari.",
        "sottocategorie": {
            "Boschi Montani di Conifere e Faggete": {
                "peso_habitat": 30,
                "immagine": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500",
                "descrizione": "Faggete interne e foreste di alta quota alpine o appenniniche.",
                "flora": [
                    ("Fagus sylvatica", 5, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Faggio comune."),
                    ("Vaccinium myrtillus", 5, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Mirtillo nero."),
                    ("Ilex aquifolium", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Agrifoglio spontaneo protetto."),
                    ("Taxus baccata", 15, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Tasso, relitto glaciale protetto.")
                ],
                "fauna": [
                    ("Sus scrofa", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Cinghiale europeo."),
                    ("Sciurus vulgaris", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Scoiattolo rosso comune."),
                    ("Canis lupus", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Lupo appenninico."),
                    ("Speleomantes strinatii", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Geotritone di Strinati.")
                ]
            },
            "Macchia Mediterranea e Boschi Costieri": {
                "peso_habitat": 25,
                "immagine": "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?w=500",
                "descrizione": "Arbusteti densi, leccete costiere e pinete marittime.",
                "flora": [
                    ("Pistacia lentiscus", 5, "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?w=500", "Lentisco."),
                    ("Olea europaea", 5, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Olivo selvatico / Oleastro."),
                    ("Chamaerops humilis", 15, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500", "Palma nana mediterranea spontanea."),
                    ("Arbutus unedo", 15, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Corbezzolo.")
                ],
                "fauna": [
                    ("Sus scrofa", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Cinghiale."),
                    ("Tarentola mauritanica", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Geco comune."),
                    ("Timon lepidus", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Lucertola ocellata, il piu grande sauro europeo."),
                    ("Testudo hermanni", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Tartaruga di terra protetta.")
                ]
            },
            "Boschi di Latifoglie Decidue (Fascia Collinare)": {
                "peso_habitat": 20,
                "immagine": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500",
                "descrizione": "Castagneti, cerrete e boschi misti collinari.",
                "flora": [
                    ("Castanea sativa", 5, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Castagno."),
                    ("Quercus pubescens", 5, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Roverella."),
                    ("Anemone nemorosa", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Anemone dei boschi."),
                    ("Paeonia officinalis", 15, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Peonia selvatica protetta.")
                ],
                "fauna": [
                    ("Sus scrofa", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Cinghiale."),
                    ("Podarcis muralis", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Lucertola muraiola."),
                    ("Lucanus cervus", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Cervo volante, coleottero protetto europeo."),
                    ("Hierophis viridiflavus", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Biacco.")
                ]
            }
        }
    },
    "Ambiente Montano Alto e Rupestre": {
        "immagine": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500",
        "descrizione": "Cime, ghiaioni alpini, pascoli e pareti rocciose.",
        "sottocategorie": {
            "Ambienti Rupestri e Ghiaioni d'Alta Quota": {
                "peso_habitat": 30,
                "immagine": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500",
                "descrizione": "Pareti di roccia nuda e sfasciumi d'alta quota.",
                "flora": [
                    ("Sempervivum arachnoideum", 5, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Semprevivo ragnatelo."),
                    ("Sedum acre", 5, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Borracina acre."),
                    ("Primula allionii", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Primula di Allioni, rarissimo endemismo rupicolo."),
                    ("Campanula sabatia", 15, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Campanula ligure.")
                ],
                "fauna": [
                    ("Podarcis muralis", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Lucertola muraiola."),
                    ("Prunella collaris", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Sordone (uccello d'alta quota)."),
                    ("Aquila chrysaetos", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Aquila reale."),
                    ("Falco peregrinus", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Falco pellegrino.")
                ]
            },
            "Praterie di Altitudine e Pascoli": {
                "peso_habitat": 25,
                "immagine": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500",
                "descrizione": "Praterie naturali sopra il limite degli alberi.",
                "flora": [
                    ("Trifolium alpinum", 5, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Trifoglio alpino."),
                    ("Tarassaco montano", 5, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Tarassaco di montagna."),
                    ("Narcissus poeticus", 15, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Narciso selvatico protetto."),
                    ("Viola bertolonii", 15, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Viola di Bertoloni, endemismo ligure-provenzale.")
                ],
                "fauna": [
                    ("Chionomys nivalis", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Arvicola delle nevi."),
                    ("Falco tinnunculus", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Gheppio."),
                    ("Vipera ursinii", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Vipera dell'Orsini, specie rarissima e iper-protetta."),
                    ("Anthus campestris", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Calandro.")
                ]
            }
        }
    },
    "Ambiente Antropizzato e Agricolo": {
        "immagine": "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500",
        "descrizione": "Zone urbane, fasce terrazzate, oliveti storici liguri.",
        "sottocategorie": {
            "Terrazzamenti, Oliveti e Vigneti / Zone Urbane": {
                "peso_habitat": 15,
                "immagine": "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500",
                "descrizione": "Muretti a secco tradizionali e insediamenti rurali o urbani.",
                "flora": [
                    ("Olea europaea", 5, "https://images.unsplash.com/photo-1596722240538-4e899201a0bc?w=500", "Olivo coltivato."),
                    ("Parietaria officinalis", 5, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Erba vetriola delle mura."),
                    ("Anacamptis pyramidalis", 15, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Orchidea piramidale selvatica protetta."),
                    ("Capparis spinosa", 15, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Pianta del cappero delle vecchie mura.")
                ],
                "fauna": [
                    ("Sus scrofa", 5, "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?w=500", "Cinghiale urbano."),
                    ("Tarentola mauritanica", 5, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Geco dei muretti."),
                    ("Pipistrellus kuhlii", 15, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Pipistrello albolimbato."),
                    ("Euplagia quadripunctaria", 15, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Falena dell'edera (Specie protetta Direttiva Habitat).")
                ]
            }
        }
    }
}

# -------------------------------------------------------------------------
# MATRICI OPERA E MATRICI FISICHE ATOMICHE (SI / NO)
# -------------------------------------------------------------------------
MATRICI_FISICHE_EDILIZIE = {
    "suolo": [
        ("Terreno sabbioso o roccia compatta", 0, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500", "Basso rischio di compattamento."),
        ("Terreno limoso o argilloso", 15, "https://images.unsplash.com/photo-1576086213369-97a306dca664?w=500", "Rischio moderato di fango e instabilita."),
        ("Humus fertile, organico o forestale", 20, "https://images.unsplash.com/photo-1448375240586-882707db888b?w=500", "Alto valore ecologico e rischio erosione.")
    ],
    "pendenza": [
        ("Terreno pianeggiante o debole pendenza (inferiore a 15 gradi)", 0, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500", "Bassa suscettibilita al dissesto."),
        ("Forte pendenza, versante o scarpata (superiore a 15 gradi)", 25, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500", "Versante instabile ad alto rischio.")
    ],
    "idro": [
        ("Presenza di fossi di scolo, canali artificiali o rii temporanei?", 10, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500", "Rileva corsi idrici minori stagionali."),
        ("Presenza di ruscelli, torrenti, fiumi perenni o specchi d'acqua?", 25, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500", "Presenza idrica perenne stabile entro 100m.")
    ],
    "stato_acqua": [
        ("Corpo idrico visibilmente compromesso (scarichi, rifiuti, torbidita)?", 15, "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=500", "Seleziona SI se la qualita dell'acqua e alterata.")
    ],
    "opera": [
        ("Manufatto leggero o temporaneo (legno, chioschi, recinzioni pesanti)", 15, "https://images.unsplash.com/photo-1546484475-7f7bd55792da?w=500", "Basso impatto fisico volumetrico."),
        ("Edifici civili o industriali (abitazioni, uffici, parcheggi interrati)", 30, "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=500", "Impatto strutturale permanente medio-alto."),
        ("Infrastrutture pesanti o lineari (strade, ponti, gallerie, grandi muri)", 40, "https://images.unsplash.com/photo-1545558014-8687977e99a5?w=500", "Massimo impatto per modificazione dell'assetto del suolo.")
    ],
    "superficie": [
        ("Superficie ridotta (inferiore a 100 metri quadri)", 0, "https://images.unsplash.com/photo-1546844755-7f7bd55792da?w=500", "Minima area impermeabilizzata."),
        ("Superficie media (compresa tra 100 e 500 metri quadri)", 15, "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=500", "Modifica planimetrica standard."),
        ("Superficie estesa (superiore a 500 metri quadri)", 30, "https://images.unsplash.com/photo-1545558014-8687977e99a5?w=500", "Ampia impronta di cantiere e impermeabilizzazione.")
    ],
    "altezza": [
        ("Altezza minima fuori terra (inferiore a 3 metri)", 0, "https://images.unsplash.com/photo-1546484475-7f7bd55792da?w=500", "Sviluppo verticale trascurabile."),
        ("Altezza moderata fuori terra (compresa tra 3 e 7 metri)", 10, "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=500", "Impatto visivo o faunistico medio."),
        ("Altezza rilevante fuori terra (superiore a 7 metri)", 20, "https://images.unsplash.com/photo-1545558014-8687977e99a5?w=500", "Forte impatto verticale permanente.")
    ],
    "scavi": [
        ("Scavi profondi o invasivi (fondazioni complesse, pali, tiranti, sotterranei)", 30, "https://images.unsplash.com/photo-1576086213369-97a306dca664?w=500", "Forte alterazione degli strati profondi geologici. (Se NO = punti 15).")
    ],
    "disturbi": [
        ("Logistica di cantiere pesante (transito frequente mezzi, stoccaggio)", 25, "https://images.unsplash.com/photo-1545558014-8687977e99a5?w=500", "Disturbo logistico temporaneo."),
        ("Rumori continui o impulsivi (demolizioni, scavi meccanici, perforazioni)", 25, "https://images.unsplash.com/photo-1576086213369-97a306dca664?w=500", "Disturbo acustico."),
        ("Inquinamento luminoso (illuminazione notturna di cantiere o esercizio)", 25, "https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?w=500", "Disturbo fotometrico della fauna notturna.")
    ]
}

# -------------------------------------------------------------------------
# INIZIALIZZAZIONE DELLA SESSIONE IN MICRO-PASSI REATTIVI
# -------------------------------------------------------------------------
if "micro_passo" not in st.session_state:
    st.session_state.micro_passo = "macro_area"
if "indice_corrente" not in st.session_state:
    st.session_state.indice_corrente = 0
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
    st.session_state.scelte = {
        "macro_area": None, "sottocategoria": None, "peso_habitat": 0,
        "flora_rilevata": [], "fauna_rilevata": [], "punti_suolo": 0, "suolo_testo": "",
        "punti_pendenza": 0, "pendenza_testo": "", "punti_idro": 0, "idro_testo": "",
        "punti_stato_acqua": 0, "stato_acqua_testo": "Non applicabile", "punti_opera": 0, "opera_testo": "",
        "punti_superficie": 0, "superficie_testo": "", "punti_altezza": 0, "altezza_testo": "",
        "punti_scavi": 15, "scavi_testo": "Scavi superficiali o assenti", "disturbi_selezionati": [], "punti_disturbo": 0
    }
    st.rerun()

# Configurazione Barra Laterale Rapida
st.sidebar.title("EcoRischio Liguria")
st.sidebar.caption(f"Fase Attuale: {st.session_state.micro_passo.upper()}")
if st.sidebar.button("Inizia nuova analisi"):
    reset_totale()

mp = st.session_state.micro_passo
idx = st.session_state.indice_corrente

# -------------------------------------------------------------------------
# NAVIGAZIONE ATOMICA SI / NO (SWIPE STYLE)
# -------------------------------------------------------------------------

# 1. SCELTA MACRO AREA
if mp == "macro_area":
    lista_macro = list(DATABASE_AMBIENTALE.keys())
    if idx >= len(lista_macro): idx = 0
    
    nome = lista_macro[idx]
    dati = DATABASE_AMBIENTALE[nome]
    
    st.caption(f"Filtro Contesto: Macro-Ambiente ({idx+1}/{len(lista_macro)})")
    st.header(nome)
    st.image(dati["immagine"], use_container_width=True)
    st.subheader(dati["descrizione"])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO", key=f"macro_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista_macro)
            st.rerun()
    with col2:
        if st.button("SI", key=f"macro_si_{idx}"):
            st.session_state.scelte["macro_area"] = nome
            st.session_state.micro_passo = "sottocategoria"
            st.session_state.indice_corrente = 0
            st.rerun()

# 2. SCELTA SOTTOCATEGORIA
elif mp == "sottocategoria":
    macro = st.session_state.scelte["macro_area"]
    lista_sotto = list(DATABASE_AMBIENTALE[macro]["sottocategorie"].keys())
    if idx >= len(lista_sotto): idx = 0
    
    nome = lista_sotto[idx]
    dati = DATABASE_AMBIENTALE[macro]["sottocategorie"][nome]
    
    st.caption(f"Dettaglio Specifica Habitat ({idx+1}/{len(lista_sotto)})")
    st.header(nome)
    st.image(dati["immagine"], use_container_width=True)
    st.subheader(dati["descrizione"])
    st.caption(f"Punti Vulnerabilita Habitat Intrinseca: {dati['peso_habitat']} pt")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO", key=f"sotto_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista_sotto)
            st.rerun()
    with col2:
        if st.button("SI", key=f"sotto_si_{idx}"):
            st.session_state.scelte["sottocategoria"] = nome
            st.session_state.scelte["peso_habitat"] = dati["peso_habitat"]
            st.session_state.micro_passo = "flora"
            st.session_state.indice_corrente = 0
            st.rerun()

# 3. VALUTAZIONE SPECIE FLORA
elif mp == "flora":
    macro = st.session_state.scelte["macro_area"]
    sotto = st.session_state.scelte["sottocategoria"]
    lista_flora = DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["flora"]
    
    nome_sp, punti_sp, img, desc = lista_flora[idx]
    
    st.caption(f"Rilevamento Specie Botaniche ({idx+1}/{len(lista_flora)})")
    st.header(nome_sp)
    st.image(img, use_container_width=True)
    st.write(f"*{desc}*")
    st.caption(f"Rilevanza Ecologica Specie: {punti_sp} pt")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ASSENTE", key=f"flo_no_{idx}"):
            if idx + 1 < len(lista_flora):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "fauna"
                st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("PRESENTE", key=f"flo_si_{idx}"):
            if nome_sp not in st.session_state.scelte["flora_rilevata"]:
                st.session_state.scelte["flora_rilevata"].append(nome_sp)
            if idx + 1 < len(lista_flora):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "fauna"
                st.session_state.indice_corrente = 0
            st.rerun()

# 4. VALUTAZIONE SPECIE FAUNA
elif mp == "fauna":
    macro = st.session_state.scelte["macro_area"]
    sotto = st.session_state.scelte["sottocategoria"]
    lista_fauna = DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["fauna"]
    
    nome_sp, punti_sp, img, desc = lista_fauna[idx]
    
    st.caption(f"Rilevamento Fauna Locale ({idx+1}/{len(lista_fauna)})")
    st.header(nome_sp)
    st.image(img, use_container_width=True)
    st.write(f"*{desc}*")
    st.caption(f"Rilevanza Ecologica Specie: {punti_sp} pt")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ASSENTE", key=f"fau_no_{idx}"):
            if idx + 1 < len(lista_fauna):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "suolo"
                st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("PRESENTE", key=f"fau_si_{idx}"):
            if nome_sp not in st.session_state.scelte["fauna_rilevata"]:
                st.session_state.scelte["fauna_rilevata"].append(nome_sp)
            if idx + 1 < len(lista_fauna):
                st.session_state.indice_corrente += 1
            else:
                st.session_state.micro_passo = "suolo"
                st.session_state.indice_corrente = 0
            st.rerun()

# 5. MATRICE FISICA - SUOLO
elif mp == "suolo":
    lista = MATRICI_FISICHE_EDILIZIE["suolo"]
    nome, punti, img, desc = lista[idx]
    
    st.caption(f"Tipo di Suolo Superficiale di Cantiere ({idx+1}/{len(lista)})")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"suo_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"suo_si_{idx}"):
            st.session_state.scelte["punti_suolo"] = punti
            st.session_state.scelte["suolo_testo"] = nome
            st.session_state.micro_passo = "pendenza"
            st.session_state.indice_corrente = 0
            st.rerun()

# 6. MATRICE FISICA - OROGRAFIA E PENDENZA
elif mp == "pendenza":
    lista = MATRICI_FISICHE_EDILIZIE["pendenza"]
    nome, punti, img, desc = lista[idx]
    
    st.caption(f"Orografia e Pendenza Versante ({idx+1}/{len(lista)})")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"pen_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"pen_si_{idx}"):
            st.session_state.scelte["punti_pendenza"] = punti
            st.session_state.scelte["pendenza_testo"] = nome
            st.session_state.micro_passo = "idro"
            st.session_state.indice_corrente = 0
            st.rerun()

# 7. MATRICE FISICA - IDROGRAFIA
elif mp == "idro":
    lista = MATRICI_FISICHE_EDILIZIE["idro"]
    
    if idx >= len(lista):
        st.session_state.scelte["punti_idro"] = 0
        st.session_state.scelte["idro_testo"] = "Assente (Nessun corpo idrico entro 100m)"
        st.session_state.scelte["punti_stato_acqua"] = 0
        st.session_state.scelte["stato_acqua_testo"] = "Non applicabile (Idrografia assente)"
        st.session_state.micro_passo = "opera"
        st.session_state.indice_corrente = 0
        st.rerun()
        
    nome, punti, img, desc = lista[idx]
    
    st.caption(f"Verifica Presenza Idrica entro 100m ({idx+1}/{len(lista)})")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO", key=f"idr_no_{idx}"):
            st.session_state.indice_corrente += 1
            st.rerun()
    with col2:
        if st.button("SI / CONFERMA", key=f"idr_si_{idx}"):
            st.session_state.scelte["punti_idro"] = punti
            st.session_state.scelte["idro_testo"] = nome
            st.session_state.micro_passo = "stato_acqua"
            st.session_state.indice_corrente = 0
            st.rerun()

# 8. MATRICE FISICA - STATO DELL'ACQUA
elif mp == "stato_acqua":
    lista = MATRICI_FISICHE_EDILIZIE["stato_acqua"]
    nome, punti, img, desc = lista[idx]
    
    st.caption("Stato Ecologico Qualitativo dell'Acqua")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO (Limpida/Buona)", key=f"sta_no_{idx}"):
            st.session_state.scelte["punti_stato_acqua"] = 0
            st.session_state.scelte["stato_acqua_testo"] = "Nessuna anomalia evidente, acqua limpida"
            st.session_state.micro_passo = "opera"
            st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("SI (Compromessa)", key=f"sta_si_{idx}"):
            st.session_state.scelte["punti_stato_acqua"] = punti
            st.session_state.scelte["stato_acqua_testo"] = nome
            st.session_state.micro_passo = "opera"
            st.session_state.indice_corrente = 0
            st.rerun()

# 9. CARATTERISTICHE OPERA - CATEGORIA EDILIZIA
elif mp == "opera":
    lista = MATRICI_FISICHE_EDILIZIE["opera"]
    nome, punti, img, desc = lista[idx]
    
    st.caption(f"Tipologia Strutturale dell'Opera Edilizia ({idx+1}/{len(lista)})")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"ope_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"ope_si_{idx}"):
            st.session_state.scelte["punti_opera"] = punti
            st.session_state.scelte["opera_testo"] = nome
            st.session_state.micro_passo = "superficie"
            st.session_state.indice_corrente = 0
            st.rerun()

# 10. CARATTERISTICHE OPERA - SUPERFICIE PROGETTO
elif mp == "superficie":
    lista = MATRICI_FISICHE_EDILIZIE["superficie"]
    nome, punti, img, desc = lista[idx]
    
    st.caption(f"Estensione Area Modificata/Impermeabilizzata ({idx+1}/{len(lista)})")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"sup_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"sup_si_{idx}"):
            st.session_state.scelte["punti_superficie"] = punti
            st.session_state.scelte["superficie_testo"] = nome
            st.session_state.micro_passo = "altezza"
            st.session_state.indice_corrente = 0
            st.rerun()

# 11. CARATTERISTICHE OPERA - ELEVAZIONE (ALTEZZA)
elif mp == "altezza":
    lista = MATRICI_FISICHE_EDILIZIE["altezza"]
    nome, punti, img, desc = lista[idx]
    
    st.caption(f"Sviluppo Verticale Massimo Fuori Terra ({idx+1}/{len(lista)})")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ALTRO", key=f"alt_no_{idx}"):
            st.session_state.indice_corrente = (idx + 1) % len(lista)
            st.rerun()
    with col2:
        if st.button("CONFERMA", key=f"alt_si_{idx}"):
            st.session_state.scelte["punti_altezza"] = punti
            st.session_state.scelte["altezza_testo"] = nome
            st.session_state.micro_passo = "scavi"
            st.session_state.indice_corrente = 0
            st.rerun()

# 12. CARATTERISTICHE OPERA - INVASIVITA SCAVI
elif mp == "scavi":
    lista = MATRICI_FISICHE_EDILIZIE["scavi"]
    nome, punti, img, desc = lista[idx]
    
    st.caption("Invasivita Ipogea e Struttura delle Fondazioni")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("NO (Scavi Superficiali)", key=f"sca_no_{idx}"):
            st.session_state.scelte["punti_scavi"] = 15
            st.session_state.scelte["scavi_testo"] = "Scavi superficiali o assenti (Senza alterazione geologica)"
            st.session_state.micro_passo = "disturbi"
            st.session_state.indice_corrente = 0
            st.rerun()
    with col2:
        if st.button("SI (Scavi Profondi)", key=f"sca_si_{idx}"):
            st.session_state.scelte["punti_scavi"] = punti
            st.session_state.scelte["scavi_testo"] = nome
            st.session_state.micro_passo = "disturbi"
            st.session_state.indice_corrente = 0
            st.rerun()

# 13. FATTORI DI DISTURBO DEL CANTIERE
elif mp == "disturbi":
    lista = MATRICI_FISICHE_EDILIZIE["disturbi"]
    
    if idx >= len(lista):
        st.session_state.scelte["punti_disturbo"] = len(st.session_state.scelte["disturbi_selezionati"]) * 25
        st.session_state.micro_passo = "risultato"
        st.session_state.indice_corrente = 0
        st.rerun()
        
    nome, punti, img, desc = lista[idx]
    
    st.caption(f"Sorgenti di Pressione Antropica Attive in Cantiere ({idx+1}/{len(lista)})")
    st.header(nome)
    st.image(img, use_container_width=True)
    st.write(desc)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ASSENTE", key=f"dis_no_{idx}"):
            if idx + 1 <= len(lista):
                st.session_state.indice_corrente += 1
                st.rerun()
    with col2:
        if st.button("PRESENTE", key=f"dis_si_{idx}"):
            if nome not in st.session_state.scelte["disturbi_selezionati"]:
                st.session_state.scelte["disturbi_selezionati"].append(nome)
            st.session_state.indice_corrente += 1
            st.rerun()

# 14. SCHERMATA FINALE CON CALCOLO MATEMATICO ESATTO
elif mp == "risultato":
    st.header("14. Valutazione dell'Impatto Ecologico")
    
    macro = st.session_state.scelte["macro_area"]
    sotto = st.session_state.scelte["sottocategoria"]
    
    lista_flora_rif = {nome: pt for nome, pt, _, _ in DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["flora"]}
    lista_fauna_rif = {nome: pt for nome, pt, _, _ in DATABASE_AMBIENTALE[macro]["sottocategorie"][sotto]["fauna"]}
    
    # --- CALCOLO INDICE S (SENSIBILITA) ---
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
    
    # --- CALCOLO INDICE D (IMPRONTA EDIFICIO) ---
    punti_opera = st.session_state.scelte["punti_opera"]
    punti_superficie = st.session_state.scelte["punti_superficie"]
    punti_altezza = st.session_state.scelte["punti_altezza"]
    punti_scavi = st.session_state.scelte["punti_scavi"]
    
    punti_d_totale = punti_opera + punti_superficie + punti_altezza + punti_scavi
    d_normalizzato = min((punti_d_totale / 120.0) * 100.0, 100.0)
    
    # --- CALCOLO INDICE P (DISTURBO ATTIVITA) ---
    punti_p_totale = st.session_state.scelte["punti_disturbo"]
    p_normalizzato = min((punti_p_totale / 75.0) * 100.0, 100.0)
    
    # --- COEFFICIENTE FINALE ASSOLUTO (MEDIA PESATA 40% - 45% - 15%) ---
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
    st.markdown(f"Stato di Allerta Ecologica: <span style='color:{colore_stato}; font-weight:bold; font-size:22px;'>{stato_impatto}</span>", unsafe_allow_html=True)
    
    st.write("---")
    st.write(f"Sensibilita Territoriale (S): {s_normalizzato:.1f} / 100")
    st.write(f"Impronta Strutturale (D): {d_normalizzato:.1f} / 100")
    st.write(f"Disturbo Fase Cantiere (P): {p_normalizzato:.1f} / 100")
    st.write("---")
    
    with st.expander("Visualizza Riepilogo Parametri"):
        st.write(f"**Macro-area:** {macro}")
        st.write(f"**Sottocategoria:** {sotto} (Habitat: {punti_habitat} pt)")
        st.write(f"**Flora:** {', '.join(flora_scelta) if flora_scelta else 'Nessuna (Latenza 8 pt)'}")
        st.write(f"**Fauna:** {', '.join(fauna_scelta) if fauna_scelta else 'Nessuna (Latenza 8 pt)'}")
        st.write(f"**Matrice Suolo:** {st.session_state.scelte['suolo_testo']}")
        st.write(f"**Orografia:** {st.session_state.scelte['pendenza_testo']}")
        st.write(f"**Idrografia Superficiale:** {st.session_state.scelte['idro_testo']}")
        if punti_idro > 0:
            st.write(f"**Qualita Idrica:** {st.session_state.scelte['stato_acqua_testo']}")
        st.write(f"**Tipologia Struttura:** {st.session_state.scelte['opera_testo']}")
        st.write(f"**Superficie Coperta:** {st.session_state.scelte['superficie_testo']}")
        st.write(f"**Altezza Edificio:** {st.session_state.scelte['altezza_testo']}")
        st.write(f"**Profilo Scavi:** {st.session_state.scelte['scavi_testo']}")
        disturbi_attivi = st.session_state.scelte["disturbi_selezionati"]
        st.write(f"**Pressioni Antropiche:** {', '.join(disturbi_attivi) if disturbi_attivi else 'Nessun fattore rilevato'}")

    st.write("---")
    if st.button("Inizia una Nuova Valutazione", use_container_width=True):
        reset_totale()
