<template>
  <button class="btn" onclick="my_modal_1.showModal()">Add author</button>
  <dialog id="my_modal_1" class="modal">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Add author</h3>
      <div class="flex flex-col gap-4 mt-4">
        <div class="flex justify-between">
          <label class="input input-bordered flex items-center gap-2">
            <input type="text" class="grow" placeholder="Name" />
          </label>
          <label class="input input-bordered flex items-center gap-2">
            <input type="text" class="grow" placeholder="Age" />
          </label>
        </div>
        <div class="flex justify-between">
          <label class="input input-bordered flex items-center gap-2">
            <input type="text" class="grow" placeholder="Name" />
          </label>
          <label class="input input-bordered flex items-center gap-2">
            <input type="text" class="grow" placeholder="Age" />
          </label>
        </div>
      </div>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn">Close</button>
        </form>
      </div>
    </div>
  </dialog>
</template>

<script setup lang="ts"></script>
