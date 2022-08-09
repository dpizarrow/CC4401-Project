
var xhr2 = new XMLHttpRequest();
xhr2.onreadystatechange = function(){
    if(xhr2.readyState===4 && xhr2.status===200){
        let response = xhr2.responseText;
        response = JSON.parse(response)['context'];
        alert(response);
    }
    
}

var xhr3 = new XMLHttpRequest();
xhr3.onreadystatechange = function(){
    if(xhr3.readyState===4 && xhr3.status===200){
        let response = xhr3.responseText;
        response = JSON.parse(response)['context'];
        alert(response);
        xhr.open("GET", "/filtrar_peliculas?nombre="+buscador.value+"&fecha="+mySlider.getValue());    
        xhr.send();
        document.getElementById("myForm").style.display = "none";
    }  
}

function playlist_add_pelicula(id_pelicula,id_playlist){
    xhr2.open("GET", "/add_pelicula_playlist?id="+id_pelicula+"&playlist="+id_playlist);
    xhr2.send();
}

var id_pelicula;
function form_nueva_playlist(id){
    id_pelicula=id;
    document.getElementById("myForm").style.display = "block";
}
function closeForm(){
    document.getElementById("myForm").style.display = "none";
}
function new_playlist(){
    var nombre=document.getElementById('nombre').value;
    xhr3.open("GET", "/nueva_playlist_pelicula?id="+id_pelicula+"&nombre="+nombre);
    xhr3.send();

    
}