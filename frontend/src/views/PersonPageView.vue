<template>
  <div id="app">
    <HeaderComponent />

    <Sidebar />

    <FooterComponent />

    <div class="container pt-5">
      <div class="row">
        <div class="col-md-6 text-right pr-5">
          <img width="150" height="150" v-bind:src="image" alt="Red dot" />
        </div>
        <div v-if="!edit" class="col-md-6 text-left">
          <h4>Your profile:</h4>
          <div>Username: {{ userName ? userName : "Not provided" }}</div>
          <div>Email: {{ email ? email : "Not provided" }}</div>
          <div>First name: {{ firstName ? firstName : "Not provided" }}</div>
          <div>Last name: {{ lastName ? lastName : "Not provided" }}</div>
          <div>Phone: {{ phone ? phone : "Not provided" }}</div>
          <button class="btn btn-light" @click="$router.go(-1)">Back</button>
          <button class="btn btn-success ml-2" @click="edit = !edit">
            Edit profile fields
          </button>
        </div>
        <div v-if="edit" class="col-md-6 text-left">
          <form>
            <h4>Edit your personal data</h4>
            <div class="form-group">
              <label for="inputEmail">Email address</label>
              <input
                v-model="email"
                type="email"
                class="form-control"
                id="inputEmail"
                aria-describedby="emailHelp"
                placeholder="Enter email"
              />
            </div>
            <div class="form-group">
              <label for="firstName">First name</label>
              <input
                v-model="firstName"
                type="text"
                class="form-control"
                id="firstName"
                placeholder="First name"
              />
            </div>
            <div class="form-group">
              <label for="lastName">Last name</label>
              <input
                v-model="lastName"
                type="text"
                class="form-control"
                id="lastName"
                placeholder="Last name"
              />
            </div>
            <div class="form-group">
              <label for="phone">Phone</label>
              <input
                v-model="phone"
                type="text"
                class="form-control"
                id="phone"
                placeholder="Phone"
              />
            </div>
            <div v-if="!file" class="form-group">
              <label for="image">Image</label>
              <input
                @change="handleFileUpload($event)"
                type="file"
                class="form-control"
                id="image"
                placeholder="Image"
              />
            </div>
            <div v-else>
              <img class="previewImage float-left" :src="imgUrl" />
              <button @click="removeImage" class="btn btn-link float-left">
                Remove image
              </button>
            </div>
            <!-- <div v-if="!previewImage" class="form-group">
              <label for="image">Image</label>
              <input @change="onFileChange" type="file" class="form-control" id="image" placeholder="Image">
            </div>
            <div v-else>
              <img class="previewImage float-left" :src="previewImage" />
              <button @click="removeImage" class="btn btn-link float-left">Remove image</button>
            </div> -->
            <div class="row pl-3">
              <button @click="edit = !edit" class="btn btn-light float-left">
                Close edit
              </button>
              <button
                @click="updatePersonInfo()"
                type="submit"
                class="btn btn-success float-right ml-2"
              >
                Submit
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent.vue";
import Sidebar from "@/components/SideBar.vue";
import FooterComponent from "@/components/FooterComponent.vue";
import { axios } from "@/common/api.service.js";

export default {
  name: "App",
  components: {
    HeaderComponent,
    Sidebar,
    FooterComponent,
  },
  data() {
    return {
      userName: "",
      email: "",
      firstName: "",
      lastName: "",
      phone: "",
      image: "",
      file: "",
      edit: false,
      imgUrl: "",
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];

      this.imgUrl = URL.createObjectURL(this.file);
    },
    removeImage() {
      this.file = "";
      this.imgUrl = "";
    },
    // onFileChange(e) {
    //   var files = e.target.files || e.dataTransfer.files;
    //   if (!files.length) return;
    //   this.file = files[0]
    //   this.createImage(this.file);
    // },
    // createImage(file) {
    //   //var image = new Image();
    //   var reader = new FileReader();
    //   var vm = this;

    //   reader.onload = (e) => {
    //     vm.previewImage = e.target.result;
    //   };
    //   reader.readAsDataURL(file);
    // },
    // removeImage: function () {
    //   this.previewImage = '';
    // },
    async getData() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/account/profile/"
        );
        this.userName = response.data.username;
        this.email = response.data.email;
        this.firstName = response.data.first_name;
        this.lastName = response.data.last_name;
        this.phone = response.data.phone_number;
        this.image = response.data.image;
      } catch (error) {
        console.log(error.response);
      }
    },
    async updatePersonInfo() {
      // Initialize the form data
      let formData = new FormData();

      // Add data to the form
      formData.append("email", this.email);
      formData.append("first_name", this.firstName);
      formData.append("last_name", this.lastName);
      formData.append("phone_number", this.phone);
      formData.append("image", this.file);

      axios
        .put("http://127.0.0.1:8000/api/account/profile/", formData)
        .then(() => {
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getData();
  },
};
</script>


<style>
.previewImage {
  width: 50%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}
</style>