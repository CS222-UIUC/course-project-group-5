import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './components/Login'
import Header from './components/Header' 
import Searchbar from './components/Searchbar';
import PreviewBlock from './components/PreviewBlock';

function App() {
  return (
    <div className="App">
      <Searchbar/>
      <PreviewBlock/>
      <Header/>
      <Login/>
    </div>
  );
}

export default App;
