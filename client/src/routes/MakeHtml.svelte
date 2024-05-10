<script>
    import { slide } from "svelte/transition";
    import { jsonStart, jsonEnd } from "$lib/config.js";
    import KeyValue from "./KeyValue.svelte";

    export let key;
    export let value;
    const values = Object.entries(value);

    let expanded = true;

    const toggle = () => expanded = !expanded;
    const isObject = (obj) => typeof obj === 'object' && obj !== null;
</script>

{#if isObject(value)}
    <button class:expanded on:click={toggle}>
        {key} : {@html jsonStart}
    </button>

        {#if expanded}
            <ul transition:slide={{ duration: 300 }} class="jth-group">
                {#each values as [itemKey, itemValue]}
                    <li>
                        {#if isObject(itemValue)}
                            <svelte:self key={itemKey} value={itemValue} />
                        {:else}
                            <KeyValue key={itemKey} value={itemValue} />
                        {/if}
                    </li>
                {/each}
            </ul>
        {/if}
    <div class="jth-body-buttom">{@html jsonEnd}</div>
{:else}
    <KeyValue {key} {value} />
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
</style>