<template>
  <!-- modal element   -->
  <div
    id="manage-employee-Modal"
    ref="employeeModal"
    class="modal fade"
    tabindex="-1"
    data-bs-backdrop="static"
    aria-labelledby="manage-employee-ModalLabel"
    aria-hidden="true"
    data-bs-keyboard="false"
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

<script setup>
import { onMounted, ref } from 'vue'
import { Modal } from "bootstrap";
import axios from "axios";

const props = defineProps({
  employee: {
    type: Object,
    required: false,
    default: () => ({
      id: null,
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
        }
      ]
    })
  },
  modelValue: undefined, // show
})

const emit = defineEmits(
  ["update:modelValue"],
  "submitSuccess"
);

//html elements
let employeeModal = ref(undefined);
let formElement = ref(undefined);

//form variables
let form = ref(props.employee)
let errors = ref([]);

onMounted(async () => {
  if (props.modelValue) {
    showModal();
  }
})

function validate() {
  let skills = form.value.skill;
  if (formElement.value.checkValidity() === false) {
    formElement.value.classList.add("was-validated");
    return false;
  }

  return true;
}

async function submitForm() {
  if (!validate()) {
    return;
  }
  if (!form.value?.id) {
    await axios
      .post("employees/", form.value)
      .then(async (response) => {
        errors.value = []
        if (response.status == 201) {
          closeModal();
          localStorage.removeItem("form");
          localStorage.removeItem("inProgress");
          await fetchEmployees();
        } else {
          errors.value = response.data;
        }
      })
      .catch((error) => {
        if (error?.response?.data) {
          errors.value = error.response.data;
        } else {
          errors.value = "Server Error";
        }
      });
  } else {
    await axios
      .put(`employees/${form.value.id}/`, form.value)
      .then(async (response) => {
        errors.value = []
        if (response.status == 200) {
          closeModal();
          localStorage.removeItem("form");
          await fetchEmployees();
        } else {
          errors.value = response.data;
        }
      })
      .catch((error) => {
        if (error?.response?.data) {
          errors.value = error.response.data;
        } else {
          errors.value = "Server Error";
        }
      });
  }
}

function showModal() {
  let modal = Modal.getOrCreateInstance(employeeModal.value);
  modal.show();
}

function closeModal() {
  let modal = Modal.getOrCreateInstance(employeeModal.value);
  modal.hide();
  emit("update:modelValue", false);
}

function addSkill() {
  form.value.skill.push({
    name: "",
    years_experience: "",
    seniority_rating: "Beginner",
  });
}

function removeSkill(index) {
  form.value.skill.splice(index, 1);
  if (form.value.skill.length === 0) {
    form.value.skill.push({
      name: "",
      years_experience: "",
      seniority_rating: "Beginner",
    });
  }
}
</script>