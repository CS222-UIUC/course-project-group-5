import React, { useState } from 'react';
import getApartments from '../components/getApts';
import Populate from '../components/PopulateLeftSection';
import SearchBar from '../components/SearchBar';
import { AptType } from '../components/Types';
import RightSection from '../sections/MainPageRightSection';

function MainPage() {
   const { apartments } = getApartments('', 0, '0', '0');
   const [to, setTo] = useState<AptType>(apartments[0]);
   return (
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
            </div>
         </div>
      </div>
   );
}
export default MainPage;
