import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
// const Alpaca = require(‘@alpacahq/alpaca-trade-api’);



function HomeFeed (){
  const [users, setUsers] = useState([]);
  const [news, setNews] = useState([]);

  // const { userId } = useParams();

 useEffect(() => {
    if (!users) {
      return;
    }
    async function fetchData() {
      const response = await fetch("/api/users/");
      const responseData = await response.json();
      setUsers(responseData.users);
      console.log(responseData.users[0]);
    }
    fetchData();
  }, []);

  if (!users) {
    return null;
  }

  return (
    <div className="wholePageContainer">
      <div className="bodyContainer">
        <div className="feedContainer">
          <h1 className="heading">HomeFeed</h1>
        </div>
      </div>
    </div>
  );
};

export default HomeFeed;
