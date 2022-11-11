import React, { useState } from 'react';
import getApartments from '../components/mainpageleft/getApts';
import Populate from '../components/mainpageleft/PopulateLeftSection';
import SearchBar from '../components/SearchBar';
import { AptType } from '../components/Types';
import RightSection from '../sections/MainPageRightSection';

function MainPage() {
   const { apartments } = getApartments('0', '0', -1);
   const [to, setTo] = useState<AptType>(apartments[0]);
   return (
<<<<<<< HEAD
      <div>
         <SearchBar />
         <div className="d-flex flex-row">
            <div className="w-50">
<<<<<<< HEAD
               <Populate />
=======
               <SearchBar />
               <Populate onSelect={(apt) => setTo(apt)} />
>>>>>>> f1bfa98339d10778892fa18c6638d635a0bf4f96
            </div>
            <div className="w-50">
               <RightSection apt={to || apartments[0]} />
=======
      <>
         <div className="Header" style={{ height: '200px' }}>
            <SearchBar />
         </div>
         <div className="Content">
            <div className="Wrapper">
               <div
                  className="Right"
                  style={{ width: '1000px', float: 'right', height: '500px' }}
               >
                  <RightSection apt={to || apartments[0]} />
               </div>
               <div className="Left">
                  <Populate onSelect={(apt) => setTo(apt)} />
               </div>
>>>>>>> 32bff1c1a3108ad1be6ee951585ca73c9bd24963
            </div>
         </div>
      </>
   );
}
export default MainPage;
