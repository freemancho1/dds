<script>
    import ButtonGroup from "./ButtonGroup.svelte";
    import JsonToHtml from "./JsonToHtml.svelte";
    import Toast from "../common/Toast.svelte";

    const reqRePredict = () => {
        console.log('Click reqRePredict');
    }

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

    async function predict() {
        const liveToast = bootstrap.Toast.getOrCreateInstance(
            document.getElementById("liveToast"));
        liveToast.show();
        // console.log(promise);
    }
    const reqPredict = () => {
        const liveToast = bootstrap.Toast.getOrCreateInstance(
            document.getElementById("liveToast"));
        liveToast.show();
        console.log(promise);
    }

    let menuInfos = [
        {id: "getSamples", color: "btn-success", click: getSamples, label: "Get Samples"},
        {id: "reqPredict", color: "btn-primary", click: reqPredict, label: "Req Predict"},
        {id: "reqRePredict", color: "btn-primary", click: reqRePredict, label: "reqRe Predict"},
    ]
    let toastArgs = {
        title: "Information:", subTitle: "", message: "The facility data for predicting construction costs hasn't been prepared yet.",
    }
</script>

<div class="row justify-content-around">
    <!-- Input JSON data -->
    <div class="col-4">
        <i class="fa-solid fa-circle-info"></i>
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

<Toast />
