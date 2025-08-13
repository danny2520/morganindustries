document.addEventListener("DOMContentLoaded", function () {
    const zhBtn = document.getElementById("lang-zh-btn");
    const enBtn = document.getElementById("lang-en-btn");

    function showChinese() {
        document.querySelectorAll(".lang-zh").forEach(el => el.style.display = "inline");
        document.querySelectorAll(".lang-en").forEach(el => el.style.display = "none");
    }

    function showEnglish() {
        document.querySelectorAll(".lang-zh").forEach(el => el.style.display = "none");
        document.querySelectorAll(".lang-en").forEach(el => el.style.display = "inline");
    }

    zhBtn.addEventListener("click", showChinese);
    enBtn.addEventListener("click", showEnglish);

    // Default: show Chinese first
    showChinese();
});
