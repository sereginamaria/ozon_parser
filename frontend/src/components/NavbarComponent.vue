<template>
  <Toolbar id="toolbar" ref="toolbar" class="toolbar-block">
    <template #start>
        <div style="display: flex; flex-direction: column">
            <div class="flex items-center gap-2">
                <Button label="H" text plain @click="goToHome()"/>
                <Button v-for="(label, index) in labels" :label="label" text plain @click="goTo(index)"/>
            </div>
            <p style="text-align: center; margin: 0; padding: 0; font-size: 10px">{{ channelName }}</p>
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
    labels: {
        type: Array,
        default: []
    },
    goToUrls: {
      type: Array,
      default: []
    },
      channelName:{
          type: String,
          default: ''
      }
  },
  components: { Toolbar, Button},
  methods: {
    goTo(index) {
      if (this.goToUrls.length !== 0) {
          this.$router.push(this.goToUrls[index])
      }
    },
    goToHome() {
      this.$router.push('/home')
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