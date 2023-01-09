import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <h1>Django Vite Example</h1>
      <p className="read-the-docs">
        A reusable Django app integrated with vite.
      </p>
    </div>
  )
}

export default App
