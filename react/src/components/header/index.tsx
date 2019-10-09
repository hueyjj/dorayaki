import React from 'react';

import styles from "./index.module.scss";
import logo from "assets/darky18.gif";

const Header = () => {
  return (
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
  );
}

export default Header;