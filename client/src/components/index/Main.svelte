<script>
    import ButtonGroup from "./ButtonGroup.svelte";
    import JsonToHtml from "./JsonToHtml.svelte";

    const getSamples = () => {
        console.log('Click getSamples');
    }
    const reqPredict = () => {
        console.log('Click reqPredict');
    }
    const reqRePredict = () => {
        console.log('Click reqRePredict');
    }
    let menuInfos = [
        {id: "aaa", color: "btn-success", click: getSamples, label: "Get Samples"},
        {id: "bbb", color: "btn-primary", click: reqPredict, label: "Req Predict"},
        {id: "aaa", color: "btn-primary", click: reqRePredict, label: "reqRe Predict"},
    ]
    let jsonData = {
        "title": "Get Samples", 
        "color": "btn-success", 
        "click": "getSamples()",
        "getSampleBtn": {
            "title": "Get Samples", 
            "color": "btn-success", 
            "click": "getSamples()",
            "reqPredictBtn": {
                "title": "Req Predict", 
                "color": "btn-danger", 
                "click": "reqPredict()",
                "reqPredictBtn": {
                    "title": "Req Predict", 
                    "color": "btn-danger", 
                    "click": "reqPredict()"
                },
                "reqRePredictBtn": {
                    "title": "ReReq Predict", 
                    "color": "btn-danger", 
                    "click": "reqRePredict()"
                },
            },
            "reqRePredictBtn": {
                "title": "ReReq Predict", 
                "color": "btn-danger", 
                "click": "reqRePredict()"
            },
        },
        "reqPredictBtn": {
            "title": "Req Predict", 
            "color": "btn-danger", 
            "click": "reqPredict()"
        },
        "reqRePredictBtn": {
            "title": "ReReq Predict", 
            "color": "btn-danger", 
            "click": "reqRePredict()"
        },
    };
    $: jsonList = jsonData;
</script>

<div class="row justify-content-around">
    <!-- Input JSON data -->
    <div class="col-4">
        <JsonToHtml {jsonList} />
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

<style>
    :global(.sub-item-t) {
        padding-left: 30px;
    }
    :global(.sub-item-b) {
        padding-left: 0px;
        /* border: 0px !important; */
    }
    :global(.sub-item) {
        padding-left: 30px;
        padding-top: 0px;
        padding-bottom: 0px;
        padding-right: 0px;
    }
</style>
