<template>
  <sidebar-menu :menu="menu" />
</template>

<script>
import "@fortawesome/fontawesome-free/css/all.css";

export default {
  data() {
    return {
      menu: [
        {
          header: "Mood Journal",
          hiddenOnCollapse: true,
        },
        {
          href: "/",
          title: "Dashboard",
          icon: "fa fa-user",
        },
        {
          href: "/login/",
          title: "Login",
          icon: "fa fa-chart-area",
        },
        {
          href: "/statistics/",
          title: "Statistics",
          icon: "fa fa-chart-area",
        },
        {
          href: "/logout/",
          title: "Log Out",
          icon: "fa fa-sign-out",
        },
      ],
    };
  },
  created() {
    // If user is logged then remove login from side menu
    if (window.localStorage.getItem("logged")) {
      this.menu.splice(
        this.menu.findIndex(({ title }) => title == "Login"),
        1
      );
    }
  },
};
</script>