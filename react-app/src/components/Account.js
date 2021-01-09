import React, { useState, useEffect } from "react";
import alpacaApi from "../services/trade";

import "bootstrap/dist/css/bootstrap.min.css";


const Account = () => {
  const [buying_power, setBuying_power] = useState([]);
  const [cash, setCash] = useState([0]);
  const [long_market_value, setLong_market_value] = useState([0]);
  const [portfolio_value, setPortfolio_value] = useState([0]);


  useEffect(() => {
    const api = alpacaApi()

        api.getAccount().then((response) => {
          const  data =response.data;

          if (response.ok) {
            setBuying_power(data.buying_power);
            setCash(data.cash);
            setLong_market_value(data.long_market_value);
            setPortfolio_value(data.portfolio_value);
            }
        })
  }, []);

  return (
    <div>
      Buying power     {buying_power}
      <div>
        Cash             {cash}
        </div>
      PortFolio Value
      {portfolio_value}
    </div>
  );
};

export default Account


// export default class About extends React.Component {
//   render() {
//     return (
//       <div>
//         <br></br>
//         <h1>ABOUT</h1>
//         <p>
//           <br></br>
//           This is a website where users can trade stocks and can access its historical data.<br></br>
//           section. Users interested in news can also use the News<br></br>
//           tab to browse through most popular updates throughout their visit of
//           our website.<br></br>
//           <br></br>
//         </p>
//         <br></br>
//         <h3>Created by</h3>
//         <script
//           type="text/javascript"
//           src="https:profile.js"
//           async
//         ></script>
//         <div
//           className="LI-profile-badge"
//           data-version="v1"
//           data-size="large"
//           data-locale="en_US"
//           data-type="vertical"
//           data-theme="light"
//           data-vanity="Rashmi Jain"
//         >
//           <a
//             className="LI-simple-link"
//             href="LinkedIn"
//           >
//             Rashmi Jain
//           </a>
//         </div>
//         <br></br>
//         <br></br>
//       </div>
//     );
//   }
// }
