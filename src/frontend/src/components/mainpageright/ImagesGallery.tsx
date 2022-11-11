import * as React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
// import { PicType } from './Types';
import Carousel from 'react-bootstrap/Carousel';

export interface IImagesGalleryProps {
   pics: string[];
}

const ImagesGallery = ({ pics }: IImagesGalleryProps) => {
   return (
      <Carousel>
         {pics.map((pic) => (
            <Carousel.Item key={pic} style={{ height: '500px' }}>
               <img className="d-block w-100" src={pic} alt="" />
            </Carousel.Item>
         ))}
      </Carousel>
   );
};

export default ImagesGallery;
