import axios from "axios";
import apartment from './apartment.jpeg';

import React, { useState } from "react";
import {
  Grid,
  Typography,
  Container,
  Paper,
  Card,
  CardContent,
  CardActions,
  Button
} from "@material-ui/core";
import { CardActionArea, CardMedia } from "@mui/material";
import styled from 'styled-components';
import InfiniteScroll from "react-infinite-scroll-component";

const MyCard = styled(Card)`
  height: 300px;
  width: 470px;
`;

export default function PreviewBlock(props: any) {
  return (
    <div style={{marginLeft: '30px'}}>
      <Scroll/>
    </div>
  );
};

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

const Scroll = (props: any) => {
  const initialArray = [ // workaround until api works
    <SingleCard
    aptName="ab"
    address="asdf"
    />,
    <SingleCard
    aptName="ab"
    address="asdf"
    />,
    <SingleCard
    aptName="ab"
    address="asdf"
    />,
    <SingleCard
    aptName="ab"
    address="asdf"
    />
  ]
  const [items, setItems] = useState(initialArray);
  const [hasMore, setHasMore] = useState(true); // hasMore apartments

  const fetchData = () => {
    if (items.length >= 200) { // stop calling the api after 200 elements
      setHasMore(false);
      return;
    }
    setTimeout(() => { // at bottom of elements, so we call the api to concat the array of apartments
      axios.get('/login')
      .then(function (response) {
        console.log(response.data.apartment);
        setItems([
          // populate array with apartment items from get request (don't know how)
          ...items
        ]);
      })
      .then(function (error) {
        console.log(error);
      })
      .then(function () {});
    }, 500);
  };

  return (
    <>
      <InfiniteScroll
      dataLength={20}
      next={fetchData}
      hasMore={hasMore}
      loader={<h4>Loading ...</h4>}
      endMessage={
        <p style={{ textAlign: "center" }}>
          <b>No more apartments</b>
        </p>
      }
      >
        {items.map((component, index) => (
          component
        ))}
      </InfiniteScroll>
    </>
  );
}
