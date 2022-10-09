import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './components/Login'
import Header from './components/Header' 
import Register from './components/Register';
import {useState} from 'react';

function App() {

  return (
    <div className="App">
      <Header/>
      {/* need to add routing to switch between register/login */}
      <Register/> 
    </div>
  );
}

export default App;
