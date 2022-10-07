import React from "react";
import { Grid, TextField } from "@mui/material";
import { useState } from "react";
import axios from "axios";

export default function Searchbar(props: any) {
    const [inputText, setInputText] = useState("");
    let inputHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
        var convertToLowerCase = e.target.value.toLowerCase();
        setInputText(convertToLowerCase);
    };
    function handlePost(query) {
        var myParams = {
            data: query
        }
        if (query !== "") {
            axios.post('http://127.0.0.1:5000/login', {
        }
        

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
                    onChange={inputHandler}
                    fullWidth
                    label="Apartment Search"
                />
                </div>
            </div>
        </div>
    );
}