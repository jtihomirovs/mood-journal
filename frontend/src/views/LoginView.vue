<template>
  <div>
    <section id="login">
      <form @submit.prevent="submitForm">
        <h2>Mood journal 0.1 - login</h2>
        <input
          type="text"
          v-model="login.login"
          placeholder="Username"
          required
        />
        <input
          type="password"
          v-model="login.password"
          placeholder="Password"
          required
        />
        <button type="submit">Log in</button>
        <span id="alert">{{ alert.message }}</span>
      </form>
    </section>

    <FooterComponent />
  </div>
</template>

<script>
import FooterComponent from "@/components/FooterComponent.vue";
import { axios } from "@/common/api.service.js";

export default {
  components: {
    FooterComponent,
  },
  data() {
    return {
      alert: {
        message: "",
      },
      login: {
        login: "",
        password: "",
      },
    };
  },
  methods: {
    async submitForm() {
      if (this.login.login == "" && this.login.password == "") {
        this.alert.message = "Enter username or password!";
      } else {
        axios
          .post("http://127.0.0.1:8000/api/account/login/", {
            username: this.login.login,
            password: this.login.password,
          })
          .then((response) => {
            window.localStorage.setItem("logged", true);
            window.localStorage.setItem("user_id", response.data.user_id);
            window.localStorage.setItem("first_name", response.data.name);
            window.localStorage.setItem("last_name", response.data.last_name);
            window.location.href = "/";
          })
          .catch((error) => {
            console.log(error);
            this.alert.message = "Username or password is invalid!";
          });
      }
    },
  },
};
</script>

<style scoped>
html,
body {
  width: 100%;
  height: 100%;
  margin: 0px;
  font-family: "Work Sans", sans-serif;
}

body {
  background-size: cover;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #fff;
}

section {
  background-color: #2a2a2e;
  width: 500px;
  min-height: 25%;
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
}
form {
  display: flex;
  flex-direction: column;
  padding: 15px;
}
h2 {
  font-family: "Archivo Black", sans-serif;
  color: #e0dada;
  margin-left: auto;
  margin-right: auto;
}

.info {
  width: 100%;
  padding: 1em 5px;
  text-align: center;
  min-height: 45px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.info.error {
  border: 1px solid #a90e0;
  background-color: #ff3c41;
  color: #a90e0;
}

.info p {
  margin: auto;
  padding: 5px;
}
.info.good {
  border: 1px solid #416d50;
  background-color: #47cf73;
  color: #416d50;
}

input {
  height: 35px;
  padding: 5px 5px;
  margin: 10px 0px;
  background-color: #e0dada;
  border: none;
}
button {
  height: 40px;
  padding: 5px 5px;
  margin: 10px 0px;
  font-weight: bold;
  background-color: #be5256;
  border: none;
  color: #e0dada;
  cursor: pointer;
  font-size: 16px;
}
button:hover {
  background-color: #711f1b;
}

@-webkit-keyframes shake {
  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }
  10%,
  30%,
  50%,
  70%,
  90% {
    -webkit-transform: translate3d(-10px, 0, 0);
    transform: translate3d(-10px, 0, 0);
  }
  20%,
  40%,
  60%,
  80% {
    -webkit-transform: translate3d(10px, 0, 0);
    transform: translate(10px, 0, 0);
  }
}

.shake {
  animation-name: shake;
  animation-duration: 1s;
  /*animation-fill-mode: both;*/
}

#alert {
  color: #ff3333;
}

@media screen and (max-width: 780px) {
  section {
    width: 90%;
  }
}
</style>