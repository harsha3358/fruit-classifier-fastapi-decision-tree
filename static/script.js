function predict() {
    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            weight: parseInt(document.getElementById("weight").value),
            color: document.getElementById("color").value,
            texture: document.getElementById("texture").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Predicted Fruit: " + data.prediction;
    })
    .catch(() => alert("API not running"));
}
