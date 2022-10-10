import React from "react";
import { Grid, TextField } from "@mui/material";
import { useState } from "react";
import axios from "axios";

export default function Searchbar(props: any) {
    const [input, setInput] = useState("");
    
    function keyPress(e: any) {
        if (e.key === 'Enter') {
            // handle
        }
    }

    function handlePost(query: any) {
        var myParams = {
            data: query
        }
        if (query !== "") {
            axios.post('http://127.0.0.1:5000/login', myParams)
            .then(function(response) {
                console.log(response);
            })
            .catch(function(error) {
                console.log(error);
            });
        } else {
            alert("Query empty");
        }
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
                        }
                    }}
                />
                </div>
            </div>
        </div>
    );
}