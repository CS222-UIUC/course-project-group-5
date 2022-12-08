import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Login from './pages/Login';
import MainPage from './pages/MainPage';
import Register from './pages/Register';
import User from './pages/User';

function App() {
   return (
      <>
         <BrowserRouter>
            <div style={{ height: '80px', textAlign: 'center' }}>
               <Header />
            </div>
            <Routes>
               <Route path="/login">
                  <Route index element={<Login />} />
               </Route>
               <Route path="/register">
                  <Route index element={<Register />} />
               </Route>
               <Route path="/">
                  <Route index element={<MainPage />} />
               </Route>
               <Route path="/user">
                  <Route index element={<User />} />
               </Route>
            </Routes>
         </BrowserRouter>
      </>
   );
}
export default App;
