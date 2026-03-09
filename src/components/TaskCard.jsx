export default function TaskCard({tarea}){

  const mover = async (nuevoEstado)=>{

    await fetch(`http://localhost:5000/tareas/${tarea.id}`,{
      method:"PUT",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        estado:nuevoEstado
      })
    })

    location.reload()

  }

  return(

    <div className="tarea">

      <strong>{tarea.titulo}</strong>

      <p>{tarea.descripcion}</p>

      <div className="acciones">

        {tarea.estado>0 &&
          <button onClick={()=>mover(tarea.estado-1)}>
            ⬅
          </button>
        }

        {tarea.estado<4 &&
          <button onClick={()=>mover(tarea.estado+1)}>
            ➡
          </button>
        }

      </div>

    </div>

  )

}