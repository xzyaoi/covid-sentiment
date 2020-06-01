<template>
  <div style="width:100%;height:100%;">
    <v-container class="main_container" v-if="!loading">
      <div class="background" :style="background">
        <div id="main_plot"></div>
        <v-slider
          class="abs_child"
          v-model="current_step"
          step="1"
          ticks="always"
          thumb-label="always"
          :max="wordcloud.length-1"
        >
          <template v-slot:thumb-label="{ value }">{{ wordcloud[value].date }}</template>
        </v-slider>
      </div>
    </v-container>
    <v-dialog v-model="loading" hide-overlay persistent width="300">
      <v-card color="primary" dark>
        <v-card-text>
          Please stand by...
          <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { compare } from "../service/datecompare";
import { fetch_wordcloud_files } from "../service/api";
import Plotly from "plotly.js-dist";

export default {
  name: "Main",
  mounted() {
    let self = this;
    fetch_wordcloud_files().then(function(res) {
      self.wordcloud = res.sort(compare);
      self.loading = false;
      self.plot('https://raw.githubusercontent.com/xzyaoi/covid-sentiment/master/data/5-24.csv')
    });
  },
  data: () => ({
    loading: true,
    wordcloud: [],
    emotions: [],
    current_step: 0,
    layout: {
      autosize: true,
      paper_bgcolor: "rgba(0,0,0,0)",
      plot_bgcolor: "rgba(0,0,0,0)"
    }
  }),
  computed: {
    background() {
      return (
        "background: url('https://files.de-1.osf.io/v1/resources/vej5u/providers/osfstorage/" +
        this.wordcloud[this.current_step]["id"] +
        "') no-repeat center center;"
      );
    }
  },
  watch: {
    current_step(newVal) {
      this.plot('https://raw.githubusercontent.com/xzyaoi/covid-sentiment/master/data/'+this.wordcloud[newVal].date+'.csv')
    }
  },
  methods: {
    updatebg() {
      this.$el.style.setProperty("--url", this.url);
    },
    plot(url) {
      let self = this
      Plotly.d3.csv(
        url,
        function(err, rows) {
          function unpack(rows, key) {
            return rows.map(function(row) {
              return row[key];
            });
          }

          var happiness = {
            type: "scatter",
            mode: "lines",
            name: "Hapiness",
            x: unpack(rows, "time"),
            y: unpack(rows, "happy"),
            line: { color: "#B5495B" }
          };
          var bad = {
            type: "scatter",
            mode: "lines",
            name: "Bad",
            x: unpack(rows, "time"),
            y: unpack(rows, "bad"),
            line: { color: "#26453D" }
          };
          var polarity = {
            type: "scatter",
            mode: "lines",
            name: "Polarity",
            x: unpack(rows, "time"),
            y: unpack(rows, "polarity"),
            line: { color: "#268785" }
          };
          var encouraged = {
            type: "scatter",
            mode: "lines",
            name: "Encouraged",
            x: unpack(rows, "time"),
            y: unpack(rows, "encouraged"),
            line: { color: "#FFB11B" }
          };
          var data = [happiness, bad, polarity, encouraged];

          Plotly.newPlot("main_plot", data, self.layout);
        }
      );
    }
  }
};
</script>
<style scoped>
.main_container {
  min-width: 100%;
  height: 100%;
  display:flex;
  text-align: center;
  align-items: center;
}
.background {
  width: 100%;
  height: 100%;
  display:flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
#main_plot {
  background: rgba(255,255,255,0.8);
  width: 95%;
  margin-top: 20px;
}
.abs_child {
  width: 95%;
}
</style>