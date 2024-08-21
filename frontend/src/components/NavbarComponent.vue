<template>
  <Toolbar id="toolbar" ref="toolbar" class="toolbar-block">
    <template #start>
      <div class="flex items-center gap-2">
        <Button :label="label" text plain @click="goTo()"/>
      </div>
    </template>
        <template #end>
      <div class="flex items-center gap-2">
        <Button label="Выйти" text plain @click="exit()"/>
      </div>
    </template>
  </Toolbar>
</template>

<script lang="ts">
import Toolbar from 'primevue/toolbar';
import Button from 'primevue/button';
import {defineComponent} from "vue";

export default defineComponent( {
  name: "NavbarComponent",
  props: {
    label: String,
    goToUrl: {
      type: String,
      default: '/'
    }
  },
  components: { Toolbar, Button},
  methods: {
    goTo() {
      this.$router.push(this.goToUrl)
    },
    exit() {
      localStorage.setItem('isAuth', 'false');
      this.$router.push('/')
    }
  }
})
</script>

<style scoped>
  .toolbar-block {
    padding: 1rem 1rem 1rem 1rem;
    margin-bottom: 1rem
  }

  @media screen and (max-width: 480px) {
    .toolbar-block {
      padding: 0.5rem 0.5rem 0.5rem 0.5rem;
      margin-bottom: 0.5rem
    }
  }
</style>