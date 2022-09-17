<template>
<div class="container">
  <div class="col centerme">
    <HomeCard />
  </div> 
</div>
</template>

<script>
// @ is an alias to /src
import HomeCard from '@/components/HomeCard.vue'

export default {
  name: 'HomeView',
  components: {
    HomeCard
  }
}
</script>

<style scoped>
.centerme{
  margin-left: auto;
  margin-right: auto;
}
</style>