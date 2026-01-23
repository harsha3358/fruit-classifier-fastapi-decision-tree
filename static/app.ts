interface PredictionResponse {
    prediction: string;
}

function predict(): void {
    const weight = parseInt((document.getElementById("weight") as HTMLInputElement).value);
    const color = (document.getElementById("color") as HTMLSelectElement).value;
    const texture = (document.getElementById("texture") as HTMLSelectElement).value;

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ weight, color, texture })
    })
    .then(res => res.json())
    .then((data: PredictionResponse) => {
        const result = document.getElementById("result") as HTMLDivElement;
        result.innerText = "Predicted Fruit: " + data.prediction;
    })
    .catch(err => console.error(err));
}

// expose to window
(window as any).predict = predict;
