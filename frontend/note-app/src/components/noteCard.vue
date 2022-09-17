<template>
  <div class="card m-2" style="width: 18rem;">
  <div class="card-body">
    <small class="text-success">Category id: {{ category }}</small>
    <p class="card-text">{{ truncatedtext }}</p>
    <button class="btn btn-sm btn-primary m-1" @click="viewNote(id)">View</button>
  </div>
</div>
</template>

<script>
export default {
    name: 'Card',
    props: ['category', 'truncatedtext', 'id'],
    methods:{
      viewNote: function(pk){
        this.$router.push({name:'viewnote', params:{id:pk}})
      }
    }
}
</script>

<style>

</style>