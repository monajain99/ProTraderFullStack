import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import HomeFeed from "./components/HomeFeed"
import { authenticate } from "./services/auth";
import 'bootstrap/dist/css/bootstrap.min.css'
import Account from "./components/Account";

function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async () => {
      const user = await authenticate();
      if (!user.errors) {
        setAuthenticated(true);
      }
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar setAuthenticated={setAuthenticated} />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <ProtectedRoute
          path="/users"
          exact={true}
          authenticated={authenticated}
        >
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute
          path="/users/:userId"
          exact={true}
          authenticated={authenticated}
        >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path="/" exact={true} authenticated={authenticated}>
          <h1>CandleStick Chart for MSFT</h1>
          <HomeFeed />
        </ProtectedRoute>
        <ProtectedRoute
          path="/trades"
          exact={true}
          authenticated={authenticated}
        >
          <h1>trades</h1>
        </ProtectedRoute>
        <ProtectedRoute
          path="/account"
          exact={true}
          authenticated={authenticated}
        >
          <h1>Account Value</h1>
          <Account/>
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
