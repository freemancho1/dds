<script>
    import { waiting } from "$lib/config.js";
    import JsonToHtml from "./JsonToHtml.svelte";

    export let promise;
</script>

{#await promise}
    <p>{waiting}</p>
{:then jsonDatas} 
    <JsonToHtml {jsonDatas} />
{:catch error}
    <p style:color="red">{error.message}</p>
{/await}