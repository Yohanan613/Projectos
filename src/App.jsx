import TaskBoard from "./components/TaskBoard"
import TaskForm from "./components/TaskForm"
import "./App.css"

export default function App() {

  return (
    <div style={{padding:"20px"}}>
      <h1>Tablero de Tareas</h1>

      <TaskForm/>

      <TaskBoard/>
    </div>
  )
}