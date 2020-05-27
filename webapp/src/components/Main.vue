<template>
<div style="width:100%;height:100%;">
  <v-container class="main_container" v-if="!loading">
    <div class="background" :style="background"></div>
    <div class="abs_child">
      <v-slider v-model="current_step" step="1" ticks="always" thumb-label="always" :max="wordcloud.length-1">
        <template v-slot:thumb-label="{ value }">{{ wordcloud[value].date }}</template>
      </v-slider>
    </div>
  </v-container>
      <v-dialog
      v-model="loading"
      hide-overlay
      persistent
      width="300"
    >
      <v-card
        color="primary"
        dark
      >
        <v-card-text>
          Please stand by...
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
</div>
</template>

<script>
import { compare } from "../service/datecompare";
import { fetch_wordcloud_files, fetch_emotion_files } from "../service/api";
import { load_data } from '../service/dataloader'
export default {
  name: "Main",
  mounted() {
    let self = this;
    fetch_wordcloud_files().then(function(res) {
      self.wordcloud = res.sort(compare);
      self.loading = false
    });
  },
  data: () => ({
    loading: true,
    wordcloud: [],
    emotions:[],
    current_step: 0
  }),
  computed: {
    background() {
      return "background: url('https://files.de-1.osf.io/v1/resources/vej5u/providers/osfstorage/"+this.wordcloud[this.current_step]['id']+"') no-repeat center center;"
    }
  },
  watch: {
    current_step(newVal) {
      self.loading = true
      console.log(newVal)
      load_data(this.emotions[0].id).then(function(res) {
        console.log(res)
      })
    }
  },
  methods: {
    updatebg() {
      this.$el.style.setProperty("--url", this.url);
    }
  }
};
</script>
<style scoped>
.main_container {
  min-width: 100%;
  height: 100%;
  text-align: center;
  align-items: center;
}
.abs_child {
  display: flex;
  margin-top: -100px;
  width: 95%;
  margin-left: auto;
  margin-right: auto;
}
.background {
  min-width: 100%;
  min-height: 100%;
  opacity: 0.4;
}
</style>