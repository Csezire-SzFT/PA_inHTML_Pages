
**A repo mappa szerkezete** <br>
repo/ <br>
├── .github/workflows/manifest.yml     (változatlan) <br>
├── js/ <br>
│   └── app.js                         (1 sor bővül) <br>
├── lib/                               ← ÚJ: a segédmodulok, a rács nem listázza <br>
│   ├── seged.py <br>
│   └── jatek/                         ← példa csomagra (almappa) <br>
│       ├── __init__.py <br>
│       └── kocka.py <br>
├── pythons/ <br>
│   └── OrkGoblinXP.py                 ← futtatható script, importál a lib-ből <br>
├── config.toml                        ← ÚJ: megmondja, mit másoljon be a futtatás előtt <br>
├── index.html                         (változatlan) <br>
├── mini-coi.js                        (változatlan) <br>
└── scripts.json                       (automatikus) <br>


**A workflow file leírása** <br>

A workflow két módon indul <br>
 - kézileg <br>
 - automatikusan, ha a pythons mappába egy push művelettel új file érkezik <br>

A workflow írási jogot kap a repository felett (ahová fel lett töltve), hogy a frissített file listát tartalmazó script.json visszaírásra kerülhessen a repository-ba. <br>

A workflow <br>
 - egy - a github által biztosított - virtuális gépen (Linux - Ubuntu OS) fog futni <br>
 - a repository tartalma felkerül erre a virtuális gépre, hogy a benne lévő adatok elérhetőek legyenek <br>
 - a CLI-ben (Linux) elindul egy többlépcsős folyamat, melynek során <br>
   = készít egy listát a pythons mappában lévő py kiterjesztésű file-okról a mappa nevével együtt (ls) <br>
   = minden egyes file-névből levágja az útvonalat, csak a file-nevet adja vissza <br>
   = a file-neveket JSON formátumúra alakítja és egy tömbbe rendezi <br>
   = a tömböt kiírja a script.json file-ba <br>
 - ezután ellenőrzésre kerül van-e változás, és ha igen, akkor lefut egy commit és egy push a frissítés érdekében <br>


**A HTML és a kapcsolódó JS működése** <br>

Mindig ugyanaz az index.html töltődik be, csak más URL-lel, és a JavaScript a böngészőben, futás közben építi fel, hogy mit jelenítsen meg. A Menet lépésről lépésre <br>

1. Első betöltés: https://csezire.github.io/REPO/
   1.1. A böngésző betölti az index.html-t, a core.css-t és a mini-coi.js-t.
   1.2. A mini-coi.js regisztrálja a service workert. Ha ez az első látogatás, az oldal egyszer automatikusan újratölt, hogy a worker átvegye az irányítást.
   1.3. Lefut a <script type="module">: lekéri a fájllistát (scripts.json).
   1.4. Az URL-ben nincs ?s= paraméter, ezért a wanted értéke null, és az else ág fut le. Ez egy <a> linket készít minden .py fájlhoz, és berakja a rácsba.
   1.5. A PyScript (core.js) ilyenkor még be sem töltődik, mert nincs mit futtatnia.

2. Kattintás egy cellára
   2.1. A cella egy sima link: href="?s=OrkGoblinXP.py".
   2.2. A böngésző ugyanarra az oldalra navigál, csak az URL végére kerül a paraméter: .../REPO/?s=OrkGoblinXP.py.
   2.3. Ez teljes oldalújratöltés, vagyis a régi oldal és minden, ami rajta futott, eltűnik.

3. Második betöltés: ...?s=OrkGoblinXP.py
   3.1. Ugyanaz az index.html töltődik be, a lista újra lekérődik.
   3.2. Most a wanted értéke "OrkGoblinXP.py", és szerepel a fájllistában, így az if ág fut le.
   3.3. A JS eltávolítja a rácsot, és létrehoz egy új <script type="py" src="./pythons/OrkGoblinXP.py" worker terminal> elemet, ami pont ugyanaz, mint amit eddig kézzel íródott az index.html-be. A különbség csak az, hogy most a JS illeszti be.
   3.4. Utána betölti a core.js-t. A PyScript elindul, megtalálja ezt a taget, letölti a Python fájlt, elindítja a workert, és kirajzolja a terminált.

4. Mi van, ami nem látszik elsőre
   4.1. Nincs "új link generálás": a link a rács építésekor készül (?s=fájlnév), a címsorba is be lehet másolni, és bárkinek elküldhető, aki így közvetlenül egy adott scriptet nyit meg.
   4.2. Az engedélyezési lista (files.includes(wanted)) miatt csak olyan fájl indulhat el, ami tényleg ott van a pythons mappában.
   4.3. A core.js késleltetett betöltése azért fontos, mert a PyScript az induláskor végignézi az oldalt a type="py" tagekért. Ha előbb töltődne be, mint ahogy a JS létrehozza a tagot, nem találná meg.
   4.4. Visszalépés: a böngésző vissza gombja a rácsra visz, ami szintén újratölt, így a futó script leáll. A scriptek között váltani is csak így lehet, ami szándékos, mert így nincs két interpreter és két terminál egymás nyakán.