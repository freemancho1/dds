<script>
    import { reqGET, reqPOST } from "$lib/communication.js";
    import { clickSamples } from "$lib/config.js";

    import MidButtonGroup from './MidButtonGroup.svelte';
    import WrappingJth from "./WrappingJTH.svelte";
    import Toast from "./../components/common/Toast.svelte";

    let samples;
    let predicts;

    const getSamples = () => samples = reqGET("samples");

    const reqPredicts = (predict) => {
        if (samples === undefined) {
            bootstrap.Toast.getOrCreateInstance(
                document.getElementById("liveToast")
            ).show();
        } else {
            predicts = (predict === "predict" || predict === "") ?
                reqPOST("predict", samples): reqPOST("rePredict", samples);
        }
    }
    const reqPredict = () => reqPredicts("predict");
    const reqRePredict = () => reqPredicts("rePredict");

    const indexButtonGroupMenus = [
        {id: "getSamples", color: "btn-success", click: getSamples, label: "Get Samples"},
        {id: "reqPredict", color: "btn-primary", click: reqPredict, label: "Req Predict"},
        {id: "reqRePredict", color: "btn-primary", click: reqRePredict, label: "reqRe Predict"},
    ];
</script>

<Toast id="reqPredictErr" />

<div class="row justify-content-around">
    <div class="col-4">
        {#if samples === undefined}
            <p>{clickSamples}</p>
        {:else}
            <WrappingJth promise={samples} />
        {/if}
    </div>

    <div class="col-2">
        <MidButtonGroup {indexButtonGroupMenus} />
    </div>

    <div class="col-4">
        {#if predicts === undefined}
            <p></p>
        {:else}
            <WrappingJth promise={predicts} />
        {/if}
    </div>
</div>