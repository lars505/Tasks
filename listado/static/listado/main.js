document.addEventListener("DOMContentLoaded", function () {
    console.log("Hola!")

    const formulario = document.querySelector("#formulario-agregar");
    formulario.style.display = 'none';
    cargarLista()

    document.querySelector("#formulario").addEventListener('submit', add_tasks);
})

function cargarLista(){
    fetch(`tasks`,{
        method: "GET"
    })
    .then(response => response.json())
    .then( data => {
        console.log(data)
        const tasks =  data.tasks;

        tasks.forEach(task => {

            const li = document.createElement('li')
            const div = document.createElement('div')
            const div2 = document.createElement('div')
            const span = document.createElement('span')
            const a = document.createElement('a')
            const a2 = document.createElement('a')
            const span2 = document.createElement('span')
            const span3 = document.createElement('span')

            li.classList.add("list-group-item")
            li.classList.add("d-flex")
            li.classList.add("justify-content-between")
            li.classList.add("mb-2")

            div.classList.add("d-flex")
            div.classList.add("flex-column")

            div2.classList.add("iconos")
            div2.classList.add("d-flex")
            div2.classList.add("justify-content-center")
            div2.classList.add("align-items-center")
            
            a.classList.add("d-flex")
            a.setAttribute('href', "{% url 'realizada' task.id %}")
            a2.classList.add("d-flex")
            a2.setAttribute('href', "{% url 'eliminar' task.pk %}")
            
            span2.classList.add("material-symbols-outlined")
            span2.classList.add("done")
            span2.innerHTML = "done"
            
            span3.classList.add("material-symbols-outlined")
            span3.classList.add("trash")
            span3.innerHTML = "delete"
            
            span.classList.add("form-text")

            div.innerHTML = task.titulo;
            span.innerHTML = task.descripcion;

            li.append(div)
            div.append(span)
            a.append(span2)
            a2.append(span3)
            div2.append(a)
            div2.append(a2)
            li.append(div2)
            

            document.querySelector("#ul-tasks").append(li);

        })

    })

}

function ver_formulario(){
    console.log("Funciona!")

    document.querySelector("header").style.display = 'none';
    document.querySelector("#tasks").style.display = 'none';
    document.querySelector("#tasks-realizadas").style.display = 'none';
    document.querySelector("#formulario-agregar").style.display = 'block';

}

function add_tasks(event){
    event.preventDefault();
    const titulo = document.querySelector('#titulo').value;
    const descripcion = document.querySelector('#descripcion').value;

    fetch('agregar',
    {
        method : 'POST',
        headers:{
            'X-CSRFToken': obtenerCSRFToken('csrftoken')
        },
        body : JSON.stringify({
            'titulo': titulo,
            'descripcion': descripcion
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.querySelector('header').style.display='block'
        document.querySelector('#tasks').style.display='block'
        document.querySelector('#tasks-realizadas').style.display='block'
        document.querySelector('#formulario-agregar').style.display='none'
        document.querySelector('#ul-tasks').innerHTML = '';
        
        cargarLista();
    })
    return 1;
}

function obtenerCSRFToken(nombre){
    const coockieString = document.cookie;
    const coockie = coockieString.split(';');

    for (let cookie of coockie){
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName == nombre){

            console.log(cookieValue)
            return cookieValue
        }
    }
    return '';
    
}