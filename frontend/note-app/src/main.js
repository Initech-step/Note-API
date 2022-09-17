import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import mitt from 'mitt'
// instantiate the mitt library
const emitter = mitt()
//app instance
const app = createApp(App)
app.use(router)
//add the event 
app.config.globalProperties.emitter = emitter
//mount
app.mount('#app')


