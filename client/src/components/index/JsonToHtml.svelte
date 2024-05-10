<script>
    import { onMount } from "svelte";

	import MakeHtml from "./MakeHtml.svelte";
    export let jsonDatas;
    const jsonList = Object.entries(jsonDatas);

    onMount(() => {
        // console.log("JsonToHtml");
        // console.log(jsonDatas);
    });
</script>

<div class="jth-top">&#123;</div>
    {#each jsonList as [key, value]}
        <div>
            <MakeHtml {key} {value} />    
        </div>
    {/each}
<div class="jth-bottom">&#125</div>

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