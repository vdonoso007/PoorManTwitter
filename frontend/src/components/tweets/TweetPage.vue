<template>
    <div>
        <h3>Welcome to Poor Man's Twitter Project</h3>
        <hr>
        <br>
        <tweet-create v-on:tweetPosted="refreshTweetsList" />
        <br>
        <br>
        <tweets v-bind:tweets="tweets" />
    </div>
</template>

<script>
import TweetCreate from './TweetCreate.vue'
import Tweets from './Tweets.vue'
import axios from 'axios'

export default {
  
  data() {
    return {
      tweets: []
    }
  },
  
  components: { TweetCreate, Tweets },

  methods: {
    
    refreshTweetsList () {

      this.getTweets()

    },

    getTweets () {

        const path = `${process.env.BASE_URI}tweets/`;

        axios.get(path).then((response) => { 
            
            this.tweets = response.data

        })
        .catch((error) => {
            console.log(error)
        })

    }

  },

  created() {
    this.getTweets()
  }
}
</script>

<style scoped>

</style>