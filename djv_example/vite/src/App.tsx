import { useState, useEffect } from 'react';
import { djangoVite } from './api/django-vite'; 
import './App.css'

function App() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
	(async () => {
		const resp = await djangoVite.get('/api/users/');
		console.log(resp);
	})();
		// eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

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
