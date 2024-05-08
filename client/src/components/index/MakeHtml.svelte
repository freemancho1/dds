<script>
    import { slide } from "svelte/transition";

    export let key;
    export let value;
    
    let expanded = true;

    const values = Object.entries(value)

    const toggle = () => expanded = !expanded;
    const isObject = (obj) => typeof obj === 'object' && obj !== null;
</script>

{#if isObject(value)}
    <button class:expanded on:click={toggle}>{key} : &#123;</button>

    {#if expanded}
        <ul transition:slide={{ duration: 300 }} class="jth-group">
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
    {/if}
    <div class="jth-body-buttom">&#125;,</div>
{:else}
    <div class="d-flex justify-content-between jth-body">
        <div>{key} :</div><div>{value}</div>
    </div>
{/if}

<style>
    button {
        font-weight: bold;
        cursor: pointer;
        border: none;
        font-size: 16px;
        margin: 0 0 0 2em;
        background-color: white;
    }

    ul {
        margin: 0 0 0 0;
        list-style: none;
        /* border-left: 1px solid #eee; */
    }

    .jth-body-buttom {
        margin: 2px 0 2px 2.5em;
        font-weight: bold;
    }

    .jth-body {
        margin: 2px 0 2px 2.5em;
    }
</style>

