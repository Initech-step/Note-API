<template>
    <h2 class="text-center">Add category</h2>
        <div class="container">
            <CreateCategoryForm />
        </div>
</template>

<script>
import CreateCategoryForm from '@/components/CreateCategoryForm.vue'

export default {
  name: 'CreateCategory',
  components: {
    CreateCategoryForm
  }
}
</script>

<style>
</style>