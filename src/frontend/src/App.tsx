import React from 'react';
import './App.css';
import Header from './components/Header';
import Register from './components/Register';
import Login from './components/Login';

function App() {
   return (
      <div className="App">
         <Header />
         {/* need to add routing to switch between register/login */}
         <Register />
      </div>
   );
}

export default App;
