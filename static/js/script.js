document.addEventListener("DOMContentLoaded", () => {
    // Récupère toutes les lignes de billets
    const lignes = document.querySelectorAll(".ligne");

    lignes.forEach((ligne) => {
        const valeur = parseFloat(ligne.dataset.valeur);
        const input = ligne.querySelector(".quantite");
        const sousTotalEl = ligne.querySelector(".sous-total");

        // Recalcule à chaque frappe dans le champ
        input.addEventListener("input", () => {
            const quantite = parseInt(input.value) || 0;
            const sousTotal = valeur * quantite;
            sousTotalEl.textContent = sousTotal.toFixed(2) + " €";
        });
    });
});