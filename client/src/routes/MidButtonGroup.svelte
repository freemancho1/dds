<script>
    import Button from "./../components/common/Button.svelte";

    export let indexButtonGroupMenus;
</script>

<div class="d-flex justify-content-center">
    <div class="d-grid gap-5">
        {#each indexButtonGroupMenus as menu}
            <Button {menu} />
        {/each}
    </div>
</div>