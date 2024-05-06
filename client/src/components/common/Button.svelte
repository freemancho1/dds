<script>
    import { slide } from "svelte/transition";
    export let menu;

    let expanded = false;
    const toggle = () => expanded = !expanded;
</script>

<button 
    id={menu.id} 
    type="button" 
    class="btn {menu.color}" 
    on:click={menu.click}>
    {menu.label} 
    {#if menu.id === "getSamples"}
        <a href="/" on:click|preventDefault|stopPropagation={()=>toggle()}>
            ▼
        </a>
    {/if}
</button>

{#if expanded}
<ul transition:slide={{ duration: 300 }}>
    <li><div class="form-control">
        aaaa
    </div></li>
</ul>
{:else}
<!-- <p>a 3, b 4</p> -->
{/if}