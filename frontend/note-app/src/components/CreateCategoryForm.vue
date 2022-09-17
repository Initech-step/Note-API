<template>
<form @submit.prevent="addNewCategory">
    <div>
        <input type="text" class="form-control" placeholder="Category" v-model="category" required/>
    </div>
    <div>
        <br>
        <button type="submit" class="btn btn-lg btn-primary">Create Category</button>
    </div>
</form>
</template>

<script>
import axios from 'axios'
export default {
    name: 'CreateCategoryForm',
    data: function(){
        return {
            category:''
        }
    },
    methods: {
        addNewCategory: function(){

            axios.post(`http://127.0.0.1:8000/api/category/`, {
                category: this.category
            })
            .then(function (response) {
                alert('The category was added successfully')
            })
            .catch(function (error) {
                console.log(error)
                alert('There was an issue error!')
            })
        }
    }
}
</script>

<style>
</style>