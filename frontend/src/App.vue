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
  </div>

  <!-- modal element   -->
  <div
    id="manage-employee-Modal"
    ref="employeeModal"
    class="modal fade"
    tabindex="-1"
    aria-labelledby="manage-employee-ModalLabel"
    aria-hidden="true"
  >
    <div 
      class="modal-dialog" 
      style="font-size: xx-small"
    >
      <div class="modal-content">
        <div class="modal-header pb-1">
          <h5 
            id="manage-employee-ModalLabel"
            class="modal-title" 
          >
            {{ form.id ? "Edit" : "Add" }} Employee
          </h5>
          <button
            type="button"
            class="btn-close"
            aria-label="Close"
            @click="closeModal()"
          />
        </div>

        <div class="modal-body">
          <form 
            ref="formElement" 
            class="row g-3" 
            @submit.prevent="submitForm()"
          >
            <span 
              id="basic-header" 
              class="form-header"
            >
              Basic Info
            </span>

            <div 
              id="first-name" 
              class="col-6"
            >
              <label 
                for="firstName" 
                class="form-label"
              >
                First name
              </label>
              <input
                id="firstName"
                v-model="form.first_name"
                type="text"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.first_name">
                <li
                  v-for="(error, index) in errors.first_name"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <div 
              id="last-name" 
              class="col-6"
            >
              <label 
                for="lastName" 
                class="form-label"
              >
                Last Name</label>
              <input
                id="lastName"
                v-model="form.last_name"
                type="text"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.last_name">
                <li
                  v-for="(error, index) in errors.last_name"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <div 
              id="contact-number" 
              class="col-12"
            >
              <label 
                for="contactNumber" 
                class="form-label"
              >
                Contact Number
              </label>
              <input
                id="contactNumber"
                v-model="form.contact_number"
                type="text"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.contact_number">
                <li
                  v-for="(error, index) in errors.contact_number"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <div 
              id="email-address" 
              class="col-12"
            >
              <label 
                for="emailAddress" 
                class="form-label"
              >
                Email Address
              </label>
              <input
                id="emailAddress"
                v-model="form.email"
                type="email"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.email">
                <li
                  v-for="(error, index) in errors.email"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <div 
              id="date-of-birth" 
              class="col-4"
            >
              <label 
                for="dateOfBirth" 
                class="form-label"
              >
                Date of Birth
              </label>
              <input
                id="dateOfBirth"
                v-model="form.date_of_birth"
                type="date"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.date_of_birth">
                <li
                  v-for="(error, index) in errors.date_of_birth"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <span 
              id="address-header" 
              class="form-header"
            >
              Address Info</span>

            <div 
              id="street-address" 
              class="col-12"
            >
              <label 
                for="streetAddress" 
                class="form-label"
              >
                Street Address
              </label>
              <input
                id="streetAddress"
                v-model="form.street_address"
                type="text"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.street_address">
                <li
                  v-for="(error, index) in errors.street_address"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <div 
              id="city" 
              class="col-4"
            >
              <label 
                for="city" 
                class="form-label"
              >
                City</label>
              <input
                id="city"
                v-model="form.city"
                type="text"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.city">
                <li
                  v-for="(error, index) in errors.city"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <div 
              id="postal-code" 
              class="col-4"
            >
              <label 
                for="postalCode" 
                class="form-label"
              >
                Postal Code</label>
              <input
                id="postalCode"
                v-model="form.postal_code"
                type="text"
                pattern="[0-9][0-9][0-9][0-9]"
                class="form-control"
                required
                oninvalid="this.setCustomValidity('Postal Code Cannot be more than 4 characters.')"
                oninput="this.setCustomValidity('')"
              >
              <ul v-if="errors && errors.postal_code">
                <li
                  v-for="(error, index) in errors.postal_code"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <div 
              id="country" 
              class="col-4"
            >
              <label 
                for="country" 
                class="form-label"
              >
                Country
              </label>
              <input
                id="country"
                v-model="form.country"
                type="text"
                class="form-control"
                required
              >
              <ul v-if="errors && errors.country">
                <li
                  v-for="(error, index) in errors.country"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>

            <span 
              id="skills header" 
              class="form-header"
            >
              Skills</span>

            <template 
              v-for="(skill, index) in form.skill" 
              :key="index"
            >
              <div class="col-4">
                <label 
                  for="skillName" 
                  class="form-label"
                >
                  Skill
                </label>
                <input
                  id="skillName"
                  v-model="skill.name"
                  type="text"
                  class="form-control"
                  required
                >
              </div>
              <div 
                class="col-3"
              >
                <label 
                  for="yearsOfExperience" 
                  class="form-label"
                >
                  Yrs Exp
                </label>
                <input
                  id="yearsOfExperience"
                  v-model="skill.years_experience"
                  type="number"
                  min="0"
                  step="1"
                  class="form-control"
                  required
                >
              </div>
              <div 
                class="col-4"
              >
                <label 
                  for="seniorityRating" 
                  class="form-label"
                >
                  Seniority Rating
                </label>
                <select
                  id="seniorityRating"
                  v-model="skill.seniority_rating"
                  class="form-select"
                  required
                >
                  <option value="Beginner">
                    Beginner
                  </option>
                  <option value="Intermediate">
                    Intermediate
                  </option>
                  <option value="Advanced">
                    Advanced
                  </option>
                  <option value="Expert">
                    Expert
                  </option>
                </select>
              </div>
              <div class="col-1 centered-content">
                <span
                  class="material-icons centered-content pt-3"
                  style="cursor: pointer"
                  @click="removeSkill(index)"
                >
                  delete
                </span>
              </div>
            </template>
            <div 
              v-if="errors && errors.skill"
              id="skill-errors" 
              class="col-12" 
            >
              <ul>
                <li
                  v-for="(error, index) in errors.skill"
                  :key="index"
                  class="form-label text-danger col-12"
                >
                  {{ error }}
                </li>
              </ul>
            </div>
            <div 
              id="add-skill-button" 
              class="me-2 d-flex mt-4"
            >
              <span
                class="btn centered-content w-100"
                @click.prevent="addSkill"
              >
                <span 
                  class="material-icons centered-content"
                >
                  add 
                </span>
                Add New Skill
              </span>
            </div>
            <div 
              id="submit-button" 
              class="right-content mt-4"
            >
              <button
                type="submit"
                class="btn btn-primary centered-content w-auto"
                @click.prevent="submitForm()"
              >
                <span 
                  class="material-icons-outlined me-2"
                >
                  {{ form.id ? "edit" : "add_circle" }}
                </span>
                {{ form.id ? "Edit" : "Add" }} Employee
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>

</style>

<script setup>
import { onMounted, ref, watch } from 'vue'
import axios from "axios";
import { Modal } from "bootstrap";

//filter variables
let searchValue = ref("");
let filterType = ref("first_name");

//employee variables
let employees = ref([]);
let unfilteredList = ref([]); // original data stored to cache employees before filtering

//form variables
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
let errors = ref([]);

//html elements
let employeeModal = ref(undefined);

onMounted(async () => {
  await fetchEmployees();
  if (localStorage.getItem("form")) {
    form.value = JSON.parse(localStorage.getItem("form"));
  }
});
async function fetchEmployees() {
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

function closeModal() {
  let modal = Modal.getOrCreateInstance(employeeModal.value);
  modal.hide();
}

function showModal() {
  let modal = Modal.getOrCreateInstance(employeeModal.value);
  modal.show();
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