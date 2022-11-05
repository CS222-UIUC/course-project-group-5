import React, { useState } from 'react';
import Populate from '../components/PopulateLeftSection';
import SearchBar from '../components/SearchBar';
import { AptType } from '../components/Types';
import RightSection from '../sections/MainPageRightSection';

function MainPage() {
   const [to, setTo] = useState<AptType>(); // right section will take care of initial state
   return (
      <div>
         <div className="d-flex flex-row">
            <div className="w-50">
               <SearchBar />
               <Populate onSelect={(apt) => setTo(apt)} />
            </div>
            <div className="w-50">
               <RightSection apt={to} />
            </div>
         </div>
      </div>
   );
}
export default MainPage;
