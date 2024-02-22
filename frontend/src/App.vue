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
    <div 
      v-if="employees.length > 0"
      id="employees" 
    >
      <div 
        v-for="(employee, index) in employees"
        :key="employee"
        class="card mb-3"
      >
        <div class="card-body d-flex left-content">
          <div class="row w-100">
            <div class="col-1">
              <span class="circle-text">{{ index + 1 }}</span>
            </div>
            <div class="col-2">
              {{ employee.first_name }}
            </div>
            <div class="col-2">
              {{ employee.last_name }}
            </div>
            <div class="col-2">
              {{ employee.contact_number }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div 
      v-else
      class="centered-content-stacked"
    >
      <img src="./assets/no-employees.jpg">
      <p>There is nothing here</p>
      <p>
        Create a new employee by clicking the <br>
        <strong>New Employee</strong> button to get started.
      </p>
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