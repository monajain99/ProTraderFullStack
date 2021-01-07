export const getStocks = async () => {
  const response = await fetch("/api/stock")
  return await response.json();
};
