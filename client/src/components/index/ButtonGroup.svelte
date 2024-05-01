<script>
    export let menuInfos;
    import Button from "../common/Button.svelte";
</script>

<div class="d-flex justify-content-center">
    <div class="d-grid gap-5">
        { #each menuInfos as menu }
            <Button {menu} />
        { /each }
    </div>
</div>