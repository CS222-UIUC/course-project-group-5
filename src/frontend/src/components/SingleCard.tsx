import React from 'react';
import { Typography, Card, CardContent } from '@material-ui/core';
import { CardActionArea } from '@mui/material';
import styled from 'styled-components';
import { AptType } from './Types';

const Container = styled.div``;

const MyCard = styled(Card)`
   margin-left: 20px;
   margin-bottom: 20px;
   height: 200px;
   width: 470px;
`;

interface SingleCardProps {
   id: number;
   name: string;
   address: string;
   price_min: number;
   price_max: number;
   votes: number;
   onSelect: (apt: AptType) => void;
}

const SingleCard = ({
   id,
   name,
   address,
   price_min,
   price_max,
   votes,
   onSelect,
}: SingleCardProps) => (
   // <Container>
   //    <Alert variant="secondary">
   //       <h5>{name}</h5>
   //       <h6>{address}</h6>
   //       <h4>
   //          ${price_min}-${price_max}
   //       </h4>
   //       <h2>{rating}</h2>
   //    </Alert>
   // </Container>
   <Container className="h-25">
      <MyCard>
         {' '}
         <CardActionArea
            onClick={() =>
               onSelect({ id, name, address, price_min, price_max, votes })
            }
         >
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
                     {/* {rating} */}
                  </Typography>
               </div>
            </CardContent>
         </CardActionArea>
      </MyCard>
   </Container>
);

export default SingleCard;
