<template>
  <div class="hello">
    <h1>Place your text</h1>
    <input class="input_delay" v-model="text" type="text" @keyup="handleInputDebounced" />
    <span :class="{ saving__fade: saving.show, saving: !saving.show }">
      {{ saving.msg }}
    </span>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import { debounce } from "lodash";
export default {
  name: "InputDelay",
  props: {
    timeout: {
      type: Number,
      default: 2000,
    },
  },
  data: () => ({
    text: "",
  }),
  methods: {
    handleInput() {
      this.setSaving(true);
      this.callAPI(this.text);
    },
    ...mapActions(["setSaving", "callAPI"]),
  },
  computed: {
    handleInputDebounced() {
      console.log("debounced by ...", this.timeout);
      return debounce(this.handleInput.bind(this), this.timeout);
    },
    ...mapState(["saving"]),
  },
};
</script>

<style scoped>
.saving {
  display: none;
}
body{
  background: #F6BF89
}

* {
  font-family: Arial, Helvetica, sans-serif;
}
.saving__fade {
  display: block;
  
  color: black;
  animation: fadeIn linear 7s;
}
span {
  color: lightblue;
}
</style>
