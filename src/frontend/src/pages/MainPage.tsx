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
         <div className="d-flex flex-row">
            <div className="w-50">
               <SearchBar />
               <Populate onSelect={(apt) => setTo(apt)} />
            </div>
            <div className="w-50">
               <RightSection apt={to || apartments[0]} />
            </div>
         </div>
      </div>
   );
}
export default MainPage;
