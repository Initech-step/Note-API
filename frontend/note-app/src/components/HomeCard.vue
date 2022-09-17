<template>
  <div class="card text-center">
    <div class="card-header">
        start date: August 6, 2022
    </div>
    <div class="card-body">
        <h2 class="card-title">Notes App</h2>
        <p class="card-text">Welcome to my first fullstack application. There is so much to learn. <b class="text-info">Please use the Navbar above</b></p>
        <router-link :to="{name: 'addnote'}">
            <button class="btn btn-primary">Create Note</button>
        </router-link> 
    </div>
    <div class="card-footer text-muted">
        End date:
    </div>
</div>
</template>

<script>
export default {
    name: 'HomeCard'
}
</script>

<style>

</style>