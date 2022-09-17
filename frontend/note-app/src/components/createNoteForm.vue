<template>

<div class="alert alert-success" role="alert" v-if="success">
  Post successfully made
</div>

<div class="alert alert-danger" role="alert" v-if="failure">
  There was an issue
</div>

<form @submit.prevent="addNewNote">
    <div>
        <textarea type="text" class="form-control" placeholder="Add note here" required v-model="note"></textarea>
        <br>
    </div>
    <div>
        <select class="form-select" v-model="choosenCategory" required>
            <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.category }}</option>
        </select>
    </div>
    <div>
        <br>

        <button type="submit" class="btn btn-lg btn-primary" v-if="noteId">Edit Note</button>
        <button type="submit" class="btn btn-lg btn-primary" v-else>Create Note</button>
    </div>
</form>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CreateNoteForm',

    data: function(){
        return {
            noteId : null,
            note: '',
            categories: null,
            choosenCategory: '',
            success: false,
            failure: false,
        }
    },

    mounted(){

        if(this.$route.query.editId === undefined ){
            axios.get(`http://127.0.0.1:8000/api/category/`)
            .then((response) => {
                this.categories = response.data
            })
            // catch
            .catch(function(error){
                console.log(error)
            })

        }else{

            this.noteId = this.$route.query.editId
            axios.get(`http://127.0.0.1:8000/api/predit/${this.noteId}/`)
            .then((response) => {
                this.categories = response.data.categories
                this.note = response.data.note.note
                this.choosenCategory = response.data.note.category
            })
            // catch
            .catch(function(error){
                console.log(error)
            })
        }
        
    },
    
    methods: {
        addNewNote: function(){
            if(this.noteId == null){
                console.log('I will be making a new post')

                axios.post(`http://127.0.0.1:8000/api/note/`, {
                    note: this.note,
                    category: this.choosenCategory
                })
                .then(function(response) {
                    alert('The post was made successfully')
                })
                .catch(function(error) {
                    alert('There was an issue')
                })

            }else{

                axios.put(`http://127.0.0.1:8000/api/note/${this.noteId}/`, {
                    note: this.note,
                    category: this.choosenCategory
                })
                .then((response) => {
                    alert('The post was Edited successfully')
                })
                .catch(function(error) {
                    alert('There was an issue while Editing the post')
                })
                
            }
        }

    }
}
</script>

<style>
</style>

