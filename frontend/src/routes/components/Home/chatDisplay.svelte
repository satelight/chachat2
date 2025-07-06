<script lang="ts">
	import ChatBubble from './ui/chatBubble.svelte';
	let { messages } = $props();
</script>

<div class="">
	<ChatBubble {messages} />
</div>
