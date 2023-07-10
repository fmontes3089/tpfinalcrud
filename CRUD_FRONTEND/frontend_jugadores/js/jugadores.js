const { createApp } = Vue

  createApp({
    data() {
      return {
        url:"http://127.0.0.1:5000/jugadores",
        jugadores:[],
        error:false,
        cargando:true
      }
    },
    // Se llama después de que la instancia haya 
    // terminado de procesar todas las opciones relacionadas con el estado.
    created() {
        this.fetchData(this.url)
    },
    methods: {
        fetchData(url) {
            // Acá se consume la Api
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.jugadores = data;
                    this.cargando=false
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        // jugadores; es el id que necesita para buscar en la DB y eliminarlo
        eliminar(jugador) {
            const url = 'http://localhost:5000/jugadores/' + jugador;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    alert("Jugador eliminado correctamente")
                    location.reload();
                })
                
        }


    },
    



  }).mount('#app')