import React from 'react';
import ReactDOM from "react-dom";
import styles from "./home.module.scss";

import sum from "utils/fight";

class HomePage extends React.Component {
  render() {
    return (
      <div className={styles.homeContainer}>
        Hello {sum(3, 8)}
        <ul>
          <li>hi</li>
          <li>hi</li>
          <li>hi</li>
        </ul>
      </div>
    );
  }
}

ReactDOM.render(<HomePage />, document.getElementById("app"));