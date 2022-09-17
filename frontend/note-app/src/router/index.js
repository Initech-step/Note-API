import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddNote from '../views/AddNoteView.vue'
import CreateCategory from '../views/CreateCategoryView.vue'
import ViewNotes from '../views/ViewNotes.vue'
import ViewNote from '../components/viewNote.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/addnote',
    name: 'addnote',
    component: AddNote
  },
  {
    path: '/create-category',
    name: 'createCategory',
    component: CreateCategory
  },
  {
    path: '/viewNotes',
    name: 'viewnotes',
    component: ViewNotes
  },
  {
    path: '/notes/:id',
    name: 'viewnote',
    component: ViewNote
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router
