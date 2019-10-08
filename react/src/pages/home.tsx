import React from 'react';
import ReactDOM from "react-dom";

import Thread from "components/thread";

import styles from "./home.module.scss";
import logo from "assets/darky18.gif";

class HomePage extends React.Component {
  render() {
    return (
      <div className={styles.centerContainer}>
        <div className={styles.header}>
          <a className={styles.logoLink} href="/">
            <img src={logo} />
          </a>
          <ul className={styles.links}>
            <li>
              <b>
                <span className={styles.title}>Hacker News</span>
              </b>
            </li>
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
        <Thread
          rank={5}
          title="My title"
          points={10}
          user="hueyjj"
          datePosted="13 hours ago"
          comments={511}
          commentsLink="example.com"
          threadLink="example.com"
        />
      </div>
    );
  }
}

ReactDOM.render(<HomePage />, document.getElementById("app"));