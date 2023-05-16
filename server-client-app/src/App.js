// App.js
import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [wasteTypes, setWasteTypes] = useState([]);
  const [containers, setContainers] = useState([]);
  
  const [selectedWasteNumber, setSelectedWasteNumber] = useState(1);
  const [selectedWasteType, setSelectedWasteType] = useState('');
  const [wasteList, setWasteList] = useState([]);

  const [selectedContainerNumber, setSelectedContainerNumber] = useState(1);
  const [selectedContainer, setSelectedContainer] = useState('');
  const [containerList, setContainerList] = useState([]);

  const [status, setStatus] = useState('');
  
  const numbers = Array.from({ length: 100 }, (_, i) => i + 1);


  useEffect(() => {
    console.log('Waste list:', wasteList);
  }, [wasteList]);

  useEffect(() => {
    console.log('Container list:', containerList);
  }, [containerList]);


  useEffect(() => {
    axios.get("http://localhost:5000/waste-types").then((response) => {
      setWasteTypes(response.data);
    });
    axios.get("http://localhost:5000/container-names").then((response) => {
      setContainers(response.data);
    });
  }, []);


  const addWaste = () => {
    setWasteList([...wasteList, { type: selectedWasteType, number: selectedWasteNumber }]);
  };

  const addContainer = () => {
    setContainerList([...containerList, { name: selectedContainer, number: selectedContainerNumber }]);
  };

  const storedProcedure = async () => {
    try {
      const response = await axios.get("http://localhost:5000/execute-sp");
      setStatus(response.data);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  const submitWaste = () => {
    // send POST request to server with selected waste types
    axios.post('http://localhost:5000/submit-waste-types', JSON.stringify(wasteList), {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      console.log(response);
    })
    .catch(error => {
      console.error(error);
    });
  };

  const submitContainers = () => {
    // send POST request to server with selected containers
    axios.post('http://localhost:5000/submit-containers', JSON.stringify(containerList), {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      console.log(response);
    })
    .catch(error => {
      console.error(error);
    });
  };

  return (
    <div className="App">
      <h1>Driver: Manuel Granados</h1>
      <h2>Destination: Costa Rica Calle 1, San Juan, PR</h2>
      <h2>Collector: Esencial Verde</h2>
      <h2>Producer: Taco Bell</h2>
      <div>
        <h3>Waste to pickup</h3>
        <select onChange={e => setSelectedWasteNumber(Number(e.target.value))}>{numbers.map((num) => <option key={num}>{num}</option>)}</select>
        <select onChange={e => setSelectedWasteType(e.target.value)}>{wasteTypes.map((type) => <option key={type.name}>{type.name}</option>)}</select>
        <button onClick={addWaste}>Add Waste</button>
        <button onClick={submitWaste}>Submit Waste Types</button>
      </div>
      <div>
        <h3>Container to deliver</h3>
        <select onChange={e => setSelectedContainerNumber(Number(e.target.value))}>{numbers.map((num) => <option key={num}>{num}</option>)}</select>
        <select onChange={e => setSelectedContainer(e.target.value)}>{containers.map((container) => <option key={container.name}>{container.name}</option>)}</select>
        <button onClick={addContainer}>Add Container</button>
        <button onClick={submitContainers}>Submit Containers</button>
      </div>
      <div>
        <button onClick={storedProcedure}>Confirm Exchange</button>
        {status && 
        <div>
          <p>Status: {status.Status}</p>
          <p>Message: {status.Messsage}</p>
        </div>
        }
      </div>
    </div>
  );
}

export default App;










// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
