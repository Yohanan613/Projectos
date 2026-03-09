import { useState } from "react"

export default function TaskForm(){

  const [titulo,setTitulo] = useState("")
  const [descripcion,setDescripcion] = useState("")

  const crearTarea = async (e)=>{

    e.preventDefault()

    await fetch("http://localhost:5000/tareas",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        titulo,
        descripcion
      })
    })

    location.reload()

  }

  return(

    <form onSubmit={crearTarea}>

      <input
        placeholder="Titulo"
        value={titulo}
        onChange={e=>setTitulo(e.target.value)}
      />

      <textarea
        placeholder="Descripcion"
        value={descripcion}
        onChange={e=>setDescripcion(e.target.value)}
      />

      <button>
        Agregar
      </button>

    </form>

  )

}