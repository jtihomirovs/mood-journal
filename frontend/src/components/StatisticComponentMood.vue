<template>
  <div>
    <h4>Total day count grouped by mood data</h4>
    <DoughnutChart :chartData="moodData" />
  </div>
</template>

<script>
import { DoughnutChart } from "vue-chart-3";
import { Chart, registerables } from "chart.js";
import { axios } from "@/common/api.service.js";

Chart.register(...registerables);

export default {
  name: "StatisticComponent",
  components: { DoughnutChart },
  data() {
    return {
      moodData: {
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor: [
              "#77CEFF",
              "#0079AF",
              "#123E6B",
              "#97B0C4",
              "#A5C8ED",
            ],
          },
        ],
      },
    };
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/stats/");

        for (let [key, value] of Object.entries(response.data.mood)) {
          this.moodData.labels.push(this.formatLabel(key));
          this.moodData.datasets[0].data.push(value);
        }
      } catch (error) {
        console.log(error.response);
      }
    },
    formatLabel(label) {
      let labelFirstUpper = label[0].toUpperCase() + label.substring(1);
      let labelDivided = labelFirstUpper.replace(/_/g, " ");
      return labelDivided;
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style>
</style>