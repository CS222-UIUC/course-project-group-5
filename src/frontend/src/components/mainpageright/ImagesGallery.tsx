import * as React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import {
   Card,
   CardMedia,
} from '@mui/material';
import Carousel from 'react-material-ui-carousel'

export interface IImagesGalleryProps {
   pics: string[];
}

const ImagesGallery = ({ pics }: IImagesGalleryProps) => {
   return (
      <React.Fragment>
         <Carousel sx={{ height: 525 }} >
            {pics.map((pic) => (
               <Card key={pic} sx={{ height: 525 }}>
                  <CardMedia
                     component="img"
                     image={pic}
                     sx={{ height: 525 }}
                  >
                  </CardMedia>
               </Card>
            ))}
         </Carousel>
      </React.Fragment>
   );
};

export default ImagesGallery;
