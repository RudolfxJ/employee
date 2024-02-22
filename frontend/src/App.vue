<template>
  <div 
    id="app" 
    class="container" 
    style="height: 100vh"
  >
  <div 
      id="nav" 
      class="mb-5"
    >
      <div class="row">
        <div 
          id="header" 
          class="col-2 left-content-stacked"
        >
          <h4 class="p-0 m-0 mt-2">
            Employees
          </h4>
          <p>There are {{ employees.length }} employees</p>
        </div>
        <div 
          id="search" 
          class="col-6 centered-content"
        >
          <input
            id="search_input"
            v-model="searchValue"
            type="text"
            class="form-control"
            placeholder="Search"
          >
        </div>
        <div 
          id="filter_by" 
          class="col-2 right-content"
        >
          <select 
            id="employeeDetails" 
            v-model="filterType"
            class="form-select" 
          >
            <option 
              selected 
              disabled
            >
              Filter By
            </option>
            <option value="first_name">
              First Name
            </option>
            <option value="last_name">
              Last Name
            </option>
            <option value="email">
              Email
            </option>
            <option value="date_of_birth">
              Year (Date of Birth)
            </option>
            <option value="skills">
              Skills
            </option>
          </select>
        </div>
        <div class="col-2 right-content">
          <button
            type="button"
            class="btn btn-primary left-content"
            @click="newEmployee()"
          >
            <span class="material-icons-outlined me-2"> add_circle </span>
            New Employee
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>

<script setup>
import { onMounted, ref } from 'vue'
let employees = ref([]);
onMounted(async () => {
})
</script>