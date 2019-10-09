import React from 'react';

import styles from "./index.module.scss";

const Footer = () => {
  return (
    <>
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
    </>
  );
}

export default Footer;