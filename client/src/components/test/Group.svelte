<script>
    import Item from "./Item.svelte";
    import { slide } from "svelte/transition";

    export let key;
    export let value;
    const values = Object.entries(value)
    let expanded = true;

    const toggle = () => expanded = !expanded;
    const isObject = (obj) => typeof obj === 'object' && obj !== null;
</script>

<button class:expanded on:click={toggle}>{key} : &#123;</button>

{#if expanded}
    <ul transition:slide={{ duration: 300 }}>
        {#each values as [k, v]}
            <li>
                {#if isObject(v)}
                    <svelte:self key={k} value={v} />
                {:else}
                    <div class="d-flex justify-content-between jth-body">
                        <div>{k} :</div><div>{v}</div>
                    </div>
                {/if}
            </li>
        {/each}
    </ul>
    <div class="jth-body">&#125</div>

{/if}

