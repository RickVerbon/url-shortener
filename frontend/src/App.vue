<template>
  <div id="app" class="w-full h-full flex flex-col">
    <router-view class="flex-grow"/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Ensure the app container takes full width and height */
html, body, #app {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}
</style>