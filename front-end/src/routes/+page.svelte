<script lang="ts">
	import ChatDisplay from './components/Home/chatDisplay.svelte';
	import InputForm from './components/Home/InputForm.svelte';
	let messages = $state('test');
</script>

<div class="flex flex-1 flex-col gap-4 px-4 py-10">
	<div class="mx-auto h-full w-full max-w-3xl rounded-xl">
		<ChatDisplay {messages} />
	</div>
	<div class="mx-auto h-24 w-full max-w-3xl rounded-xl">
		<InputForm />
	</div>
</div>
