<template>
  <v-app :style="main_style">
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">COVID-19 Sentiment Analysis</div>

      <v-spacer></v-spacer>

      <v-btn href="https://github.com/vuetifyjs/vuetify/releases/latest" target="_blank" text>
        <span class="mr-2">About</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <Main />
    </v-content>

    <v-footer dark padless>
      <v-card class="flex" flat tile>
        <v-card-title class="primary lighten-1">
          <strong class="subheading">United we stand, divided we fall. - Aesop</strong>

          <v-spacer></v-spacer>
        </v-card-title>

        <v-card-text class="py-2 white--text text-center">
          {{ new Date().getFullYear() }} —
          <strong>Sentiment Analysis Team</strong>
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
    main_style:"opacity:0.4; background: url('https://ndownloader.figshare.com/files/22793075/preview/22793075/preview.jpg') no-repeat center center;" 
  })
};
</script>
