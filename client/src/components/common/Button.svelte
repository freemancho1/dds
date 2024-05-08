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
</button>
