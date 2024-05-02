<script>
    export let jsonData;
    export let isObject;
    const jsonList = Object.entries(jsonData)

    // const isObject = (obj) => {
    //     return typeof obj === 'object' && obj !== null;
    // }
</script>

<ul class="list-group list-group-flush">
    {#each jsonList as [key, value]}
        {#if isObject(value)}
            <li class="list-group-item sub-item-t">{key}: &#123</li>
            <li class="list-group-item sub-item">
                <svelte:self jsonData={value} />
            </li>
        {:else}
            <li class="list-group-item sub-item-t">
                <div class="d-flex justify-content-between">
                    <div>{key}:</div><div>{value}</div>
                </div>
            </li>
        {/if}
    {/each}
</ul>
<li class="list-group-item sub-item-b">&#125;,</li>

<style>
    .list-group-item {
        border: 0px;
    }
</style>