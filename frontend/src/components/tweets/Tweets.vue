<template>
    <div class="container">
        <div class="row">
            <div class="col">

                <div class="tweet-container" v-for="tweet of tweets" :key="tweet.id">
                    
                    <div class="tweet-header">
                        <div>
                            <b-icon icon="person-fill" style="color: #7952b3;"></b-icon>
                            <div>{{tweet.name}}</div>
                        </div>
                        <div>{{tweet.created_at | tweetDateFormat }}</div>
                    </div>
                    <br>
                    <div>{{tweet.text}}</div>
                    <div class="my-separator"></div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>

export default {

    data () {
        return {
                
                days: [
                        'Sun',
                        'Mon',
                        'Tue',
                        'Wed',
                        'Thu',
                        'Fri',
                        'Sat'
                ]

            }
    },

    props: [ 'tweets' ],

    filters: {
        tweetDateFormat: function(value) {
            
            const months = [
                        'January',
                        'February',
                        'March',
                        'April',
                        'May',
                        'June',
                        'July',
                        'August',
                        'September',
                        'October',
                        'November',
                        'December'
                ]

            const dateBuilded = new Date(value)
            const year = dateBuilded.getFullYear()
            const date = dateBuilded.getDate()
            const monthName = months[dateBuilded.getMonth()]
            const time =  dateBuilded.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })

            return `${monthName} ${date}, ${year} at ${time}`
        }
    },

    created() {
        console.log(this.tweets)
    }
    
}
</script>

<style lang="css" scoped>

.myFormContainer {
    display: flex;
    justify-content: center;
}

.tweet-container {
    display: flex;
    flex-direction: column;
}

.tweet-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.my-separator {
    margin: 2em;
    height: .025em;
    border: .025em solid #000;

}

</style>