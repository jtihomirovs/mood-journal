/* eslint-disable */
import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import LoginView from "../views/LoginView.vue";
import StatisticView from "../views/StatisticView.vue";
import PersonPageView from "../views/PersonPageView.vue";
import LogOut from "../components/LogOut.vue";
import NotFound from "../views/NotFoundView.vue";
import { axios } from "@/common/api.service.js";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "LoginView",
    component: LoginView,
  },
  {
    path: "/statistics",
    name: "Statistics",
    component: StatisticView,
  },
  {
    path: "/profile",
    name: "Profile",
    component: PersonPageView,
  },
  {
    path: "/logout",
    name: "LogOut",
    component: LogOut,
  },
  {
    path: "/:catchAll(.*)",
    name: "page-not-found",
    component: NotFound,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

const getSession = async () => {
  try {
    const resp = await axios.get('http://127.0.0.1:8000/api/account/session/');
    return resp;
  } catch (err) {
    console.error('err: ', err);
  }
};

router.beforeEach(async (to, from) => {

  // Set title from route
  document.title = to.name;

  // Get session status
  const sessionStatus = await getSession();

  // If user is not authorized && user visits login page, return login page
  if (
    sessionStatus.status === 204 &&
    // Avoid an infinite redirect
    to.name !== 'LoginView'
  ) {
    return { name: 'LoginView' }
    // If user is authorized && user try to open login page, return to dashboard page
  } else if (
    sessionStatus.status === 200 &&
    to.name == 'LoginView'
  ) {
    return { name: 'Home' }
    // If we have missed some router logic, this should help in debug process
  } else {
  }
})

export default router;