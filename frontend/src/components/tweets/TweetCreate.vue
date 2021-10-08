<template>
    <div class="container">
        <div class="row">
            <div class="col">
                
                    <form @submit="onSubmit">

                        <div class="myFormContainer">

                            <b-form-group
                                id="fieldset-1"
                                description="Let us know your name."
                                label="Enter your name"
                                label-for="input-1"
                                valid-feedback="Thank you!"
                                >
                                <!--b-form-input id="input-1" v-model="form.name" :state="form.state" trim></b-form-input-->
                                <b-form-input id="input-1" v-model="form.name" trim></b-form-input>
                            </b-form-group>
                            &nbsp;
                            <b-form-group
                                id="fieldset-2"
                                description="Let us your tweet."
                                label="Enter your tweet"
                                label-for="input-2"
                                valid-feedback="Thank you!"
                                >
                                <!--b-form-input id="input-2" v-model="form.text" :state="form.state" trim></b-form-input-->
                                <b-form-input id="input-2" v-model="form.text" trim></b-form-input>
                            </b-form-group>
                            &nbsp;&nbsp;
                            <b-form-group
                                label="Hint Post Button"
                                description=" 👆🏻👆🏻 "
                                valid-feedback="Thank you!"
                                >
                                <div>
                                    <b-button :disabled="isDisabled" pill type="submit" variant="primary">Post</b-button>
                                </div>
                            </b-form-group>
                            
                                                    
                        </div>

                    </form>

                

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {

    data () {
        return {
            form: {
                name: '',
                text: '',
                created_at: null
            }
        }
    },
    methods: {

        onSubmit (evt) {
            evt.preventDefault();

            const path = `${process.env.BASE_URI}tweets/`;

            axios.post(path, this.form).then((response) => { 
                
                this.form.title = response.data.name;
                this.form.description = response.data.text;

                swal("Done!!! Tweet was posted", "", "success")
                .then((value) => {
                    this.form.name = ""
                    this.form.text = ""
                     this.$emit('tweetPosted')
                })

            })
            .catch((error) => {
                console.log(error)
                swal("Sorry!!! Tweet was not posted", "", "error")
            })
        }

    },

    computed: {
        isDisabled: function() {
            return this.form.name.length == 0 || this.form.text.length < 50;
        }
    }
    
}
</script>

<style lang="css" scoped>

.myFormContainer {
    display: flex;
    justify-content: flex-end;
    align-items: center;
}

</style>