
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
        xhr.open("GET", "/filtrar_canciones?nombre="+buscador.value+"&fecha="+mySlider.getValue());    
        xhr.send();
        document.getElementById("myForm").style.display = "none";
    }  
}

function playlist_add_musica(id_cancion,id_playlist){
    xhr2.open("GET", "/add_musica_playlist?id="+id_cancion+"&playlist="+id_playlist);
    xhr2.send();
}
var id_cancion;
function form_nueva_playlist(id){
    id_cancion=id;
    document.getElementById("myForm").style.display = "block";
}
function closeForm(){
    document.getElementById("myForm").style.display = "none";
}
function new_playlist(){
    var nombre=document.getElementById('nombre').value;
    xhr3.open("GET", "/nueva_playlist_musica?id="+id_cancion+"&nombre="+nombre);
    xhr3.send();

    
}