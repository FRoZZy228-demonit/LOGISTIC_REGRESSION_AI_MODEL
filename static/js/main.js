document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("inputForm");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {};

    formData.forEach((value, key) => {
      data[key] = parseFloat(value); // Convert input values to numbers
    });

    try {
      const response = await fetch("/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (result.prediction === 1) {
        resultDiv.innerHTML = " Intrusion Detected!";
        resultDiv.style.color = "red";
      } else {
        resultDiv.innerHTML = " No Threat Detected.";
        resultDiv.style.color = "green";
      }

    } catch (error) {
      resultDiv.innerHTML = "❌ Error: " + error;
      resultDiv.style.color = "darkred";
    }
  });
});
