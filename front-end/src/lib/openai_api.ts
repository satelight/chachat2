export async function fetchChatStream(
    message: string,
    onChunk: (chunk: string) => void
): Promise<void> {
    const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            message,
            model: "gpt-3.5-turbo",
        }),
    });

    if (!response.ok || !response.body) {
        throw new Error(`Fetch failed: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value, { stream: true });
        onChunk(chunk);
    }
}