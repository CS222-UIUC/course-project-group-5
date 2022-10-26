import React from "react";
import data from "../staticdata.json";
import "./SearchBarStyles.css";
import SingleCard from "./SingleCard";

interface Props {
    props: string;
}

const List = ({ props }: Props) => {
    // eslint-disable-next-line
    const filteredData = data.filter((el: any) => {
        if (props === '') {
            return el;
        } else if (el.name) {
            return el.name.toLowerCase().includes(props);
        }
    })
    return (
        <div className="list">
            {filteredData.splice(0, 5).map((apartment, index) => {
                if (props !== '') {
                    return (
                        <div key={index} className="box">
                            <p key={apartment.id}>{apartment.name}</p>
                        </div>
                    );
                }
            })}
        </div>
    );
}

export default List;
