"use strict";
function predict() {
    const weight = parseInt(document.getElementById("weight").value);
    const color = document.getElementById("color").value;
    const texture = document.getElementById("texture").value;
    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ weight, color, texture })
    })
        .then(res => res.json())
        .then((data) => {
        const result = document.getElementById("result");
        result.innerText = "Predicted Fruit: " + data.prediction;
    })
        .catch(err => console.error(err));
}
// expose to window
window.predict = predict;
