import React from "react";
import {
    Typography,
    Card,
    CardContent,
  } from "@material-ui/core";
import { CardActionArea, CardMedia } from "@mui/material";
import styled from 'styled-components';
import apartment from './apartment.jpeg';

const MyCard = styled(Card)`
  height: 300px;
  width: 470px;
`;


interface SingleCardProps {
    aptName: string,
    address: string
  }
const SingleCard = ({
    aptName,
    address
   }: SingleCardProps) => (
      <div>
        <MyCard variant="outlined"> {/* 470 */}
          <CardActionArea>
            <CardMedia 
                  component="img" 
                  src={apartment} 
                  height="150"
            />
            <CardContent style={{height: '300px'}}>
                {/*<Button size="small">Learn More</Button>*/}
                <div style={{display: 'inline-block', width: '100%'}}>
                <Typography gutterBottom variant="h5" component="div" style={{float: 'left'}}>
                  {aptName}
                </Typography>
                <Typography gutterBottom variant="body1" component="div" style={{float: 'right', marginTop: '5px'}}>
                  {address}
                </Typography>
                </div>
            </CardContent>
         </CardActionArea>
        </MyCard>
      </div>
  );

export default SingleCard;