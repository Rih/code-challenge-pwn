<template>
  <div id="app">
    <InputDelay />
  </div>
</template>

<script>
import InputDelay from "./components/InputDelay.vue";

export default {
  name: "App",
  components: {
    InputDelay,
  },
  data: () => ({
    value: "",
  }),
  methods: {
    handleInputDebounced(t) {
      console.log({ t });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
