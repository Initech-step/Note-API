
<template>
<div class="container">
  <div class="row">
    <div class="col-12">
    <h5 v-show="issue">An error occured</h5>
    <div class="card">
        <h5 class="card-header text-success">Category Id: {{ category }}</h5>
        <div class="card-body">
            <p class="card-text">{{ note }}</p>
            <button class="btn btn-primary mx-1" @click="editNote(id)">Edit</button>
            <button class="btn btn-danger" @click="deleteNote(id)">Delete</button>

        </div>
    </div>

    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ViewNote',
    data: function(){
      return {
        category: null,
        note: null,
        id: null,
        issue: false,

      }
    },

    mounted: function(){
      // get the note id
      let noteid = this.$route.params.id

      // make request and share data
      axios.get(`http://127.0.0.1:8000/api/note/${noteid}/`)
      .then((response) => {
        this.category = response.data.category
        this.note = response.data.note
        this.id = response.data.id
      })
      // catch
      .catch(function(error){
        console.log(error)
      })

      
    },

    methods:{
      editNote: function(pk){
        console.log(pk)
        this.$router.push({name:'addnote', query:{editId:pk}})
      },

      deleteNote: function(pk){
        axios.delete(`http://127.0.0.1:8000/api/note/${pk}/`)
        .then((response) => {
          this.$router.push({name:'viewnotes'})
        })
        // catch
        .catch(function(error){
          alert('An error Occured')
        })
      }


    }

}
</script>

<style>

</style>





