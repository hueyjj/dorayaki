import React from 'react';
import ReactDOM from "react-dom";

import Header from "components/header";
import Footer from "components/footer";
import Thread from "components/thread";

import styles from "./home.module.scss";

class HomePage extends React.Component {
  render() {
    const lots = []
    for (let i = 0; i < 30; i++) {
      lots.push(
        <Thread
          key={i}
          rank={5}
          title="My title"
          points={10}
          user="hueyjj"
          datePosted="13 hours ago"
          comments={511}
          commentsLink="example.com"
          threadLink="example.com"
        />
      );
    }
    return (
      <div className={styles.centerContainer}>
        <Header />
        {lots}
        <Footer />
      </div>
    );
  }
}

ReactDOM.render(<HomePage />, document.getElementById("app"));