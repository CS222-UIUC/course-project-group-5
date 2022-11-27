import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
// import { cp } from 'fs';
import {
   Card,
   CardContent,
   Avatar,
   CardHeader,
   Typography,
   Stack,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import ThumbDownIcon from '@mui/icons-material/ThumbDown';
interface ReviewCardProps {
   username: string;
   date: string;
   comment: string;
   vote: boolean;
}
const ReviewCard = ({ username, date, comment, vote }: ReviewCardProps) => {
   return (
      <React.Fragment>
         <Card>
            <CardHeader
               avatar={
                  <Avatar>
                     <PersonIcon/>
                  </Avatar>
               }
               title={username}
               subheader={date}
            />
            <CardContent>
               <Stack spacing={1}>
                  <Typography variant="body1">
                     {comment}
                  </Typography>
                  {vote === true &&
                  <Avatar sx={{ width: 29, height: 29 }}>
                     <ThumbUpIcon/>
                  </Avatar>}
                  {vote !== true &&
                  <Avatar>
                     <ThumbDownIcon/>
                  </Avatar>}
               </Stack>
            </CardContent>
         </Card>
      </React.Fragment>
   );
};

export default ReviewCard;
