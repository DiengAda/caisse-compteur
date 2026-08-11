document.addEventListener("DOMContentLoaded", () => {
    const lignes = document.querySelectorAll(".ligne");
    const totalEl = document.getElementById("total");

    function calculerTout() {
        let total = 0;

        lignes.forEach((ligne) => {
            const valeur = parseFloat(ligne.dataset.valeur);
            const input = ligne.querySelector(".quantite");
            const sousTotalEl = ligne.querySelector(".sous-total");

            const quantite = parseInt(input.value) || 0;
            const sousTotal = valeur * quantite;

            sousTotalEl.textContent = sousTotal.toFixed(2) + " €";
            total += sousTotal;
        });

        totalEl.textContent = total.toFixed(2) + " €";
    }

    lignes.forEach((ligne) => {
        const input = ligne.querySelector(".quantite");
        input.addEventListener("input", calculerTout);
    });
});