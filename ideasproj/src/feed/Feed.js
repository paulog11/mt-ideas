import React, { Component } from "react";
import "./Feed.css";
import localData from "./localData";

class Feed extends Component {
    render() {
        return(
            <div>
                {localData.data1.author}
            </div>
        );
    }
}

export default Feed
