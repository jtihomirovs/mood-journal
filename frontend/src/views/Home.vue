<template>
  <div id="app">
    <HeaderComponent />

    <DashboardPage />

    <Sidebar />

    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent.vue";
import Sidebar from "@/components/SideBar.vue";
import DashboardPage from "@/components/DashboardPage.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  name: "App",
  components: {
    HeaderComponent,
    Sidebar,
    DashboardPage,
    FooterComponent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  margin-top: 5%;
}

div {
  width: 100%;
}
</style>