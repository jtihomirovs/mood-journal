<template>
  <div class="container pt-5">
    <div class="row">
      <div class="col-md-6">
        <h4>Your calendar</h4>
      </div>
      <div class="col-md-6">
        <h4>Mood entries</h4>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <CalendarComponent @clicked="onDayClick" />
      </div>
      <div class="col-md-6 text-left">
        <MoodComponent v-model:moodProperty="moodList" />
      </div>
    </div>
  </div>
</template>

<script>
import MoodComponent from "@/components/MoodComponent.vue";
import CalendarComponent from "@/components/CalendarComponent.vue";

export default {
  name: "ProfilePage",
  components: {
    CalendarComponent,
    MoodComponent,
  },
  data() {
    return {
      moodList: {},
    };
  },
  methods: {
    onDayClick(value) {
      this.moodList = value;
    },
  },
};
</script>
    
<style scoped>
</style>