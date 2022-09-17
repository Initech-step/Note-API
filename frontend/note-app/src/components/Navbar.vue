<template>
<div class="bg-warning">
  <ul class="nav justify-content-center">
    <li class="nav-item">
        <router-link :to="{name: 'addnote'}">
            <button class="beaut btn btn-md btn-dark m-2 p-2">Create note</button>
        </router-link>
    </li>
    <li class="nav-item">
        <router-link :to="{name: 'createCategory'}">
            <button class="beaut btn btn-md btn-dark m-2 p-2">Create Category</button>
        </router-link>
    </li>
    <li class="nav-item">
        <router-link :to="{name: 'viewnotes'}">
            <button class="beaut btn btn-md btn-dark m-2 p-2">View Notes</button>
        </router-link>
    </li>
</ul>
</div>
</template>

<script>
export default {
    name:'Navbar',
}
</script>

<style>

</style>