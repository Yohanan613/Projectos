import "./App.css"
import TaskBoard from "./components/TaskBoard"
import TaskForm from "./components/TaskForm"

function App() {

  return (
    <div>

      <h1>Tablero de Tareas</h1>

      <TaskForm />

      <TaskBoard />

    </div>
  )

}

export default App