# Python a böngészőben (PyScript)

## Mappaszerkezet

```
repo/
├── .github/workflows/manifest.yml     ← workflow a scripts.json frissítéséhez
├── js/
│   └── app.js                         ← a fő vezérlés: megjelenítés vagy py-script futtatás előkészítése
├── lib/                               ← segédmodulok, a rács nem listázza
│   ├── seged.py
│   └── jatek/                         ← példa csomagra (almappa)
│       ├── __init__.py
│       └── kocka.py
├── pythons/
│   └── OrkGoblinXP.py                 ← futtatható py-script, importálhat a lib-ből
├── config.toml                        ← megmondja, mit másoljon be futtatás előtt
├── index.html                         ← az alap HTML oldal
├── mini-coi.js                        ← service worker, a py-scriptek futtatásának támogatása
└── scripts.json                       ← a pythons könyvtárban található py-scriptek listája
```

A `lib/` mappát a workflow nem látja (csak a `pythons/*.py` fájlokat listázza), ezért a segédmodulok nem jelennek meg kattintható cellaként.

## A config.toml

A `config.toml` a repó gyökerében van:

```toml
# Külső csomagok (csak ha kellenek, pl. numpy)
# packages = ["numpy"]

[files]
# "forrás URL" = "hová kerüljön a virtuális fájlrendszerben"
"./lib/seged.py"          = "./seged.py"
"./lib/jatek/__init__.py" = "./jatek/__init__.py"
"./lib/jatek/kocka.py"    = "./jatek/kocka.py"
```

Minden modulfájlt külön sorban kell felsorolni. Új modul felvétele után ide is be kell írni egy sort. A fájl a gyökérben van, így az útvonalak az oldalhoz és a config fájlhoz képest is ugyanúgy értelmezhetőek.

## A workflow

A workflow kétféleképpen indul:

- kézzel
- automatikusan, ha a `pythons` mappába push-sal új fájl érkezik

Írási jogot kap a repositoryhoz, hogy a frissített `scripts.json` visszaírható legyen.

### Lépések

A workflow egy GitHub által biztosított Ubuntu virtuális gépen fut:

- A repository tartalma felkerül a gépre.
- Listát készít a `pythons` mappa `.py` fájljairól.
- Minden útvonalból csak a fájlnevet tartja meg.
- A neveket JSON tömbbé alakítja.
- A tömböt kiírja a `scripts.json` fájlba.
- Ha van változás, `commit` és `push` következik.

## A HTML és a JS működése

Mindig ugyanaz az `index.html` töltődik be, csak más URL-lel. A JavaScript futás közben építi fel, mit jelenítsen meg.

### 1. Első betöltés

URL: `https://csezire.github.io/PA_inHTML_Pages/`

- A böngésző betölti az `index.html`-t, a `core.css`-t és a `mini-coi.js`-t.
- A `mini-coi.js` regisztrálja a service workert, első látogatáskor az oldal egyszer újratölt.
- Lefut a `<script type="module">`, és lekéri a `scripts.json`-t.
- Nincs `?s=` paraméter, ezért a `wanted` értéke `null`, és az `else` ág fut: linket készít minden `.py` fájlhoz.
- A PyScript (`core.js`) ilyenkor még nem töltődik be.

### 2. Kattintás egy cellára

- A cella sima link: `href="?s=OrkGoblinXP.py"`.
- Ez teljes oldalújratöltés, a régi oldal eltűnik.

### 3. Második betöltés (például `?s=OrkGoblinXP.py`)

- Az `index.html` újra betöltődik, a lista is.
- A `wanted` értéke `"OrkGoblinXP.py"`, ez szerepel a listában, így az `if` ág fut.
- A JS eltávolítja a rácsot, és létrehozza a `<script type="py" ...>` elemet.
- Betölti a `core.js`-t, a PyScript elindul, és kirajzolja a terminált.

### 4. Amit érdemes tudni

- **Megosztható link:** a `?s=fájlnév` link bárkinek elküldhető.
- **Engedélyezési lista:** a `files.includes(wanted)` miatt csak a `pythons` mappában lévő fájl indulhat.
- **Késleltetett `core.js`:** a PyScript induláskor keresi a `type="py"` tageket, ezért csak a tag létrehozása után töltődhet be.
- **Visszalépés:** a vissza gomb a rácsra visz, a futó script leáll, így nincs két interpreter egyszerre.
