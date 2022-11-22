<template>
  <header>
    <div class="header">
      <span class="greeting"
        >Hi,
        <router-link :to="{ name: 'Profile' }" exact-active-class="exact-active"
          >{{ first_name }} {{ last_name }}</router-link
        ></span
      >
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      first_name: "",
      last_name: "",
    };
  },
  beforeMount() {
    this.first_name = window.localStorage.getItem("first_name");
    this.last_name = window.localStorage.getItem("last_name");
  },
};
</script>

<style scoped>
.header {
  position: fixed;
  text-align: right;
  top: 0;
  left: 0;
  width: 100%;
  height: 40px;
  opacity: 100%;
  background-color: #414242;
}

.greeting {
  display: inline-block;
  margin-top: 0.2%;
  margin-right: 5%;
  color: white;
}
a,
a.router-link-active,
a.router-link-exact-active {
  color: white;
  text-decoration: underline;
}
a:hover {
  color: rgb(182, 174, 174);
}
</style>