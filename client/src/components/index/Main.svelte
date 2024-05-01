<script>
    import ButtonGroup from "./ButtonGroup.svelte";

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
</script>

<div class="row justify-content-around">
    <!-- Input JSON data -->
    <div class="col-4">
        <button class="btn btn-primary">Primary</button>
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
