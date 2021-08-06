<template>
  <div id="app">
    <h1>Place your text</h1>
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
