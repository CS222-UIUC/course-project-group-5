import React from 'react';
import './App.css';
import Login from './components/Login';
import Header from './components/Header';
import LeftSection from './sections/MainPageLeftSection';
import Searchbar from './components/Searchbar';
import Searching from './components/Searching';

function App() {
  return (
    <div className="App">
      {/*<LeftSection/>
      <Header/>*/}
      <Searching/>
      {/*<Login/>*/}
    </div>
  );
}

export default App;
