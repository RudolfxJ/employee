import { createApp } from 'vue'
import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import './assets/style.css'

import axios from 'axios';
axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;

import { createStore } from 'vuex'
const store = createStore({
  state: {},
  mutations: {},
  actions: {},
  getters: {},
  modules: {},
})

createApp(App).use(store).mount('#app')