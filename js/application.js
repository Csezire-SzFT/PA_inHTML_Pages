const pySources = "pythons";
const gridInHTML = document.getElementById("grid");

const res = await fetch("./scripts.json");
if (!res.ok) {
   gridInHTML.textContent = "Nem található a scripts.json.";
   throw new Error(`scripts.json hiba: ${res.status}`);
}
const files = (await res.json())
   .filter(name => name.endsWith(".py") && !name.startsWith("_"));

const wanted = new URLSearchParams(location.search).get("s");

if (wanted && files.includes(wanted)) {
   gridInHTML.remove();

   const backLink = document.createElement("a");
   backLink.href = "./";
   backLink.textContent = "← Vissza a listához";
   backLink.className = "back";
   document.body.prepend(backLink);

   const scriptTag = document.createElement("script");
   scriptTag.type = "py";
   scriptTag.src = `./${pySources}/${encodeURIComponent(wanted)}`;
   scriptTag.setAttribute("config", "./config.toml");     // ÚJ: a közös konfiguráció betöltése
   scriptTag.setAttribute("worker", "");
   scriptTag.setAttribute("terminal", "");
      document.body.append(scriptTag);

   await import("https://pyscript.net/releases/2026.7.3/core.js");
} 
else
{
   for (const name of files) {
      const anchorTAG = document.createElement("a");
      anchorTAG.href = `?s=${encodeURIComponent(name)}`;
      anchorTAG.textContent = name.replace(/\.py$/, "");
      gridInHTML.append(anchorTAG);
  }
}