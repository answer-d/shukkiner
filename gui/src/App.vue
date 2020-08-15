<template>
  <v-app>
    <v-app-bar
      app
      color="blue"
      dark
    >
      <v-btn icon>
        <v-icon>mdi-alpha-s-box</v-icon>
      </v-btn>
      <v-toolbar-title>Shukkiner</v-toolbar-title>      
    </v-app-bar>

    <v-content>
      <EndpointUrl/>
      <ShukkinPoster/>
      <ShukkinList/>
    </v-content>
  </v-app>
</template>

<script>
import EndpointUrl from "./components/EndpointUrl"
import ShukkinList from "./components/ShukkinList"
import ShukkinPoster from "./components/ShukkinPoster"

export default {
  name: "App",
  components: {
    EndpointUrl,
    ShukkinList,
    ShukkinPoster,
  },
  data: () => ({
    //
  }),
};
</script>
