<script>
    import ButtonGroup from "./ButtonGroup.svelte";
    import JsonToHtml from "./JsonToHtml.svelte";

    const reqPredict = () => {
        console.log('Click reqPredict');
    }
    const reqRePredict = () => {
        console.log('Click reqRePredict');
    }

    // let jsonDatas = {
    //     "getSampleBtn": {
    //         "title": "Get Samples", 
    //         "color": "btn-success", 
    //         "click": "getSamples()",
    //         "reqPredictBtn": {
    //             "title": "Req Predict", 
    //             "color": "btn-danger", 
    //             "click": "reqPredict()",
    //             "reqPredictBtn": {
    //                 "title": "Req Predict", 
    //                 "color": "btn-danger", 
    //                 "click": "reqPredict()"
    //             },
    //             "reqRePredictBtn": {
    //                 "title": "ReReq Predict", 
    //                 "color": "btn-danger", 
    //                 "click": "reqRePredict()"
    //             },
    //         },
    //         "reqRePredictBtn": {
    //             "title": "ReReq Predict", 
    //             "color": "btn-danger", 
    //             "click": "reqRePredict()"
    //         },
    //     },
    //     "reqPredictBtn": {
    //         "title": "Req Predict", 
    //         "color": "btn-danger", 
    //         "click": "reqPredict()"
    //     },
    //     "reqRePredictBtn": {
    //         "title": "ReReq Predict", 
    //         "color": "btn-danger", 
    //         "click": "reqRePredict()"
    //     },
    // };

    async function getSampleData() {
        const res = await fetch('http://localhost:11000/samples');
        const jsonDatas = res.json()
        if (res.ok) {
            return jsonDatas;
        } else {
            throw new Error(jsonDatas)
        }
    }
    let promise;
    const getSamples = () => promise = getSampleData();

    let menuInfos = [
        {id: "getSamples", color: "btn-success", click: getSamples, label: "Get Samples"},
        {id: "reqPredict", color: "btn-primary", click: reqPredict, label: "Req Predict"},
        {id: "reqRePredict", color: "btn-primary", click: reqRePredict, label: "reqRe Predict"},
    ]
</script>

<div class="row justify-content-around">
    <!-- Input JSON data -->
    <div class="col-4">
        {#await promise}
            <p>...loading</p>
        {:then jsonDatas} 
            {#if jsonDatas === undefined}
                <p>Click "Get Samples" button.</p>
            {:else}
                <JsonToHtml {jsonDatas} />  
            {/if}
        {:catch error}
            <p style="color: red;">{error.message}</p>
        {/await}
    </div>
    <!-- Action Buttons -->
    <div class="col-2">
        <ButtonGroup {menuInfos} />
    </div>
    <!-- Predict Result JSON data -->
    <div class="col-4">
        <button class="btn btn-success">Success</button>
    </div>
</div>
