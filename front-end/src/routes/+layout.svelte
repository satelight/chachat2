<script lang="ts">
	import '../app.css';
	import LoginPage from './components/loginPage/LoginPage.svelte';
	import Layout from './components/layout/Layout.svelte';

	let isNOKUser: boolean = true;
	let { children } = $props();
</script>

{#if isNOKUser}
	<Layout {children} />
{:else}
	<LoginPage />
{/if}
