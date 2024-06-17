<template>
  <div class="min-h-screen w-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center p-4">
    <div class="container max-w-lg bg-white shadow-lg rounded-lg p-6">
      <h1 class="text-4xl font-bold text-center text-gray-800 mb-6">URL Shortener</h1>
      <p class="text-center text-gray-600 mb-6">Simplify your long URLs into easy-to-share short links</p>
      <form @submit.prevent="submitUrl" class="flex flex-col gap-4">
        <input
          ref="urlInput"
          v-model="url"
          name="shorturl"
          type="url"
          placeholder="Enter URL"
          required
          class="input input-bordered w-full p-3 border border-gray-300 rounded-md"
        />
        <button
          type="submit"
          class="btn btn-primary bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition duration-300"
        >
          Shorten
        </button>
      </form>
      <div v-if="shortUrl" class="mt-6 text-center">
        <p class="text-lg">Short URL:
          <a :href="shortUrl" class="text-blue-600 underline ml-2">{{ shortUrl }}</a>
        </p>
        <button
          v-if="!copiedToClipboard"
          @click="copyToClipboard"
          class="btn btn-xs btn-success btn-outline transition mt-2 duration-300"
        >
          Copy to Clipboard
        </button>
        <p v-if="copiedToClipboard" class="text-green-600 mt-2">{{ message }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      apiUrl: import.meta.env.VITE_URLSHORT_API_URL,
      frontendUrl: import.meta.env.VITE_URLSHORT_FRONT_URL,
      url: '',
      shortUrl: null,
      message: 'Copied to clipboard',
      copiedToClipboard: false,
    };
  },
  methods: {
    async submitUrl() {
      const apiUrl = this.apiUrl;
      try {
        const response = await axios.post(apiUrl, {
          url: this.url,
        });
        this.shortUrl = response.data.short_url;
        this.url = "";
        this.copiedToClipboard = false;
        this.$refs.urlInput.focus();
      } catch (error) {
        console.error('Error shortening URL:', error);
      }
    },
    async copyToClipboard() {
      await navigator.clipboard.writeText(this.frontendUrl + this.shortUrl);
      this.copiedToClipboard = true;
    }
  }
};
</script>

<style scoped>
body {
  font-family: 'Arial', sans-serif;
}
.input {
  transition: border-color 0.3s;
}
.input:focus {
  border-color: #3182ce;
  outline: none;
}
</style>