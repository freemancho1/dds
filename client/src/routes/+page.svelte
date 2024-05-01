<script>
    import Title from "../components/sys/AppTitle.svelte";
    import Footer from "../components/sys/AppFooter.svelte";
    import IndexMain from "../components/index/Main.svelte";
</script>

<div class="container app">
    <!-- App Title -->
    <div class="app app-title">
        <Title />
    </div>

    <!-- App MainBody -->
    <div class="app app-main">
        <IndexMain />
    </div>

    <!-- App Footer -->
    <div class="app app-footer">
        <Footer />
    </div>
</div>