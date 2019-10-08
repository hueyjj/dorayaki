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
        <Thread
          rank={22}
          title="My title"
          points={10}
          user="hueyjj"
          datePosted="13 hours ago"
          comments={511}
          commentsLink="example.com"
          threadLink="example.com"
        />
        <Thread
          rank={222}
          title="My title"
          points={10}
          user="hueyjj"
          datePosted="13 hours ago"
          comments={511}
          commentsLink="example.com"
          threadLink="example.com"
        />
        <hr className={styles.line} />
        <div className={styles.footer}>
          <ul>
            <li>
              <a href="/">Guidelines</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">FAQ</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">Support</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">API</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">Security</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">Lists</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">Bookmarklet</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">Legal</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">Apply to YC</a>
              <span> | </span>
            </li>
            <li>
              <a href="/">Contact</a>
            </li>
          </ul>
          <form
            method="GET"
            action="/"
          >
            <div className={styles.search}>
              <label htmlFor="search">Search: </label>
              <input
                type="text"
                id="search"
              />
            </div>
          </form>
        </div>
      </div>
    );
  }
}

ReactDOM.render(<HomePage />, document.getElementById("app"));