
function guardar() {
    let n = document.getElementById("nombre").value
    let a = document.getElementById("apellido").value
    let p = parseInt(document.getElementById("posicion").value)
    let i = document.getElementById("imagen").value

    // {
    //     "imagen": "https://picsum.photos/200/300?grayscale",
    //     "nombre": "MICROONDAS",
    //     "precio": 50000,
    //     "stock": 10
    //   }
    if (n == "") {
        alert("Ingrese nombre jugador");
        return false;
    }

    if (a == "") {
        alert("Ingrese apellido jugador");
        return false;
    }

    if (p == "") {
        alert("Ingrese dorsal jugador");
        return false;
    }
    if (i == "") {
        alert("Ingrese imagen jugador");
        return false;
    } 
    let jugador = {
        nombre: n,
        apellido: a,
        posicion: p,
        imagen: i
    }
    let url = "http://localhost:5000/jugadores"
    var options = {
        body: JSON.stringify(jugador),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            //alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "./jugadores.html";  
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}

function validarFormulario() {
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var telefono = document.getElementById("posicion").value;
    var email = document.getElementById("imagen").value;

    if (nombre == "") {
        alert("Ingrese nombre jugador");
        return false;
    }

    if (apellido == "") {
        alert("Ingrese apellido jugador");
        return false;
    }

    if (posicion == "") {
        alert("Ingrese dorsal jugador");
        return false;
    }
    if (imagen == "") {
        alert("Ingrese imagen jugador");
        return false;
    }

    alert("Formulario enviado corectamente");
    return true;
}