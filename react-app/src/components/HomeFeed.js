import React, { useState, useEffect } from "react";
import ChartJS from "./Chartutils/Chart";
import MadeData from "./Chartutils/Data";
import "bootstrap/dist/css/bootstrap.min.css";

// const Alpaca = require(‘@alpacahq/alpaca-trade-api’);


const HomeFeed = () => {

  const [chartsToDisplay, setChartsToDisplay] = useState([]);
  const [users, setUsers] = useState([]);


  const getData = async () => {
    const charts = [];
    charts.push(<ChartJS key={1} data={MadeData} />);
    setChartsToDisplay(charts);
  };

  useEffect(() => {
    getData();
  }, []);

  return <div className="App">{chartsToDisplay}</div>;
};


export default HomeFeed;
