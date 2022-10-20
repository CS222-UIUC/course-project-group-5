import React from "react";
import PreviewBlock from "../components/LeftSideScrollBlocks";
import Searchbar from "../components/Searchbar";

export default function LeftSection(props: any) {
    return (
        <div style={{marginTop: '200px'}}>
            <Searchbar/>
            <PreviewBlock/>
        </div>
    );
}