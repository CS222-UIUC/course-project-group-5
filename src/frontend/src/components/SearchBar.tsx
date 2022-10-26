import React from "react";
import { useState } from "react";
import TextField from "@mui/material/TextField";
import List from "./List";
import "./SearchBarStyles.css";

const SearchBar = () => {
  const [inputText, setInputText] = useState("");
  return (
    <div className="main">
      <h1>Apartment Search</h1>
      <div className="search">
        <TextField
          id="outlined-basic"
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => setInputText(e.target.value.toLowerCase())}
          variant="outlined"
          fullWidth
          label="Search"
          className="myInput"
        />
      </div>
      <div className="myDropdown">
        <List props={inputText} /> 
      </div>
    </div>
  );
}

export default SearchBar;
