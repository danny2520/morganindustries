function setLanguage(lang) {
    localStorage.setItem("language", lang);

    const zhElements = document.querySelectorAll(".lang-zh");
    const enElements = document.querySelectorAll(".lang-en");

    if (lang === "zh") {
        zhElements.forEach(el => el.style.display = "inline");
        enElements.forEach(el => el.style.display = "none");
    } else {
        zhElements.forEach(el => el.style.display = "none");
        enElements.forEach(el => el.style.display = "inline");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const savedLang = localStorage.getItem("language") || "zh";
    setLanguage(savedLang);

    document.getElementById("lang-zh-btn").addEventListener("click", () => setLanguage("zh"));
    document.getElementById("lang-en-btn").addEventListener("click", () => setLanguage("en"));
});
