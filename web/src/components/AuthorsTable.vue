<template>
  <div class="overflow-x-auto">
    <table class="table">
      <!-- head -->
      <thead>
        <tr>
          <th></th>
          <th>Full name</th>
          <th>Email</th>
          <th>Age</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody v-for="author in mockAuthors" v-bind:key="author.id">
        <!-- row 1 -->
        <tr>
          <th>{{ author.id }}</th>
          <td>{{ author.fullname }}</td>
          <td>{{ author.email }}</td>
          <td>{{ author.age }}</td>
          <td>{{ author.details }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
type Author = {
  id: string
  fullname: string
  email: string
  age: number
  details: string
}

const mockAuthors: Author[] = [
  {
    id: '1',
    fullname: 'Cy Ganderton',
    email: 'sgardian@example.com',
    age: 23,
    details: 'Quality Control Specialist'
  },
  {
    id: '2',
    fullname: 'Hart Hagerty',
    email: 'hagerty@example.com',
    age: 23,
    details: 'Quality Control Specialist'
  }
]
</script>
