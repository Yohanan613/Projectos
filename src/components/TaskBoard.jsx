import { useEffect, useState } from "react"
import TaskCard from "./TaskCard"

const estados = [
  "Por iniciar",
  "En proceso",
  "Terminadas",
  "En revisión",
  "Completas"
]

export default function TaskBoard(){

  const [tareas,setTareas] = useState([])

  useEffect(()=>{

    fetch("http://localhost:5000/tareas")
      .then(res => res.json())
      .then(data => setTareas(data))

  },[])

  return(

    <div className="tablero">

      {estados.map((estado,i)=>(

        <div key={i} className="columna">

          <h3>{estado}</h3>

          {tareas
            .filter(t => t.estado === i)
            .map(t => (
              <TaskCard
                key={t.id}
                tarea={t}
              />
          ))}

        </div>

      ))}

    </div>

  )

}