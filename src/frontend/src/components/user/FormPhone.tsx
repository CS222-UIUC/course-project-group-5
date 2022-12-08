import axios from 'axios';
import {
   Grid,
   Typography,
   ListItemText,
   Box,
   Stack,
   Button,
   ListItemAvatar,
   Avatar,
   ListItem,
   TextField,
} from '@mui/material';
import React, { useState, Dispatch, SetStateAction } from 'react';
import PhoneIcon from '@mui/icons-material/Phone';

const baseURL = 'http://127.0.0.1:5000/user';
interface PhoneComponentProps {
   displayPhone: string;
   setDisplayPhone: Dispatch<SetStateAction<string>>;
}

export function FormPhone({
   displayPhone,
   setDisplayPhone,
}: PhoneComponentProps) {
   const [editPhone, setEditPhone] = useState(false);
   const [newPhone, setNewPhone] = useState('');
   const [success, setSuccess] = useState(true);

   function changePhone(new_phone: string) {
      const req = {
         is_phone: true,
         phone: new_phone,
      };
      const json = JSON.stringify(req);
      axios({
         method: 'POST',
         url: `${baseURL}`,
         data: json,
         withCredentials: true,
      })
         .then((response) => {
            console.log(response);
            setDisplayPhone(newPhone);
            setEditPhone(false);
            setSuccess(true);
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
               setSuccess(false);
            }
         });
   }

   return (
      <React.Fragment>
         {/* Phone box changes based on click */}
         {editPhone === false && (
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <PhoneIcon />
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Phone number" secondary={displayPhone} />
               <Button
                  color="primary"
                  variant="outlined"
                  onClick={() => {
                     setEditPhone(true);
                  }}
               >
                  <Typography variant="subtitle2">Change phone</Typography>
               </Button>
            </ListItem>
         )}
         {editPhone === true && (
            <ListItem>
               <Stack>
                  <Grid container spacing={1}>
                     <Grid item xs={12}>
                        <TextField
                           label="Phone"
                           variant="outlined"
                           fullWidth
                           onChange={(event) => {
                              setNewPhone(event.target.value);
                           }}
                        />
                     </Grid>
                     <Grid item xs>
                        <Box display="flex" justifyContent="flex-end">
                           <Button
                              type="submit"
                              color="primary"
                              variant="contained"
                              size="small"
                              onClick={() => setEditPhone(false)}
                           >
                              Cancel
                           </Button>
                        </Box>
                     </Grid>
                     <Grid item xs={2}>
                        <Box display="flex" justifyContent="flex-end">
                           <Button
                              type="submit"
                              color="primary"
                              variant="contained"
                              size="small"
                              onClick={() => changePhone(newPhone)}
                           >
                              Submit
                           </Button>
                        </Box>
                     </Grid>
                  </Grid>
                  {success === false && (
                     <Typography sx={{ color: '#ff0000' }}>
                        Invalid phone number
                     </Typography>
                  )}
               </Stack>
            </ListItem>
         )}
      </React.Fragment>
   );
}
