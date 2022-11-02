import React from 'react';
import { Typography, Card, CardContent } from '@material-ui/core';
import { CardActionArea, CardMedia } from '@mui/material';
import styled from 'styled-components';
import image from '../image.jpeg';

const Container = styled.div``;

const MyCard = styled(Card)`
   margin-left: 20px;
   margin-bottom: 20px;
   height: 300px;
   width: 470px;
`;

interface SingleCardProps {
   name: string;
   address: string;
   rating: number;
   price_min: number;
   price_max: number;
}

const SingleCard = ({
   name,
   address,
   rating,
   price_min,
   price_max,
}: SingleCardProps) => (
   <Container>
      <MyCard>
         {' '}
         <CardActionArea>
            <CardMedia component="img" src={image} height="150" />
            <CardContent style={{ height: '300px' }}>
               {/*<Button size="small">Learn More</Button>*/}
               <div style={{ display: 'inline-block', width: '100%' }}>
                  <Typography
                     gutterBottom
                     variant="h5"
                     component="div"
                     style={{ float: 'left', marginLeft: '30px' }}
                  >
                     {name}
                  </Typography>
                  <Typography
                     gutterBottom
                     variant="body1"
                     component="div"
                     style={{ float: 'right', marginTop: '5px' }}
                  >
                     {address}
                  </Typography>
               </div>
               <div>
                  <Typography
                     gutterBottom
                     variant="body2"
                     component="div"
                     style={{ float: 'left' }}
                  >
                     {/*review*/}
                  </Typography>
                  <Typography
                     gutterBottom
                     variant="body2"
                     component="div"
                     style={{ float: 'right' }}
                  >
                     ${price_min}-${price_max}
                  </Typography>
                  <Typography
                     gutterBottom
                     variant="body2"
                     component="div"
                     style={{ float: 'left' }}
                  >
                     {rating}
                  </Typography>
               </div>
            </CardContent>
         </CardActionArea>
      </MyCard>
   </Container>
);

export default SingleCard;
