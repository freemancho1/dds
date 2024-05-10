<script>
    import { jsonStart, jsonEnd } from "$lib/config.js";
    import MakeHtml from "./MakeHtml.svelte";
    
    export let jsonDatas;
    const jsonList = Object.entries(jsonDatas);
</script>

<div class="jth-top">{@html jsonStart}</div>
    {#each jsonList as [key, value]}
    <div><MakeHtml {key} {value} /></div>
    {/each}
<div class="jth-bottom">{@html jsonEnd}</div>

<style>
    .jth-top {
        margin: 10px 0 2px 0;
        font-weight: bold;
    }
    .jth-bottom {
        margin: 2px 0 10px 0;
        font-weight: bold;
    }
</style>