<template>
  <div 
    id="app" 
    class="container" 
    style="height: 100vh"
  > 
    <employeeCreateUpdateComponent
      v-if="show"
      v-model="show"
      :employee="form"
      @update:model-value="fetchEmployees()"
    />
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
            <div class="col-5 d-flex">
              <span
                class="material-icons centered-content ms-auto"
                style="cursor: pointer"
                @click="editEmployee(employee)"
              >
                create
              </span>
              <span
                class="material-icons centered-content ms-2"
                style="cursor: pointer"
                @click="removeEmployee(employee.id)"
              >
                delete
              </span>
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
    <div v-if="errors">
      {{ errors }}
    </div>
  </div>
</template>


<script setup>
import { onMounted, ref, watch } from 'vue'
import axios from "axios";
import employeeCreateUpdateComponent from "./components/employeeCreateUpdateComponent.vue";

//filter variables
let searchValue = ref("");
let filterType = ref("first_name");

//employee variables
let employees = ref([]);
let unfilteredList = ref([]); // original data stored to cache employees before filtering

//form variable
let form = ref({
  first_name: "",
  last_name: "",
  contact_number: "",
  email: "",
  date_of_birth: "",
  street_address: "",
  city: "",
  postal_code: "",
  country: "",
  skill: [
    {
      name: "",
      years_experience: "",
      seniority_rating: "Beginner",
    },
  ],
});
let errors = ref(undefined)

//variable to toggle modal
let show = ref(false)

onMounted(async () => {
  await fetchEmployees();
  if (localStorage.getItem("form")) {
    form.value = JSON.parse(localStorage.getItem("form"));
  }
});

async function fetchEmployees() {

  errors.value = undefined

  await axios
    .get("employees/")
    .then((response) => {
      const data = response.data;
      employees.value = data;
      unfilteredList.value = data;
    })
    .catch((error) => {
      console.log(error);
    });
  filter()
}

function newEmployee() {
  if (localStorage.getItem("inProgress")) {
    form.value = JSON.parse(localStorage.getItem("inProgress"));
  } else {
    form.value = {
      skill: [{ seniority_rating: "Beginner" }],
    };
  }
  localStorage.setItem("form", JSON.stringify(form.value));
  showModal();
}

async function removeEmployee(id) {
  if (!confirm("Are you sure?")) return;

  errors.value = undefined

  await axios
    .delete(`employees/${id}/`)
    .then(() => {
      fetchEmployees();
    })
    .catch((error) => {
      console.log(error);
    });
}

function editEmployee(employee) {
  form.value = JSON.parse(JSON.stringify(employee));
  localStorage.setItem("form", JSON.stringify(form.value));
  showModal()
}

function showModal() {
  show.value = true
}

function filter() {
  if (searchValue.value === "") {
    employees.value = unfilteredList.value;
    return;
  }

  if (filterType.value == "skills") {
    employees.value = unfilteredList.value.filter((employee) => {
      return employee[filterType.value].some((skill) => {
        return skill.name
          .toLowerCase()
          .includes(searchValue.value.toLowerCase());
      });
    });
  } else if (filterType.value == "date_of_birth") {
    let year = searchValue.value;
    employees.value = unfilteredList.value.filter((employee) => {
      let employeeYear = employee[filterType.value].slice(0, 4);
      return employeeYear == year;
    });
  } else {
    employees.value = unfilteredList.value.filter((employee) => {
      return employee[filterType.value]
        .toLowerCase()
        .includes(searchValue.value.toLowerCase());
    });
  }
}

watch(
  form,
  () => {
    localStorage.setItem("form", JSON.stringify(form.value));
    if (!form.value?.id) {
      localStorage.setItem("inProgress", JSON.stringify(form.value));
    }
  },
  { deep: true }
);

watch(searchValue, () => {
  filter();
});

watch(filterType, () => {
  filter();
});
</script>