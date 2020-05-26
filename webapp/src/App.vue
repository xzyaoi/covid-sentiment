<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">COVID-19 Sentiment Analysis</div>

      <v-spacer></v-spacer>

      <v-btn href="https://blog.yaonotes.org/2020/05/22/covid-twitter/" target="_blank" text>
        <span class="mr-2">About</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <Main style="width:100%;height:100%;"/>
    </v-content>

    <v-footer dark padless>
      <v-card class="flex" flat tile>
        <v-card-title class="primary lighten-1">
          <strong class="subheading">United we stand, divided we fall. - Aesop</strong>
          <v-spacer></v-spacer>
        </v-card-title>

        <v-card-text class="py-2 white--text text-center">
          {{ new Date().getFullYear() }} —
          <strong>Yingying Chen, Songyi Han, <a href="https://blog.yaonotes.org">Xiaozhe Yao</a></strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
import Main from "./components/Main";

export default {
  name: "App",

  components: {
    Main
  },

  data: () => ({
  })
};
</script>

<style scoped>
.main_content {
  position:absolute;
}
.pdiv {
  position: relative;
}
</style>
