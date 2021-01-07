import React from "react";
import { NavLink } from "react-router-dom";
import DemoButton from "./auth/DemoButton";
import "../styles/Navbar.css";
import ProfileButton from "./auth/ProfileButton";
import LogoutButton from "./auth/LogoutButton";

// import Logo from "../assets/cropped.png";

const NavBar = ({ setAuthenticated, authenticated, user }) => {
  return (
    <div className="navContainer">
      <nav className="navbar">
        <ul className="linkList">
          <li className="left">
            <NavLink
              to="/"
              exact={true}
              className="links"
              activeClassName="active"
            >
              <img
                // src={Logo}
                alt="Logo"
                style={{ maxWidth: 80, height: "auto" }}
              />
            </NavLink>
          </li>
          {/* <div className="middle">{authenticated && <SearchInput />}</div> */}
          <div className="right">
            {authenticated ? (
              <>
                {/* <li>
                  <NavLink
                    to="/upload"
                    exact={true}
                    className="links"
                    activeClassName="active"
                  >
                    Upload
                  </NavLink>
                </li> */}
                <li>
                  <ProfileButton
                    user={user}
                    setAuthenticated={setAuthenticated}
                  />
                </li>
              </>
            ) : (
              <>
                <li>
                  <NavLink
                    to="/login"
                    exact={true}
                    className="links"
                    activeClassName="active"
                  >
                    Log In
                  </NavLink>
                </li>
                <li>
                  <NavLink
                    to="/sign-up"
                    exact={true}
                    className="links"
                    activeClassName="active"
                  >
                    Sign Up
                  </NavLink>
                </li>
                <li>
                  <NavLink to="/users" exact={true} activeClassName="active">
                    Users
                  </NavLink>
                </li>
                <li>
                  <LogoutButton setAuthenticated={setAuthenticated} />
                </li>
                <li>
                  <DemoButton
                    setAuthenticated={setAuthenticated}
                    authenticated={authenticated}
                  />
                </li>
              </>
            )}
          </div>
        </ul>
      </nav>
    </div>
  );
};

export default NavBar;
