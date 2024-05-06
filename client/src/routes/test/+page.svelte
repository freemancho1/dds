<script>
    import Item from "../../components/test/Item.svelte";
    import Group from "../../components/test/Group.svelte";
    let jsonDatas = {
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
    const jsonList = Object.entries(jsonDatas)
</script>

<div class="jth-top">&#123;</div>
{#each jsonList as [key, value]}
    <Group {key} {value} />    
{/each}
<div class="jth-body">&#125</div>
<div class="jth-bottom">&#125</div>

<style>
    .jth-top {
        margin: 10px 0 2px 0;
    }
    :global(.jth-body) {
        margin: 2px 0 2px 2em;
    }
    :global(.jth-child-buttom) {
        margin: 2px 0 2px 2em;
    }
    .jth-bottom {
        margin: 2px 0 10px 0;
    }
</style>