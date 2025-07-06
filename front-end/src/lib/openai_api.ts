async function fetchChatStream(message: string) {
    const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            message,
            model: "gpt-3.5-turbo", // 任意、省略可
        }),
    });

    if (!response.ok || !response.body) {
        throw new Error(`Failed to fetch chat stream: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let result = "";

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value, { stream: true });
        console.log("chunk:", chunk); // 表示用
        result += chunk;
    }

    return result;
}
