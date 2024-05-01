<script>
    export let menu;
</script>

<button 
    id={menu.id} 
    type="button" 
    class="btn {menu.color}" 
    on:click={menu.click}>
    {menu.label}
</button>