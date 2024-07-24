<template>
  <Toolbar id="toolbar" ref="toolbar" style="padding: 1rem 1rem 1rem 1rem; margin-bottom: 1rem">
    <template #start>
      <div class="flex items-center gap-2">
        <Button :label="this.label" text plain @click="goTo()"/>
      </div>
    </template>
  </Toolbar>
</template>

<script>
import Toolbar from 'primevue/toolbar';
import Button from 'primevue/button';

export default {
  name: "NavbarComponent",
  props: {
    label: String,
    goToUrl: String
  },
  components: { Toolbar, Button},
  methods: {
    goTo() {
      this.$router.push(this.goToUrl)
    }
  }
}
</script>

<style scoped>

</style>