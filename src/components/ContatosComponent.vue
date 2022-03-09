<template>
  <div>
    <h3>Contatos</h3>
    <table class="table table-striped table-hover">
      <thead class="thead-dark">
        <th>Nome</th>
        <th>Email</th>
        <th>Telefone</th>
        <th>Data Criação</th>
        <th>Descrição</th>
      </thead>
      <tbody>
        <tr v-for="(contato, i) in contatos" :key="i">
          <td>{{ contato.nome }} {{ contato.sobrenome }}</td>
          <td>{{ contato.email }}</td>
          <td>{{ contato.telefone }}</td>
          <td>{{ contato.data_criacao }}</td>
          <td>{{ contato.descricao }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ContatosComponent",
  props: {
    contatos: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
</style>