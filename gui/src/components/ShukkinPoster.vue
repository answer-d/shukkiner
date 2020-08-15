<template>
  <v-container>
    <v-row justify="center" class="mb-4">
      <h2 class="display-1">ここから出勤してもろて</h2>
    </v-row>
    <v-row justify="start">
      <v-col cols="3">
        <v-text-field
          outlined
          v-model="place"
          label="勤務場所"
        ></v-text-field>
      </v-col>
      <v-col cols="3">
        <v-text-field
          outlined
          v-model="leaving_expected_time"
          label="退社予定時刻"
        ></v-text-field>
      </v-col>
      <v-col cols="2">
        <v-text-field
          v-model="username"
          label="おなまえ"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="2" class="text-center">
        <v-btn
          large
          color="indigo"
          dark
          @click="postShukkin()">
          Post
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    place: "",
    leaving_expected_time: "",
    username: "",
  }),
  methods: {
    postShukkin() {
      axios
        .post(this.$store.state.url + "/shukkin", {
          "username": this.username,
          "place": this.place,
          "leaving_expected_time": this.leaving_expected_time,
        })
        .catch(err => {
          alert(err)
        });
    }
  }
}
</script>
