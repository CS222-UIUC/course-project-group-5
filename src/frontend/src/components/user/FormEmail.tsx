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
import EmailIcon from '@mui/icons-material/Email';

interface EmailComponentProps {
   displayEmail: string;
   setDisplayEmail: Dispatch<SetStateAction<string>>;
}
const baseURL = 'http://127.0.0.1:5000/user';

export function FormEmail({
   displayEmail,
   setDisplayEmail,
}: EmailComponentProps) {
   const [editEmail, setEditEmail] = useState(false);
   const [newEmail, setNewEmail] = useState('');
   const [success, setSuccess] = useState(true);

   function changeEmail(new_email: string) {
      const req = {
         is_email: true,
         email: new_email,
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
            setDisplayEmail(newEmail);
            setEditEmail(false);
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
         {/* Email box changes based on click */}
         {editEmail === false && (
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <EmailIcon />
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Email" secondary={displayEmail} />
               <Button
                  color="primary"
                  variant="outlined"
                  onClick={() => setEditEmail(true)}
               >
                  <Typography variant="subtitle2">Change email</Typography>
               </Button>
            </ListItem>
         )}
         {editEmail === true && (
            <ListItem>
               <Stack>
                  <Grid container spacing={1}>
                     <Grid item xs={12}>
                        <TextField
                           label="Email"
                           variant="outlined"
                           fullWidth
                           onChange={(event) => {
                              setNewEmail(event.target.value);
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
                              onClick={() => setEditEmail(false)}
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
                              onClick={() => {
                                 changeEmail(newEmail);
                              }}
                           >
                              Submit
                           </Button>
                        </Box>
                     </Grid>
                  </Grid>
                  {success === false && (
                     <Typography sx={{ color: '#ff0000' }}>
                        Invalid Email
                     </Typography>
                  )}
               </Stack>
            </ListItem>
         )}
      </React.Fragment>
   );
}
