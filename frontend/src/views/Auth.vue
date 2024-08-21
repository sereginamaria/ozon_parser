<template>
  <div class="auth-block">
    <FloatLabel style="margin-bottom: 2rem">
      <InputText id="username" type="text" v-model="login" style="min-width: 300px"/>
      <label for="username">Логин</label>
    </FloatLabel>
    <FloatLabel style="margin-bottom: 2rem">
      <InputText id="password" type="password" v-model="password" style="min-width: 300px"/>
      <label for="password">Пароль</label>
    </FloatLabel>
    <Button label="Войти" @click="checkAuth()"/>

    <Dialog v-model:visible="visibleAuthError" modal :draggable="false" style="min-width: 30%">
      <div>
        <h3>Ошибка авторизации!</h3>
        <p>Введен неверный логин или пароль</p>
      </div>
    </Dialog>
  </div>


</template>

<script lang="ts">
import {defineComponent} from 'vue'
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import FloatLabel from "primevue/floatLabel";
import {mapStores} from "pinia";
import {useAuthStore} from "@/stores";
import Dialog from "primevue/dialog";

export default defineComponent({
  name: "Auth",
  components: {Button, InputText, FloatLabel, Dialog},
  computed: {
    ...mapStores(useAuthStore),
  },
  data() {
    return {
      login: '',
      password: '',
      visibleAuthError: false
    }
  },
  methods: {
    checkAuth() {
      let response = this.auth.auth(this.login, this.password)
      console.log(response)
      if (response) {
        this.$router.push('/verification')
      }
      else this.visibleAuthError = true
    }
  }
})
</script>

<style scoped>
  .auth-block {
    display: flex;
    width: 100%;
    height: 100%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
</style>