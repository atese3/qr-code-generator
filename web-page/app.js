const app = Vue.createApp(
    {
        data() {
            return {
                fillColor: "#000000",
                backgroundColor: "#FFFFFF",
                isTransparent: true,
                qrData: "atesemre.com",
                img: ""
            }
        },
        methods: {
            generate_qr_code(){
                axios
                .post('http://127.0.0.1:5000/generate', {
                                                            fillColor: this.fillColor, 
                                                            backgroundColor: this.backgroundColor, 
                                                            isTransparent: this.isTransparent, 
                                                            qrData: this.qrData
                                                        }).then(response => (this.img = response.data))
            }
        },        
        created() {
            this.generate_qr_code();
        }
    }
);
app.mount('#app');