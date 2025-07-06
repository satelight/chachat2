<script lang="ts">
	import Button from '$lib/components/ui/button/button.svelte';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { fetchChatStream } from '$lib/openai_api';
	let textarea = $state('');
	let messages = $state('');
	let response = $state('');
	let isLoading = $state(false);

	async function query_openai() {
		isLoading = true;
		response = '';
		try {
			messages = textarea;
			textarea = '';
			await fetchChatStream(messages, (chunk) => {
				response += chunk;
				isLoading = false;
			});
			console.log(response);
		} catch (e) {
			response = 'エラー発生';
			console.log(e);
		}
	}
</script>

<div class="flex flex-1 flex-col gap-4 px-4 py-10">
	<div class="mx-auto h-full w-full max-w-3xl flex-1 rounded-xl">
		<div class="flex items-end justify-end">
			<div class="mx-auto h-full w-full rounded-sm bg-neutral-200">{messages}</div>
		</div>
		{#if isLoading === false}
			<div class="flex items-end justify-end">
				<div class="mx-auto h-full w-full rounded-sm">{response}</div>
			</div>
		{:else}
			<div>loading</div>
		{/if}
	</div>

	<div class="mx-auto h-24 w-full max-w-3xl rounded-xl">
		<div class="w-full rounded-lg border px-4 py-2">
			<div class="flex flex-col">
				<textarea
					placeholder="質問をしてみましょう"
					class="resize-none border-none bg-white focus:border-none focus:outline-none"
					bind:value={textarea}
				></textarea>
				<div class="mt-3 flex justify-between">
					<Button>
						<label class="mr-2">
							ファイル選択/select file
							<input type="file" class="hidden" />
						</label>
					</Button>
					<Button onclick={() => query_openai()}>送信/Send</Button>
				</div>
			</div>
		</div>
	</div>
</div>
