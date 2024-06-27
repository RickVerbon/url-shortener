<template>
  <div class="flex">
    <!-- You can add some loading text or spinner here -->
    <div class="spinner"></div>
    <p class="ms-4 mt-2">Redirecting to <strong>{{url}}</strong>...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      url: '',
      frontUrl: import.meta.env.VITE_URLSHORT_FRONT_URL,
    };
  },
  name: 'RedirectView',
  props: ['shortUrl'],
  created() {
    this.redirectToOriginalUrl();
  },
  methods: {
    async redirectToOriginalUrl() {
      const frontUrl = this.frontUrl;
      try {
        const response = await axios.get(`${frontUrl}${this.shortUrl}`);
        if (response.data.url) {
          this.url = response.data.url;
          window.location.href = response.data.url;
        }
      } catch (error) {
        console.error('Error redirecting to original URL:', error);
      }
    }
  }
};
</script>