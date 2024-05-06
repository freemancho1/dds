<script>
    import JsonToHtmlSub from "./JsonToHtmlSub.svelte";
    export let jsonList;
    // $: jsonList1 = JSON.parse(jsonList)
    const temp = Object.entries(jsonList);
    
    // const isObject = (obj) => typeof obj === 'object' && obj !== null;
    const isObject = (obj) => {
        return typeof obj === 'object' && obj !== null;
    }
</script>

<li class="list-group-item">&#123;</li>
<ul class="list-group list-group-flush">
    {#each temp as [key, value]}
        {#if isObject(value)}
            <li class="list-group-item sub-item-t">{key}: &#123;</li>
            <li class="list-group-item sub-item">
                <JsonToHtmlSub jsonData={value} />
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
<li class="list-group-item">&#125;</li>