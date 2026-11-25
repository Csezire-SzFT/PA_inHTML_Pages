# Python a böngészőben (PyScript)

## Mappaszerkezet

```
repo/
├── .github/workflows/manifest.yml     (változatlan)
├── js/
│   └── app.js                         (1 sor bővül)
├── lib/                               ← ÚJ: segédmodulok, a rács nem listázza
│   ├── seged.py
│   └── jatek/                         ← példa csomagra (almappa)
│       ├── __init__.py
│       └── kocka.py
├── pythons/
│   └── OrkGoblinXP.py                 ← futtatható script, importál a lib-ből
├── config.toml                        ← ÚJ: megmondja, mit másoljon be futtatás előtt
├── index.html                         (változatlan)
├── mini-coi.js                        (változatlan)
└── scripts.json                       (automatikus)
```

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