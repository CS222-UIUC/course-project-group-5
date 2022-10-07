import React from 'react';
import { Grid, Paper, Avatar, TextField, Button, Typography, Link, FormControlLabel, Checkbox } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';

export default function Register() {

  const paperStyle = { padding: 20, height: '55vh', width: 310, margin: "20px auto" }
  const btnstyle = { margin: '8px 0' }
  return (
    <Grid>
      <Paper elevation={12} style={paperStyle}>
        <PersonIcon fontSize="large" />
        <h2>Register</h2>
        <TextField label='Username' placeholder='Ex: user1' fullWidth required />
        <TextField label='Email' placeholder='Ex: user1@gmail.com' fullWidth required />
        <TextField label='Password' placeholder='Ex: user1password!' type='password' fullWidth required />
        <TextField label='Phone' placeholder='Ex: (000)-000-0000' fullWidth required />


        <FormControlLabel
          control={
            <Checkbox
              name="checkedB"
              color="primary"
            />
          }
          label="Remember me"
        />
        <Button type='submit' color="primary" variant="contained" style={btnstyle} fullWidth>Sign up</Button>
        <Typography >
          <Link href="#" >
            Already signed up?
          </Link>
        </Typography>
      </Paper>
    </Grid>
  )
}


