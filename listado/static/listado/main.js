document.addEventListener("DOMContentLoaded", function () {
    console.log("Hola!")

    const formulario = document.querySelector("#formulario-agregar");
    formulario.style.display = 'none';
    cargarLista()
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
            const span = document.createElement('span')

            li.classList.add("list-group-item")
            li.classList.add("d-flex")
            li.classList.add("mb-2")

            div.classList.add("d-flex")
            div.classList.add("flex-column")
            
            span.classList.add("form-text")

            div.innerHTML = task.titulo;
            span.innerHTML = task.descripcion;

            li.append(div)
            li.append(span)
            

            document.querySelector("#ul-tasks").append(li);

        })

    })

}