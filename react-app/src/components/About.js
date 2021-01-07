import React from "react";

export default class About extends React.Component {
  render() {
    return (
      <div>
        <br></br>
        <h1>ABOUT</h1>
        <p>
          <br></br>
          This is a website where users can trade stocks and can access its historical data.<br></br>
          section. Users interested in news can also use the News<br></br>
          tab to browse through most popular updates throughout their visit of
          our website.<br></br>
          <br></br>
        </p>
        <br></br>
        <h3>Created by</h3>
        <script
          type="text/javascript"
          src="https:profile.js"
          async
        ></script>
        <div
          className="LI-profile-badge"
          data-version="v1"
          data-size="large"
          data-locale="en_US"
          data-type="vertical"
          data-theme="light"
          data-vanity="Rashmi Jain"
        >
          <a
            className="LI-simple-link"
            href="LinkedIn"
          >
            Rashmi Jain
          </a>
        </div>
        <br></br>
        <br></br>
      </div>
    );
  }
}
