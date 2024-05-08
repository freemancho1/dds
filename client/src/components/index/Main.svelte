<script>
    import ButtonGroup from "./ButtonGroup.svelte";
    import JsonToHtml from "./JsonToHtml.svelte";
    import Toast from "../common/Toast.svelte";
    import axios from "axios";

    let samples;
    let predicts;

    async function getSampleData() {
        await axios.get('http://localhost:11000/samples')
            .then(res => {
                samples = res.data;
            })
            .catch(error => {
                console.log("Error:", error);
            });
    }
    const getSamples = () => {
        samples = undefined;
        getSampleData();
    }

    async function reqPredictData() {
        await axios.post("http://localhost:11000/predict", samples)
            .then(res => {
                predicts = res.data;
            })
            .catch(error => {
                console.log("Error:", error);
            });
    }
    const reqPredict = () => {
        if (samples === undefined) {
            const liveToast = bootstrap.Toast.getOrCreateInstance(
                document.getElementById("liveToast"));
            liveToast.show();
        } else {
            predicts = undefined;
            reqPredictData();
        }
    }

    async function reqRePredictData() {
        await axios.post("http://localhost:11000/re_predict", samples)
            .then(res => {
                predicts = res.data;
            })
            .catch(error => {
                console.log("Error:", error);
            });
    }
    const reqRePredict = () => {
        if (samples === undefined) {
            const liveToast = bootstrap.Toast.getOrCreateInstance(
                document.getElementById("liveToast"));
            liveToast.show();
        } else {
            predicts = undefined;
            reqRePredictData();
        }
    }

    let menuInfos = [
        {id: "getSamples", color: "btn-success", click: getSamples, label: "Get Samples"},
        {id: "reqPredict", color: "btn-primary", click: reqPredict, label: "Req Predict"},
        {id: "reqRePredict", color: "btn-primary", click: reqRePredict, label: "reqRe Predict"},
    ]
    // let toastArgs = {
    //     title: "Information:", subTitle: "", message: "The facility data for predicting construction costs hasn't been prepared yet.",
    // }
</script>

<div class="row justify-content-around">
    <!-- Input JSON data -->
    <div class="col-4">
        {#if samples === undefined}
            <p>Click "Get Samples" button.</p>
        {:else}
            <JsonToHtml jsonDatas={samples} />  
        {/if}
    </div>
    <!-- Action Buttons -->
    <div class="col-2">
        <ButtonGroup {menuInfos} />
    </div>
    <!-- Predict Result JSON data -->
    <div class="col-4">
        {#if predicts === undefined}
            <p></p>
        {:else}
            <JsonToHtml jsonDatas={predicts} />  
        {/if}
    </div>
</div>

<Toast id="reqPredictErr"/>
