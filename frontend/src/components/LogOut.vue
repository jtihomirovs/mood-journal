<script>
import { axios } from "@/common/api.service.js";

export default {
  methods: {
    async performLogOut() {
      axios
        .get("http://127.0.0.1:8000/api/account/logout/")
        .then(() => {
          // Clear local storage after logout
          window.localStorage.setItem("user_id", "");
          window.localStorage.setItem("first_name", "");
          window.localStorage.setItem("last_name", "");
          this.$router.push("/login/");
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  created() {
    // Perform logout on /api/account/logout/ hit
    this.performLogOut();
  },
};
</script>