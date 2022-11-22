<template>
  <div>
    <div v-if="showReg">
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="mood">Date and time:</label>
          <input
            id="datetime-mood-input"
            type="datetime-local"
            class="form-control"
            :value="
              moodProperty.selectedDateWithTime
                ? moodProperty.selectedDateWithTime.toISOString().slice(0, -5)
                : toISOLocal(new Date()).slice(0, -13)
            "
            :max="toISOLocal(new Date()).slice(0, -10)"
          />
        </div>
        <div class="form-group">
          <label for="mood">What is your mood today:</label>
          <div>
            <a
              class="emoji-box"
              v-bind:class="{ selectedEmoji: selectedMood == emoji.id }"
              v-for="emoji in moodEmojis"
              :key="emoji.id"
              @click="handleSelectItem(emoji)"
              >{{ emoji.icon }}</a
            >
          </div>
        </div>
        <div class="form-group">
          <label for="weather">Current weather:</label>
          <div>
            <a
              class="emoji-box"
              v-bind:class="{ selectedEmoji: selectedWeather == emoji.id }"
              v-for="emoji in weatherEmojis"
              :key="emoji.id"
              @click="handleSelectItem(emoji)"
              >{{ emoji.icon }}</a
            >
          </div>
        </div>
        <div class="form-group">
          <label for="health">Current health:</label>
          <div>
            <a
              class="emoji-box"
              v-bind:class="{ selectedEmoji: selectedHealth == emoji.id }"
              v-for="emoji in healthEmojis"
              :key="emoji.id"
              @click="handleSelectItem(emoji)"
              >{{ emoji.icon }}</a
            >
          </div>
        </div>
        <div class="form-group">
          <label for="activities">Activities today:</label>
          <div>
            <a
              class="emoji-box"
              v-bind:class="{ selectedEmoji: selectedActivity == emoji.id }"
              v-for="emoji in activityEmojis"
              :key="emoji.id"
              @click="handleSelectItem(emoji)"
              >{{ emoji.icon }}</a
            >
          </div>
        </div>
        <div class="form-group">
          <label for="note">Note about mood:</label>
          <div>
            <input
              v-model="note"
              type="text"
              id="note"
              name="note"
              placeholder="Add a note (optional)"
              style="height: 60px; width: 200px"
            />
          </div>
        </div>        
        <button
          type="submit"
          class="btn btn-secondary"
          @click="
            () => {
              showReg = !showReg;
              showStats = !showStats;
            }
          "
        >
          Back
        </button>
        <button
          type="submit"
          class="btn btn-success ml-1"
          id="postRecord"
          @click="postNewMoodRecord()"
          disabled
        >
          Submit
        </button>
      </form>
    </div>

    <div v-if="showStats" class="mood_container">
      <div class="mood">
        <div
          v-if="
            moodProperty.filteredMoodList &&
            moodProperty.filteredMoodList.length > 0
          "
        >
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Date</th>
                <th scope="col">Time</th>
                <th scope="col">Mood</th>
                <th scope="col">Weather</th>
                <th scope="col">Health</th>
                <th scope="col">Activity</th>
                <th scope="col">Note</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="moodRec in moodProperty.filteredMoodList"
                :key="moodRec.message"
              >
                <td>{{ moodRec.dateLV }}</td>
                <td>{{ moodRec.time }}</td>
                <td>{{ getEmoji(moodRec.mood, "moodEmojis") }}</td>
                <td>{{ getEmoji(moodRec.weather, "weatherEmojis") }}</td>
                <td>{{ getEmoji(moodRec.health, "healthEmojis") }}</td>
                <td>{{ getEmoji(moodRec.activity, "activityEmojis") }}</td>
                <td>{{ moodRec.note }}</td>
              </tr>
            </tbody>
          </table>
          <div class="row">
            <div class="col-md-5">
              <div>Total days Mood score:</div>
              <div>Total days Weather score:</div>
              <div>Total days Health score:</div>
              <div>Total days Activity score:</div>
            </div>
            <div class="col-md-7 pl-0">
              <progress id="mood" max="100" :value="moodScore">70%</progress>
              {{ moodScore }} %
              <progress id="weather" max="100" :value="weatherScore">
                70%
              </progress>
              {{ weatherScore }} %
              <progress id="health" max="100" :value="healthScore">
                70%
              </progress>
              {{ healthScore }} %
              <progress id="activity" max="100" :value="activityScore">
                70%
              </progress>
              {{ activityScore }} %
            </div>
          </div>
        </div>
        <div v-else>
          There are no mood entries for this day. You may register a new mood
          record.
        </div>
      </div>
      <button
        type="button"
        class="btn btn-success mt-1"
        @click="
          () => {
            showReg = !showReg;
            showStats = !showStats;
          }
        "
      >
        Register mood
      </button>
    </div>
  </div>
</template>

 <style scoped>
.emoji-box {
  font-size: 30px;
  cursor: pointer;
}
.emoji-box:hover,
active,
visited {
  text-decoration: none;
}
.selectedEmoji {
  background-color: #6c757d;
  border-radius: 2px;
  font-size: 30px;
}

.table td,
.table th {
  padding: 0.25rem;
  vertical-align: middle;
}
</style>

 <script>
import { axios } from "@/common/api.service.js";

export default {
  props: {
    moodProperty: {
      filteredMoodList: [],
      day: {},
    },
  },
  name: "moodComponent",
  components: {},
  data() {
    return {
      showReg: false,
      showStats: true,
      showAddNewAct: false,
      user_id: "",
      selectedMood: "",
      selectedWeather: "",
      selectedHealth: "",
      selectedActivity: "",
      note: "",
      moodEmojis: [
        {
          id: "Excited",
          icon: "😍",
        },
        {
          id: "Happy",
          icon: "🙂",
        },
        {
          id: "Neutral",
          icon: "😐",
        },
        {
          id: "Bored",
          icon: "😣",
        },
        {
          id: "Sad",
          icon: "🙁",
        },
        {
          id: "Angry",
          icon: "😡",
        },
      ],
      weatherEmojis: [
        {
          id: "Sunny",
          icon: "🌞",
        },
        {
          id: "Rainy",
          icon: "🌧️",
        },
        {
          id: "Cloudy",
          icon: "⛅",
        },
        {
          id: "Snowy",
          icon: "☃️",
        },
        {
          id: "Windy",
          icon: "🌬️",
        },
      ],
      healthEmojis: [
        {
          id: "Healthy",
          icon: "🤗",
        },
        {
          id: "Sick",
          icon: "🤒",
        },
      ],
      activityEmojis: [
        {
          id: "Work",
          icon: "🔨",
        },
        {
          id: "Free",
          icon: "🐢",
        },
      ],
    };
  },
  computed: {
    moodScore: function () {
      return Math.round(
        this.calculateScore(this.moodProperty.filteredMoodList, "mood")
      );
    },
    weatherScore: function () {
      return Math.round(
        this.calculateScore(this.moodProperty.filteredMoodList, "weather")
      );
    },
    healthScore: function () {
      return Math.round(
        this.calculateScore(this.moodProperty.filteredMoodList, "health")
      );
    },
    activityScore: function () {
      return Math.round(
        this.calculateScore(this.moodProperty.filteredMoodList, "activity")
      );
    },
  },
  methods: {
    calculateScore(moodList, type) {
      if (type == "mood") {
        let score = [];

        for (let moodItem of moodList) {
          if (moodItem.mood == "Excited") {
            score.push(0.5);
          } else if (moodItem.mood == "Happy") {
            score.push(0.3);
          } else if (moodItem.mood == "Neutral") {
            score.push(0.1);
          } else if (moodItem.mood == "Bored") {
            score.push(0.05);
          } else if (moodItem.mood == "Sad") {
            score.push(0.03);
          } else if (moodItem.mood == "Angry") {
            score.push(0.02);
          }
        }
        return (
          (score.reduce(function (a, b) {
            return a + b;
          }, 0) /
            moodList.length) *
          100
        );
      } else if (type == "weather") {
        let score = [];

        for (let moodItem of moodList) {
          if (moodItem.weather == "Sunny") {
            score.push(0.5);
          } else if (moodItem.weather == "Rainy") {
            score.push(0.2);
          } else if (moodItem.weather == "Cloudy") {
            score.push(0.2);
          } else if (moodItem.weather == "Snowy") {
            score.push(0.05);
          } else if (moodItem.weather == "Windy") {
            score.push(0.05);
          }
        }
        return (
          (score.reduce(function (a, b) {
            return a + b;
          }, 0) /
            moodList.length) *
          100
        );
      } else if (type == "health") {
        let score = [];

        for (let moodItem of moodList) {
          if (moodItem.health == "Healthy") {
            score.push(0.8);
          } else if (moodItem.health == "Happy") {
            score.push(0.2);
          }
        }
        return (
          (score.reduce(function (a, b) {
            return a + b;
          }, 0) /
            moodList.length) *
          100
        );
      } else if (type == "activity") {
        let score = [];

        for (let moodItem of moodList) {
          if (moodItem.activity == "Work") {
            score.push(0.3);
          } else if (moodItem.activity == "Free") {
            score.push(0.7);
          }
        }
        return (
          (score.reduce(function (a, b) {
            return a + b;
          }, 0) /
            moodList.length) *
          100
        );
      }
    },
    handleSelectItem(emoji) {
      if (this.moodEmojis.includes(emoji)) {
        this.selectedMood = emoji.id;
      } else if (this.weatherEmojis.includes(emoji)) {
        this.selectedWeather = emoji.id;
      } else if (this.healthEmojis.includes(emoji)) {
        this.selectedHealth = emoji.id;
      } else if (this.activityEmojis.includes(emoji)) {
        this.selectedActivity = emoji.id;
      }
      // on each emoji selection verify if all fields ar filled in
      this.validateForm();
    },
    getEmoji(emoji, type) {
      if (type == "moodEmojis") {
        let obj = this.moodEmojis.find((obj) => obj.id == emoji);
        return obj.icon;
      } else if (type == "weatherEmojis") {
        let obj = this.weatherEmojis.find((obj) => obj.id == emoji);
        return obj.icon;
      } else if (type == "healthEmojis") {
        let obj = this.healthEmojis.find((obj) => obj.id == emoji);
        return obj.icon;
      } else if (type == "activityEmojis") {
        let obj = this.activityEmojis.find((obj) => obj.id == emoji);
        return obj.icon;
      } else {
        console.log("There is an error in getEmoji function");
      }
    },
    validateForm() {
      if (
        document.getElementById("datetime-mood-input").value &&
        this.selectedMood &&
        this.selectedWeather &&
        this.selectedHealth &&
        this.selectedActivity
      ) {
        document.getElementById("postRecord").disabled = false;
      }
    },
    toISOLocal(d) {
      var z = (n) => ("0" + n).slice(-2);
      var zz = (n) => ("00" + n).slice(-3);
      var off = d.getTimezoneOffset();
      var sign = off > 0 ? "-" : "+";
      off = Math.abs(off);

      return (
        d.getFullYear() +
        "-" +
        z(d.getMonth() + 1) +
        "-" +
        z(d.getDate()) +
        "T" +
        z(d.getHours()) +
        ":" +
        z(d.getMinutes()) +
        ":" +
        z(d.getSeconds()) +
        "." +
        zz(d.getMilliseconds()) +
        sign +
        z((off / 60) | 0) +
        ":" +
        z(off % 60)
      );
    },
    async postNewMoodRecord() {
      // Request will be made if only all fields ar filled in
      if (
        document.getElementById("datetime-mood-input").value &&
        this.selectedMood &&
        this.selectedWeather &&
        this.selectedHealth &&
        this.selectedActivity
      ) {
        axios
          .post("http://127.0.0.1:8000/api/mood/", {
            user: this.user_id,
            mood: this.selectedMood,
            weather: this.selectedWeather,
            health: this.selectedHealth,
            activity: this.selectedActivity,
            note: this.note,
            mood_date: document.getElementById("datetime-mood-input").value,
          })
          .then(() => {
            window.location.href = "/";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  beforeMount() {
    this.user_id = window.localStorage.getItem("user_id");
  },
};
</script>