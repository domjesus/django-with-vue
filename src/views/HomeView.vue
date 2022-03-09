<template>
  <div class="home">
    <contatos-component :contatos="contatos" />
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import ContatosComponent from "../components/ContatosComponent";

export default {
  name: "HomeView",
  data() {
    return {
      contatos: [],
    };
  },
  components: {
    ContatosComponent,
  },
  mounted() {
    axios.get("/contatos/list/").then((r) => {
      console.log(r);
      this.contatos = r.data;
    });
  },
};
</script>
