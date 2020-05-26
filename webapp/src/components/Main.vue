<template>
  <v-container class="main_container" v-if="loaded">
    <div class="background" :style="background"></div>
    <div class="abs_child">
      <v-slider v-model="current_step" :step="wordcloud.length" ticks="always" thumb-label="always" :max="(wordcloud.length-1)*10">
        <template v-slot:thumb-label="{ value }">{{ wordcloud[(value/10)].date }}</template>
      </v-slider>
    </div>
  </v-container>
</template>

<script>
import { compare } from "../service/datecompare";
import { fetch_wordcloud_files } from "../service/api";
export default {
  name: "Main",
  mounted() {
    let self = this;
    fetch_wordcloud_files().then(function(res) {
      self.wordcloud = res
        .map(function(each) {
          return {
            date: each.date,
            id: each.id
          };
        })
        .sort(compare);
      console.log(self.wordcloud);
      self.loaded = true
    });
  },
  data: () => ({
    loaded: false,
    wordcloud: [],
    current_step: 0
  }),
  computed: {
    background() {
      console.log(this.wordcloud[this.current_step/10])
      console.log("background: url('https://files.de-1.osf.io/v1/resources/vej5u/providers/osfstorage/"+this.wordcloud[this.current_step/10]['id']+"') no-repeat center center;")
      return "background: url('https://files.de-1.osf.io/v1/resources/vej5u/providers/osfstorage/"+this.wordcloud[this.current_step/10]['id']+"') no-repeat center center;"
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
  position: absolute;
  display: flex;
  margin-top: -100px;
  width: 80%;
}
.background {
  min-width: 100%;
  min-height: 100%;
  opacity: 0.3;
}
</style>