import * as React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
// import { PicType } from './Types';
import Carousel from 'react-bootstrap/Carousel';

export interface IImagesGalleryProps {
   pics: string[];
}

const ImagesGallery = ({ pics }: IImagesGalleryProps) => {
   return (
<<<<<<< HEAD:src/frontend/src/components/ImagesGallery.tsx
      <div className="d-flex text-center">
         <Carousel>
            {pics.map((pic) => (
               <Carousel.Item key={pic}>
                  <img className="d-block w-100" src={pic} alt="" />
               </Carousel.Item>
            ))}
         </Carousel>
      </div>
=======
      <Carousel>
         {pics.map((pic) => (
            <Carousel.Item key={pic} style={{ height: '500px' }}>
               <img className="d-block w-100" src={pic} alt="" />
            </Carousel.Item>
         ))}
      </Carousel>
>>>>>>> 32bff1c1a3108ad1be6ee951585ca73c9bd24963:src/frontend/src/components/mainpageright/ImagesGallery.tsx
   );
};

export default ImagesGallery;
