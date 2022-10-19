import React from "react";
import { TextField } from "@mui/material";
import { useState } from "react";
import axios from "axios";

export default function Searchbar(props: any) {
    const [input, setInput] = useState("");

    function handlePost(
        query: string
    ) {
        axios({
            method: 'post',
            url: '/login', // need mainpage.py url
            data: {
                query: query
            },
        })
        .then((response) => {
            console.log(response);
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
            }
         });
    }

    return (
        <div className="main">
            <h1>Search</h1>
            <div style={{display: 'flex', justifyContent: 'center'}}>
                <div className="search" style={{width: '800px'}}>
                <TextField
                    id="outlined-basic"
                    variant="outlined"
                    fullWidth
                    value={input || ''}
                    label="Apartment Search"
                    onKeyDown={(e: any) => {
                        if (e.key === 'Enter') {
                            e.preventDefault();
                            console.log(e.target.value);
                            handlePost(e.target.value);
                        }
                    }}
                    onChange={(e: any) => setInput(e.target.value)}
                />
                </div>
            </div>
        </div>
    );
}