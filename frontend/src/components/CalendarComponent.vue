<template>
  <DatePicker
    is-expanded
    class="dtstyle"
    :attributes="attributes"
    :max-date="new Date()"
    @dayclick="onDayClick"
  />
</template>

<script>
import { axios } from "@/common/api.service.js";
import { DatePicker } from "v-calendar";
import "v-calendar/dist/style.css";

export default {
  emits: ["clicked"],
  components: {
    DatePicker,
  },
  data() {
    return {
      moodObject: {},
      responseMoodData: null,
      days: [],
      selectedDayOnCalendar: {},
      attributes: [],
    };
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/mood/");
        this.responseMoodData = response.data;

        for (let moodItem of this.responseMoodData) {
          this.moodObject = {};

          // Load data into object
          this.moodObject.dot = "red";
          this.moodObject.dates = new Date(
            moodItem.mood_date
          ).toLocaleDateString("en-US");
          this.moodObject.time = new Date(
            moodItem.mood_date
          ).toLocaleTimeString("lv-LV");
          this.moodObject.dateLV = new Date(
            moodItem.mood_date
          ).toLocaleDateString("lv-LV");
          this.moodObject.mood = moodItem.mood;
          this.moodObject.weather = moodItem.weather;
          this.moodObject.health = moodItem.health;
          this.moodObject.activity = moodItem.activity;
          this.moodObject.note = moodItem.note;
          this.moodObject.popover = {
            label: `
            Mood: ${moodItem.mood},
            Weather: ${moodItem.weather},
            Health: ${moodItem.health},
            Activity: ${moodItem.activity}
            `,
          };
          // push the object to Array
          this.attributes.push(this.moodObject);
        }
      } catch (error) {
        console.log(error.response);
      }
    },
    onDayClick(day) {
      // Add current time to selected day object
      var currentTime = new Date();

      var offset = currentTime.getTimezoneOffset() / -60;

      var selectedDate = day.date;
      var selectedDateWithTime = new Date(
        selectedDate.setHours(
          currentTime.getHours() + offset,
          currentTime.getMinutes()
        )
      );

      // If selected day on calendar is found in response data, do this day data rendering to side component
      if (
        this.attributes.some(
          (e) => e.dates === day.date.toLocaleDateString("en-US")
        )
      ) {
        // When user clicks on day, send day data to parent to pass this data to sibling component
        let filterValue = day.date.toLocaleDateString("en-US");
        let filteredMoodList = this.attributes.filter((val) =>
          val.dates.includes(filterValue)
        );
        this.$emit("clicked", { filteredMoodList, selectedDateWithTime });
      }
      // Otherwise
      else {
        let filteredMoodList = [];
        this.$emit("clicked", { filteredMoodList, selectedDateWithTime });
      }
    },
    // Disable future dates for mood functionality
    disableFutureDates() {
      // find calendar element by class .vc-weeks
      let calendar = this.$el.querySelector(".vc-weeks");
      // find calendars inner elements with .is-disabled
      let futureDates = calendar.querySelectorAll(".is-disabled");
      // iterate through elements and disable pointer on these dates
      for (let i = 0; i < futureDates.length; i++) {
        futureDates[i].style.cssText = "pointer-events:none";
      }
    },
  },
  mounted() {
    this.disableFutureDates();
  },
  created() {
    this.getData();
  },
};
</script>

<style>
</style>