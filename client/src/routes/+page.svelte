<script>
    import Title from "../components/sys/AppTitle.svelte";
    import Footer from "../components/sys/AppFooter.svelte";
    import AppBody from "./AppBody.svelte";
</script>

<div class="container app">
    <!-- App Title -->
    <div class="app app-title">
        <Title />
    </div>

    <!-- App MainBody -->
    <div class="app app-body">
        <AppBody />
    </div>

    <!-- App Footer -->
    <div class="app app-footer">
        <Footer />
    </div>
</div>