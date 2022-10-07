import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './components/Login'
import Header from './components/Header' 
import Searchbar from './components/Searchbar';

function App() {
  return (
    <div className="App">
      <Searchbar/>
      <Header/>
      <Login/>
    </div>
  );
}

export default App;
