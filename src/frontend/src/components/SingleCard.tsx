import React from "react";
import {
    Typography,
    Card,
    CardContent,
  } from "@material-ui/core";
import { CardActionArea, CardMedia } from "@mui/material";
import styled from 'styled-components';

const Container = styled.div`
  
`;

const MyCard = styled(Card)`
  margin-left: 20px;
  margin-bottom: 20px;
  height: 300px;
  width: 470px;
`;

interface SingleCardProps {
    name: string,
    address: string,
    image: string,
    review: string,
    priceLow: string,
    priceHigh: string,
    company: string
}

const SingleCard = ({
    name,
    address,
    image,
    review,
    priceLow,
    priceHigh,
    company
   }: SingleCardProps) => (
      <Container>
        <MyCard> {/* 470 */}
          <CardActionArea>
            <CardMedia 
                  component="img" 
                  src={image}
                  height="150"
            />
            <CardContent style={{height: '300px'}}>
                {/*<Button size="small">Learn More</Button>*/}
                <div style={{display: 'inline-block', width: '100%'}}>
                  <Typography gutterBottom variant="h5" component="div" style={{float: 'left', marginLeft: '30px'}}>
                    {name}
                  </Typography>
                  <Typography gutterBottom variant="body1" component="div" style={{float: 'right', marginTop: '5px'}}>
                    {address}
                  </Typography>
                </div>
                <div>
                  <Typography gutterBottom variant="body2" component="div" style={{float: 'left'}}>
                    {review}
                  </Typography>
                  <Typography gutterBottom variant="body2" component="div" style={{float: 'right'}}>
                    ${priceLow}-${priceHigh}
                  </Typography>
                  <Typography gutterBottom variant="body2" component="div" style={{float: 'left'}}>
                    {company}
                  </Typography>
                </div>
            </CardContent>
         </CardActionArea>
        </MyCard>
      </Container>
);

export default SingleCard;