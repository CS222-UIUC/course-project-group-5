import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './components/Login'
import Header from './components/Header' 
import Register from './components/Register';
function App() {
  return (
    <div className="App">
      <Header/>
      <Register/>
    </div>
  );
}

export default App;
