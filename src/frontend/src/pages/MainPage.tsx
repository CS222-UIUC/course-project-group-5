import React from 'react';
import Searching from '../components/SearchAndDisplayResults';
import LeftSection from '../sections/MainPageLeftSection';

function MainPage() {
   return (
      <div>
         <Searching />
         <LeftSection />
      </div>
   );
}

export default MainPage;
