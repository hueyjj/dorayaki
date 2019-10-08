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
      <span className={styles.rank}>{props.rank}.</span>
      <span className={styles.upvote}>▲</span>
      <div>
        <div>
          <a href={props.threadLink}>{props.title}</a>
          <a href="/">(cleaned url)</a>
        </div>
        <div>
          <span>{props.points} points by {props.user} {props.datePosted} | </span>
          <a href="/">hide</a>
          <span> | {props.comments} comments</span>
        </div>
      </div>
    </div>
  );
}

export default Thread;