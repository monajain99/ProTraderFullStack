import apisauce from "apisauce";
// import config from "./config"

const API_KEY = "PK0CDPFB1RM8SA4URUGW";
const SECRET_KEY = "Z8StsoZwwKFH0TLnJL8LvMfyyI6otN7bkEocWQZe";
const BASE_URL = "https://paper-api.alpaca.markets";

const alpacaApi = (baseURL = BASE_URL) => {
  const api = apisauce.create({
    baseURL: BASE_URL,
    headers: {
      "APCA-API-KEY-ID": API_KEY,
      "APCA-API-SECRET-KEY": SECRET_KEY,
    },
    timeout: 5000,
  });

  const getAccount = () => api.get("v2/account");
  const getPositions = () => api.get("v2/positions");

  return {
    getAccount,
    getPositions,
  };
};

export default alpacaApi; 

// export const getStocks = async () => {
//   const response = await fetch("/api/stocks")
//   return await response.json();
// };



