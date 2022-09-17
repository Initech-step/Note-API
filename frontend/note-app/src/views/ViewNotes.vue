<template>
<div class="container">
  <div class="row">

    <div v-if="loading">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    
    <p v-if="whahala">There was an erorr</p>

    <div class="col" v-for="note in notes" :key="note.id">
      <Card :category="note.category" :truncatedtext="note.note" :id="note.id">
      </Card>
    </div>

  </div>
</div>
</template>

<script>
import Card from '@/components/noteCard.vue'
import axios from 'axios';

export default {
    name: 'ViewNotes',
    data: function(){
        return{
            notes: null,
            loading: true,
            whahala: false,
        }
    },

    components:{
      Card
    },

    mounted(){
      axios.get('http://127.0.0.1:8000/api/note/')
      .then((response) => {
        this.notes = response.data
        this.loading = false
        console.log('Response', this.notes)
      })
      .catch(function(error){
        this.whahala = true
      })
      .finally()

    }
}
</script>
