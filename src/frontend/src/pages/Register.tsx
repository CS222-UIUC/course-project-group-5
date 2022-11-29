import React, { useEffect, useState } from 'react';
import {
   Grid,
   Paper,
   TextField,
   Button,
   Typography,
   Link,
   FormControlLabel,
   Checkbox,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Register() {
   const [user, setUser] = useState('');
   const [email, setEmail] = useState('');
   const [password, setPassword] = useState('');
   const [number, setNumber] = useState('');
   const [res, setRes] = useState();
   const paperStyle = {
      padding: 20,
      height: '75vh',
      width: 310,
      margin: '20px auto',
   };
   const btnstyle = { margin: '8px 0' };

   function sendData() {
      axios({
         method: 'POST',
         url: 'http://127.0.0.1:5000/register',
         withCredentials: true,
         data: {
            username: user,
            email: email,
            password: password,
            phone: number,
         },
      })
         .then((response) => {
            console.log(response);
            setRes(response.data);
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
               setRes(error.response.data);
            }
         });
   }
   const navigate = useNavigate();

   useEffect(() => {
      if (res === `Register successful, welcome ${user}`) {
         setTimeout(() => {
            navigate('/login');
         }, 3000);
      }
   }, [res, user, navigate]);

   return (
      <Grid>
         <Paper elevation={12} style={paperStyle}>
            {/* A paper like UI with fields for register*/}
            <PersonIcon fontSize="large" />
            <h2>Register</h2>
            <TextField
               label="Username"
               placeholder="Ex: user1"
               onChange={(event) => setUser(event.target.value)}
               fullWidth
               required
            />
            <TextField
               label="Email"
               placeholder="Ex: user1@gmail.com"
               onChange={(event) => setEmail(event.target.value)}
               fullWidth
               required
            />
            <TextField
               label="Password"
               placeholder="Ex: user1password!"
               onChange={(event) => setPassword(event.target.value)}
               type="password"
               fullWidth
               required
            />
            <TextField
               label="Phone"
               placeholder="Ex: (000)-000-0000"
               onChange={(event) => setNumber(event.target.value)}
               fullWidth
               required
            />
            <FormControlLabel
               control={<Checkbox name="checkedB" color="primary" />}
               label="Remember me"
            />
            <Button
               type="submit"
               color="primary"
               variant="contained"
               style={btnstyle}
               onClick={sendData}
               fullWidth
            >
               Sign up
            </Button>
            <Typography>
               <Link href="/login">Already signed up?</Link>
            </Typography>
            {res === `Register successful, welcome ${user}` && (
               <Typography sx={{ color: '#0000ff' }}>
                  {res + '. You will be directed to the login page shortly.'}
               </Typography>
            )}
            {res !== undefined &&
               res !== `Register successful, welcome ${user}` && (
                  <Typography sx={{ color: '#ff0000' }}>{res}</Typography>
               )}
         </Paper>
      </Grid>
   );
}
