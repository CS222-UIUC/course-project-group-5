import React, { useState } from 'react';
import { Row, Col } from 'react-bootstrap';
import getApartments from '../components/mainpageleft/getApts';
import Populate from '../components/mainpageleft/PopulateLeftSection';
import SearchBar from '../components/SearchBar';
import { AptType } from '../components/Types';
import RightSection from '../sections/MainPageRightSection';

function MainPage() {
   const { apartments } = getApartments('0', '0', -1);
   const [to, setTo] = useState<AptType>(apartments[0]);
   return (
      <>
         <SearchBar />
         <div className="container" style={{ paddingTop: '100px' }}>
            <Row>
               <Col>
                  <Populate onSelect={(apt) => setTo(apt)} />
               </Col>
               <Col>
                  <RightSection apt={to || apartments[0]} />
               </Col>
            </Row>
         </div>
      </>
   );
}
export default MainPage;
