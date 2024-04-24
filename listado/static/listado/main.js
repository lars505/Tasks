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