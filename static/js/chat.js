document
  .getElementById("chat-form")
  .addEventListener("submit", async function (event) {
    event.preventDefault();
    const userInput = document.getElementById("user-input").value;

    if (userInput.trim() === "") {
      alert("Input cannot be empty");
      return;
    }

    const formData = new FormData();
    formData.append("user_input", userInput);

    try {
      const response = await fetch("/chat", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (response.ok) {
        const chatLog = document.getElementById("chat-log");
        const userMessage = document.createElement("li");
        const spanUserMessage = document.createElement("span");
        spanUserMessage.setAttribute("class", "avatar user");
        spanUserMessage.textContent = "You";
        const divUserMessage = document.createElement("div");
        divUserMessage.setAttribute("class", "message");
        divUserMessage.textContent = `${userInput}`;

        userMessage.appendChild(spanUserMessage);
        userMessage.appendChild(divUserMessage);
        chatLog.appendChild(userMessage);

        const botMessage = document.createElement("li");
        const spanBotMessage = document.createElement("span");
        spanBotMessage.setAttribute("class", "avatar bot");
        spanBotMessage.textContent = "AI";
        const divBotMessage = document.createElement("div");
        divBotMessage.setAttribute("class", "message");
        divBotMessage.textContent = `${data.response}`;

        botMessage.appendChild(spanBotMessage);
        botMessage.appendChild(divBotMessage);
        chatLog.appendChild(botMessage);

        document.getElementById("user-input").value = "";
        chatLog.scrollTop = chatLog.scrollHeight;
      } else {
        alert(`Error: ${data.error}`);
      }
    } catch (error) {
      alert(`Error: ${error.message}`);
    }
  });
