async function sendMessage() {

    const input = document.getElementById("userInput");

    const message = input.value;

    if (message.trim() === "") {
        return;
    }

    const chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `
        <div class="message user-message">
            ${message}
        </div>
    `;

    input.value = "";

    document.getElementById("typing").style.display = "block";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    setTimeout(() => {

        document.getElementById("typing").style.display = "none";

        chatbox.innerHTML += `
            <div class="message bot-message">
                ${data.reply}
            </div>
        `;

        const trace = document.getElementById("trace");

        trace.innerHTML = "";

        data.trace.forEach(step => {
            trace.innerHTML += `<li>✔ ${step}</li>`;
        });

        chatbox.scrollTop = chatbox.scrollHeight;

    }, 1000);

}