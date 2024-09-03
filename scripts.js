document.getElementById("healthForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const formProps = Object.fromEntries(formData);

  const responseDiv = document.getElementById("response");
  responseDiv.innerText = "Loading...";

  try {
    const response = await fetch("/api/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formProps),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok and i like to reuse again");
    }

    const data = await response.json();
    responseDiv.innerText = data;
  } catch (error) {
    responseDiv.innerText = "Error: " + error.message;
  }
});
