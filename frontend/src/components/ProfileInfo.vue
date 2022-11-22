<template>
  <div>
    <div class="tasks_container">
      <div class="tasks_content">
        <h1>Profile info:</h1>
        <p>Username: {{ responseData ? responseData.username : "" }}</p>
        <p>Email: {{ responseData ? responseData.email : "" }}</p>
        <p>Fist name: {{ responseData ? responseData.first_name : "" }}</p>
        <p>Last name: {{ responseData ? responseData.last_name : "" }}</p>
        <p>Phone name: {{ responseData ? responseData.phone_number : "" }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  data() {
    return {
      responseData: null,
    };
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/account/profile/"
        );
        this.responseData = response.data;
      } catch (error) {
        console.log(error.response);
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style>
.tasks_container {
  float: right;
}
</style>