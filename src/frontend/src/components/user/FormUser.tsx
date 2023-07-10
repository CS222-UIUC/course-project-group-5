import React, { useEffect } from 'react';
import {
   List,
   ListItemText,
   Divider,
   ListItemAvatar,
   Avatar,
   ListItem,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import getInfo from './getUser';
import { FormEmail } from './FormEmail';
import { FormPhone } from './FormPhone';
import { useState, Dispatch, SetStateAction } from 'react';

interface UserProps {
   setId: Dispatch<SetStateAction<number>>;
}

export function FormUser({ setId }: UserProps) {
   const user_info = getInfo();
   const [displayEmail, setDisplayEmail] = useState('');
   const [displayPhone, setDisplayPhone] = useState('');
   useEffect(() => {
      setDisplayEmail(user_info.user.email);
      setDisplayPhone(user_info.user.phone);
      setId(user_info.user.user_id);
   }, [user_info.user.email, user_info.user.phone, user_info.user.user_id]);
   return (
      <React.Fragment>
         {/* Form UI for user info */}
         <List>
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <PersonIcon />
                  </Avatar>
               </ListItemAvatar>
               <ListItemText
                  primary="Username"
                  secondary={user_info.user.username}
               />
            </ListItem>
            <Divider />
            <FormEmail
               displayEmail={displayEmail}
               setDisplayEmail={setDisplayEmail}
            />
            <Divider />
            <FormPhone
               displayPhone={displayPhone}
               setDisplayPhone={setDisplayPhone}
            />
         </List>
      </React.Fragment>
   );
}
