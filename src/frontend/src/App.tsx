import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Login from './components/Login';
import MainPage from './pages/MainPage';

function App() {
   return (
      <div className="App">
         <BrowserRouter>
            <Header />
            <Routes>
               <Route path="/login">
                  <Route index element={<Login />} />
               </Route>
               <Route path="/">
                  <Route index element={<MainPage />} />
               </Route>
            </Routes>
         </BrowserRouter>
      </div>
   );
}
export default App;
