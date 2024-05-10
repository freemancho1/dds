<script>
    import ButtonGroup from "./ButtonGroup.svelte";
    import JsonToHtml from "./JsonToHtml.svelte";
    import Toast from "../common/Toast.svelte";
    import axios from "axios";

    const url = {
        jsonHeader: {"Content-Type": "application/json"},
        sample: "http://localhost:11000/samples",
        predict: "http://localhost:11000/predict",
        rePredict: "http://localhost:11000/re_predict",
    }
    let samples;
    let samplesData;
    let predicts;

    async function getSampleData() {
        const response = await fetch(url.sample, {
            method: 'GET',
            headers: url.jsonHeader,
            body: undefined,
        });
        const data = response.json();

        if (response.ok) {
            return data;
        } else {
            throw new Error(data);
        }
    }
    const getSamples = () => samples = getSampleData();

    async function reqPredictData() {
        console.log(`reqPredict: ${samplesData}`);
        console.log(samplesData);
        const response = await fetch(url.predict, {
            method: 'POST',
            headers: url.jsonHeader,
            body: samplesData,
        });
        const data = response.json();

        if (response.ok) {
            return data;
        } else {
            throw new Error(data);
        }
    }
    const reqPredict = () => {
        if (samples === undefined) {
            const liveToast = bootstrap.Toast.getOrCreateInstance(
                document.getElementById("liveToast"));
            liveToast.show();
        } else {
            // predicts = undefined;
            predicts = reqPredictData();
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
</script>

<div class="row justify-content-around">
    <!-- Input JSON data -->
    <div class="col-4">
        {#if samples === undefined}
            <p>Click "Get Samples" button.</p>
        {:else}
            {#await samples}
                <p>...waiting</p>
            {:then mydata}
                {samplesData = mydata}
                {console.log(`then: ${samplesData}`)}
                {console.log(samplesData)}
                <JsonToHtml jsonDatas={mydata} />  
            {:catch error}
                <p style:color="red">{error.message}</p>
            {/await}
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
            {#await predicts}
                <p>...waiting</p>
            {:then data}
                <JsonToHtml jsonDatas={data} />  
            {:catch error}
                <p style:color="red">{error.message}</p>
            {/await}
        {/if}
    </div>
</div>

<Toast id="reqPredictErr"/>
