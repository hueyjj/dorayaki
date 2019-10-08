import React from 'react';
import ReactDOM from "react-dom";

import styles from "./home.module.scss";

import logo from "assets/darky18.gif";

class HomePage extends React.Component {
  render() {
    return (
      <div className={styles.centerContainer}>
        <div className={styles.header}>
          <a href="/"><img src={logo}></img></a>
          <span>Hacker News</span>
          <ul className={styles.links}>
            <li>
              <a href="/newest">new</a>
              <span> | </span>
            </li>
            <li>
              <a href="/front">past</a>
              <span> | </span>
            </li>
            <li>
              <a href="/newcomments">comments</a>
              <span> | </span>
            </li>
            <li>
              <a href="/ask">ask</a>
              <span> | </span>
            </li>
            <li>
              <a href="/show">show</a>
              <span> | </span>
            </li>
            <li>
              <a href="/jobs">jobs</a>
              <span> | </span>
            </li>
            <li>
              <a href="/submit">submit</a>
            </li>
          </ul>
          <a className={styles.login} href="/login">login</a>
        </div>
      </div>
    );
  }
}

ReactDOM.render(<HomePage />, document.getElementById("app"));