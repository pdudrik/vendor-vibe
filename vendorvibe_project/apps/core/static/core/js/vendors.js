document.addEventListener("DOMContentLoaded", () => {
    console.log("in function");
    const rows = document.querySelectorAll(".clickable-row");
    console.log(rows);

    rows.forEach(row => {
        row.addEventListener("click", function(event) {
            // Ignore if user clicked button or form
            console.log("Clicked");
            if (event.target.closest("button") || event.target.closest("form")) {
                return;
            }

            const url = this.dataset.url;
            if (url) {
                console.log("url: ", url);
                window.location.href = url;
            }
        });
    });
});