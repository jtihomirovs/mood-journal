<template>
  <div id="app">
    <HeaderComponent />
    <Sidebar />

    <div class="container pt-5">
      <carousel :items-to-show="1">
        <Slide v-for="slide in components" :key="slide">
          <component :is="slide"></component>
        </Slide>

        <template #addons>
          <navigation />
          <pagination />
        </template>
      </carousel>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent.vue";
import Sidebar from "@/components/SideBar.vue";
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Pagination, Navigation } from "vue3-carousel";
import StatisticComponentMood from "@/components/StatisticComponentMood.vue";
import StatisticComponentWeather from "@/components/StatisticComponentWeather.vue";
import StatisticComponentHealth from "@/components/StatisticComponentHealth.vue";
import StatisticComponentActivity from "@/components/StatisticComponentActivity.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  name: "App",
  components: {
    HeaderComponent,
    Sidebar,
    Carousel,
    Slide,
    Pagination,
    Navigation,
    StatisticComponentMood,
    StatisticComponentWeather,
    StatisticComponentHealth,
    StatisticComponentActivity,
    FooterComponent,
  },
  data() {
    return {
      components: [
        "StatisticComponentMood",
        "StatisticComponentWeather",
        "StatisticComponentHealth",
        "StatisticComponentActivity",
      ],
    };
  },
};
</script>

<style>
.carousel__item {
  min-height: 200px;
  width: 100%;
  background-color: var(--vc-clr-primary);
  color: var(--vc-clr-white);
  font-size: 20px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
  background-color: #1e1e21;
}

.carousel__pagination-button {
  background-color: #6c757d;
}

.carousel__pagination-button--active {
  background-color: #1e1e21;
}
</style>