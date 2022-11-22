import { createApp } from 'vue';
import App from './App.vue';

// import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import VueSidebarMenu from 'vue-sidebar-menu';
import SetupCalendar from 'v-calendar';

import 'bootstrap'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css';
// import 'bootstrap/dist/css/bootstrap.css';
// import 'bootstrap-vue/dist/bootstrap-vue.css';


import router from "./router";

const app = createApp(App)
// app.use(BootstrapVue)
// app.use(BootstrapVueIcons)
app.use(VueSidebarMenu)
app.use(router)
app.use(SetupCalendar, {})
app.mount('#app')