import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://server-djangoquickstack.bunnyenv.com/rest_api/quote/')
    .then(res => res.json())
    .then(data => setData(data.data))
    .then(console.log(data));
  })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h4>Django QuickStack </h4>
        <p>If you see a message below from Django backend, then Django REST APIs works fine with this ReactJS app</p>
        <h4>{data}</h4>
      </header>

      
    </div>
  );
}

export default App;