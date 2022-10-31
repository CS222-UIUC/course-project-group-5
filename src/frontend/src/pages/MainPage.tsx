import React from 'react';
import { Col, Row } from 'react-bootstrap';
import Searching from '../components/Searching';
import LeftSection from '../sections/MainPageLeftSection';
import RightSection from '../sections/MainPageRightSection';

function MainPage() {
   return (
      <div>
         <div className="d-flex flex-row">
            <div className="w-50">
               <LeftSection />
            </div>
            <div className="w-50">
               <RightSection />
            </div>
         </div>
      </div>
   );
}
export default MainPage;
