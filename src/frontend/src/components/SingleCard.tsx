import React from 'react';
import {
   Typography,
   Card,
   CardContent,
   Stack,
   CardActionArea,
} from '@mui/material';
import { AptType } from './Types';

interface SingleCardProps {
   id: number;
   name: string;
   address: string;
   price_min: number;
   price_max: number;
   rating: number;
   onSelect: (apt: AptType) => void;
}

const SingleCard = ({
   id,
   name,
   address,
   price_min,
   price_max,
   rating,
   onSelect,
}: SingleCardProps) => (
   <React.Fragment>
      <Card>
         {/* A clickable card with info about an apartment */}
         <CardActionArea
            onClick={() =>
               onSelect({ id, name, address, price_min, price_max, rating })
            }
         >
            <CardContent style={{ height: '175px' }}>
               <Stack>
                  {/*<Button size="small">Learn More</Button>*/}
                  <Typography
                     gutterBottom
                     variant="h5"
                     style={{ float: 'left', marginLeft: '30px' }}
                     component="div"
                  >
                     {name}
                  </Typography>
                  <Typography
                     gutterBottom
                     variant="body1"
                     style={{ float: 'right', marginTop: '5px' }}
                  >
                     {address}
                  </Typography>
                  <Typography
                     gutterBottom
                     variant="body2"
                     style={{ float: 'left' }}
                  >
                     {/*review*/}
                  </Typography>
                  <Typography
                     gutterBottom
                     variant="body2"
                     style={{ float: 'right' }}
                  >
                     ${price_min}-${price_max}
                  </Typography>
                  <Typography
                     gutterBottom
                     variant="body2"
                     style={{ float: 'left' }}
                  >
                     {/* {rating} */}
                  </Typography>
               </Stack>
            </CardContent>
         </CardActionArea>
      </Card>
   </React.Fragment>
);

export default SingleCard;
