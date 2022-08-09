var mySlider;
function newvar_p(minimo,maximo){
    mySlider = new rSlider({
        target: document.getElementById('Slider'),
        values: {min:minimo,max:maximo},
        range: true,
        tooltip: true,
        scale: true,
        labels: false,
        step:1,
        set: [minimo, maximo],
        onChange: function(){ 
                xhr.open("GET", "/filtrar_peliculas?nombre="+buscador.value+"&fecha="+mySlider.getValue());  
                xhr.send();
        }
    });
}
