<script lang="ts">
	import { fetchChatStream } from '$lib/openai_api';
	let { messages, response } = $props();

	async function query_openai() {
		try {
			await fetchChatStream(messages, (chunk) => {
				response += chunk;
			});
			console.log(response);
		} catch (e) {
			response = 'エラー発生';
			console.log(e);
		}
	}
</script>

<div class="w-full rounded-lg border px-4 py-2">
	<div class="flex flex-col">
		<textarea placeholder="質問をしてみましょう" class="bg-white" bind:value={messages}
			>{messages}</textarea
		>
		<div class="flex justify-end">
			<button class="bg-black text-white" onclick={() => query_openai()}>●</button>
		</div>
	</div>
</div>
