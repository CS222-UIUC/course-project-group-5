import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Login from './pages/Login';
import MainPage from './pages/MainPage';
//import UserPage from './pages/UserPage';

function App() {
   return (
      <>
         <BrowserRouter>
            <Routes>
               <Route path="/login">
                  <Route index element={<Login />} />
               </Route>
               <Route path="/">
                  <Route index element={<MainPage />} />
               </Route>
               {/* <Route path="/user">
                  <Route index element={<UserPage />} />
               </Route> */}
            </Routes>
         </BrowserRouter>
      </>
   );
}
export default App;
