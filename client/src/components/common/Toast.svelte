<script>
    export let id;

    let toastArgs = {
        reqPredictErr: { 
            img: "fa-solid fa-triangle-exclamation", 
            color: "#ff3d3d", 
            title: "Error:", 
            subTitle: "", 
            message: "The facility data for predicting construction costs hasn't been prepared yet."
        },
    }

    const ta = toastArgs[id];
</script>

<div 
    aria-live="polite" 
    aria-atomic="true" 
    class="position-fixed top-0 end-0 translate-middle-x"
>
    <div 
        id="liveToast" class="toast" role="alert" 
        aria-live="assertive" aria-atomic="true" data-bs-autohide="false" 
    >
        <div class="toast-header">
            <i class="{ta.img} img" style:color={ta.color}></i>
            <strong class="me-auto" style:color={ta.color}>{ta.title}</strong>
            <small>{ta.subTitle}</small>
            <button 
                type="button" class="btn-close"
                data-bs-dismiss="toast" aria-label="Close">
            </button>
        </div>
        <div class="toast-body">
            {ta.message}
        </div>
    </div>
</div>

<style>
    .position-fixed {
        margin-top: 0.5em;
    }

    .img {
        margin-right: 0.5em;
    }
</style>
