<template>
  <v-container>
    <v-row justify="start">
      <v-col>
        <h2 class="display-2">出勤ピーポー</h2>
      </v-col>
      <v-col cols="2">
        <v-btn
          class="accent"
          @click="reloadShukkin()"
        >
          Refresh
        </v-btn>
      </v-col>
    </v-row>
    <v-row justify="start">
      <v-col
        cols="4"
        v-for="shukkin in shukkins"
        v-bind:key="shukkin.item_id">
        <v-card
          class="pa-2"
          outlined
        >
          <v-card-text>
            <v-row justify="space-between" class="mb-2">
              <v-col>
                <span class="caption pb-3">{{shukkin.item_id}}</span>
              </v-col>
              <v-col class="text-right">
                <span class="caption pb-3">{{formatTimestamp(shukkin.created_at)}}</span>
              </v-col>
            </v-row>
            <p class="display-1 text--primary">出勤なう</p>
            <v-row justify="space-between" align="center">
              <v-col cols="5">
                <v-btn
                  icon
                  @click="leave(shukkin.item_id)">
                  <v-icon>mdi-heart</v-icon>
                </v-btn>
                <span class="ml-0 subheading">{{shukkin.leaved}}</span>
              </v-col>
              <v-col cols="7" class="text-right">
                <span class="title">{{shukkin.username}}</span>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  name: "ShukkinList",
  data() {
    return {
      shukkins: null
    };
  },
  created: function() {
    if (!this.$store.state.url) return;
    axios
      .get(this.$store.state.url + "/shukkin")
      .then(res => {
        this.shukkins = res.data;
      });
  },
  methods: {
    formatTimestamp (value) {
      return moment(String(value)).format("YYYY/MM/DD hh:mm")
    },
    reloadShukkin() {
      if (!this.$store.state.url) return
      axios
        .get(this.$store.state.url + "/shukkin")
        .then(res => {
          this.shukkins = res.data;
        });
    },
    taisha(item_id) {
      axios
        .patch(this.$store.state.url + "/shukkin/" + item_id)
        .then(() => {
          axios
            .get(this.$store.state.url + "/shukkin")
            .then(res => {
              this.shukkins = res.data;
            });
        });
    }
  }
}
</script>
