var buscador = document.getElementById("busqueda")
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function(){
          if(xhr.readyState===4 && xhr.status===200){
            
            let response = xhr.responseText;
            response = JSON.parse(response)['context'];
            
            var table=document.getElementById("table");
            var td=table.getElementsByTagName("tbody")[0];
            td.parentNode.removeChild(td);
            var row="<tbody>";
            for(i in response){
              
              row+="<tr>";
              row+="<td><img src="+response[i]['url']+" style='max-height:120px; max-width:120px; height:auto; width:auto;'></td>";
              row+="<td>"+response[i]['nombre']+"</td>";
              row+="<td>"+response[i]['artista']+"</td>";
              row+="<td>"+response[i]['genero']+"</td>";
              row+="<td>"+response[i]['album']+"</td>";
              row+="<td>"+response[i]['fecha']+"</td>";
              row+="<td><a href=review_cancion?id="+response[i]['id']+">Click para hacer una review</a></td>";
              row+=`<td>
              <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button"        id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                  Seleccionar playlist
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">`;
              playlist=JSON.parse(response[i]["playlist"])
              
                for(p in playlist){    
                    row+='<li><a class="dropdown-item" onclick="playlist_add_musica('+response[i]['id']+','+playlist[p]['pk']+')">'+playlist[p]['fields'].nombre+'</a></li>'
                  };
                row+=`
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" onclick="form_nueva_playlist(`+response[i]['id']+`)">Nueva Playlist</a></li>`;
              row+=`</ul>
              </div>
            </td>`;
              row+="</tr>";
            }
            row+="</tbody>";
            table.innerHTML+=row;

        }
      }
      buscador.addEventListener("input", function(){
        
        xhr.open("GET", "/filtrar_canciones?nombre="+buscador.value+"&fecha="+mySlider.getValue());
        
        xhr.send();
      })
      
      
      