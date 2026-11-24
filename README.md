
**A repo mappa szerkezete**
repo/
├── .github/workflows/manifest.yml     (változatlan)
├── js/
│   └── app.js                         (1 sor bővül)
├── lib/                               ← ÚJ: a segédmodulok, a rács nem listázza
│   ├── seged.py
│   └── jatek/                         ← példa csomagra (almappa)
│       ├── __init__.py
│       └── kocka.py
├── pythons/
│   └── OrkGoblinXP.py                 ← futtatható script, importál a lib-ből
├── config.toml                        ← ÚJ: megmondja, mit másoljon be a futtatás előtt
├── index.html                         (változatlan)
├── mini-coi.js                        (változatlan)
└── scripts.json                       (automatikus)