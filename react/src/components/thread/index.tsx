import React from 'react';

import styles from "./index.module.scss";

interface ThreadProps {
  rank: number;
  title: string;
  points: number;
  user: string;
  datePosted: string;
  comments: number;
  commentsLink: string;
  threadLink: string;
}

const Thread = (props: ThreadProps) => {
  return (
    <div className={styles.threadContainer}>
      <span className={styles.rank}>{props.rank}</span>
      <span>▲</span>
    </div>
  );
}

export default Thread;