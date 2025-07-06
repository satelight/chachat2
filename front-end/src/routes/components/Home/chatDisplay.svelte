<script lang="ts">
	import ChatBubble from './ui/chatBubble.svelte';
	let { messages, response } = $props();
	$inspect(response);
</script>

<div class="">
	<ChatBubble {messages} />
	<ChatBubble messages={response} />
</div>
